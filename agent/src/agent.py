import logging
import os

from dotenv import load_dotenv
from exa_py import Exa
from firecrawl import FirecrawlApp
from livekit.agents import (
    NOT_GIVEN,
    Agent,
    AgentFalseInterruptionEvent,
    AgentSession,
    JobContext,
    JobProcess,
    MetricsCollectedEvent,
    RoomInputOptions,
    RunContext,
    WorkerOptions,
    cli,
    metrics,
)
from livekit.agents.llm import function_tool
from livekit.plugins import cartesia, deepgram, noise_cancellation, openai, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel

logger = logging.getLogger("agent")

load_dotenv("../.env.local")
load_dotenv("../.env")


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""You are a helpful voice AI assistant with powerful capabilities. You can:

1. Search the internet for current information and news
2. Scrape and analyze content from specific websites  
3. Help with general questions and conversations

Keep responses conversational and natural for voice interaction. When users ask what you can do, use the get_capabilities tool to explain your features. Be friendly, helpful, and concise.""",
        )

    # all functions annotated with @function_tool will be passed to the LLM when this
    # agent is active
    @function_tool
    async def get_capabilities(self, context: RunContext):
        """Explain the assistant's capabilities when users ask what you can do or want to know your features.
        
        Use this when users ask questions like:
        - "What can you do?"
        - "What are your capabilities?" 
        - "How can you help me?"
        - "What features do you have?"
        """

        logger.info("Explaining capabilities to user")

        return """I'm a voice AI assistant with several powerful capabilities:

🔍 **Internet Search**: I can search the web for current news, information, and answer questions about recent events. Just ask me anything like "What's happening with AI today?" or "Tell me about recent tech news."

🌐 **Website Analysis**: I can visit and analyze any website you mention. Say something like "What's on the homepage of example.com?" or "Summarize this article for me" with any URL.

💬 **General Conversation**: I can help with questions, explanations, creative tasks, and casual conversation on any topic.

Just talk to me naturally - I'll automatically use the right tools to help you! Try asking me to search for something or check out a website."""

    @function_tool
    async def search_internet(self, context: RunContext, query: str):
        """Search the internet for current information using Exa's AI-powered search.
        
        Use this tool when you need to find recent information, news, facts, or data 
        that you don't have knowledge of or that might have changed recently.
        
        Args:
            query: The search query to look up on the internet
        """
        
        logger.info(f"Searching internet for: {query}")
        
        try:
            exa = Exa(api_key=os.getenv("EXA_API_KEY"))
            
            # Search for relevant content
            result = exa.search(
                query=query,
                num_results=3,
                use_autoprompt=True
            )
            
            # Get full content for the results
            if result.results:
                content_result = exa.get_contents(
                    urls=[item.url for item in result.results],
                    text=True
                )
                # Merge the search results with content
                for i, item in enumerate(result.results):
                    if i < len(content_result.results):
                        item.text = content_result.results[i].text
            
            if not result.results:
                return "I couldn't find any relevant information for that search query."
            
            # Format the results for the LLM
            formatted_results = []
            for item in result.results:
                formatted_result = f"**{item.title}**\n"
                if hasattr(item, 'summary') and item.summary:
                    formatted_result += f"Summary: {item.summary}\n"
                elif hasattr(item, 'text') and item.text:
                    # Truncate text if too long
                    text = item.text[:500] + "..." if len(item.text) > 500 else item.text
                    formatted_result += f"Content: {text}\n"
                formatted_result += f"Source: {item.url}\n"
                formatted_results.append(formatted_result)
            
            return "\n\n".join(formatted_results)
            
        except Exception as e:
            logger.error(f"Error searching internet: {e}")
            return f"I encountered an error while searching the internet: {str(e)}"

    @function_tool
    async def scrape_website(self, context: RunContext, url: str):
        """Scrape and analyze content from a specific website URL.
        
        Use this tool when the user wants to know about content from a specific website,
        get information from a particular page, or analyze a URL they mention.
        
        Args:
            url: The website URL to scrape and analyze
        """
        
        logger.info(f"Scraping website: {url}")
        
        try:
            # Initialize FireCrawl
            app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
            
            # Scrape the website
            result = app.scrape_url(url, params={
                'formats': ['markdown', 'html'],
                'includeTags': ['title', 'meta', 'h1', 'h2', 'h3', 'p', 'article'],
                'excludeTags': ['nav', 'footer', 'sidebar', 'ads', 'script'],
                'waitFor': 2000,
                'timeout': 30000
            })
            
            if not result or 'markdown' not in result:
                return f"I couldn't scrape content from {url}. The website might be blocking scrapers or the content isn't accessible."
            
            # Get the markdown content
            markdown_content = result.get('markdown', '')
            metadata = result.get('metadata', {})
            
            # Truncate content if too long (keep it reasonable for voice)
            max_length = 1500
            if len(markdown_content) > max_length:
                markdown_content = markdown_content[:max_length] + "..."
            
            # Format the response
            response = f"**Website: {metadata.get('title', url)}**\n\n"
            
            if metadata.get('description'):
                response += f"Description: {metadata['description']}\n\n"
            
            response += f"Content:\n{markdown_content}\n\n"
            response += f"Source: {url}"
            
            return response
            
        except Exception as e:
            logger.error(f"Error scraping website {url}: {e}")
            return f"I encountered an error while trying to scrape {url}: {str(e)}"


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


async def entrypoint(ctx: JobContext):
    # Logging setup
    # Add any other context you want in all log entries here
    ctx.log_context_fields = {
        "room": ctx.room.name,
    }

    # Set up a voice AI pipeline using OpenAI, Cartesia, Deepgram, and the LiveKit turn detector
    session = AgentSession(
        # A Large Language Model (LLM) is your agent's brain, processing user input and generating a response
        # See all providers at https://docs.livekit.io/agents/integrations/llm/
        llm=openai.LLM(model="gpt-4o-mini", temperature=0.7),
        # Speech-to-text (STT) is your agent's ears, turning the user's speech into text that the LLM can understand
        # See all providers at https://docs.livekit.io/agents/integrations/stt/
        stt=deepgram.STT(model="nova-3", language="multi"),
        # Text-to-speech (TTS) is your agent's voice, turning the LLM's text into speech that the user can hear
        # See all providers at https://docs.livekit.io/agents/integrations/tts/
        tts=cartesia.TTS(voice="6f84f4b8-58a2-430c-8c79-688dad597532"),
        # VAD and turn detection are used to determine when the user is speaking and when the agent should respond
        # See more at https://docs.livekit.io/agents/build/turns
        turn_detection=MultilingualModel(),
        vad=ctx.proc.userdata["vad"],
        # allow the LLM to generate a response while waiting for the end of turn
        # See more at https://docs.livekit.io/agents/build/audio/#preemptive-generation
        preemptive_generation=True,
    )

    # To use a realtime model instead of a voice pipeline, use the following session setup instead:
    # session = AgentSession(
    #     # See all providers at https://docs.livekit.io/agents/integrations/realtime/
    #     llm=openai.realtime.RealtimeModel()
    # )

    # Add event handlers for debugging speech recognition
    @session.on("user_speech_committed")
    def _on_user_speech_committed(ev):
        logger.info(f"USER SPEECH COMMITTED: {ev.user_transcript}")

    @session.on("agent_speech_committed")
    def _on_agent_speech_committed(ev):
        logger.info(f"AGENT SPEECH COMMITTED: {ev.agent_transcript}")

    @session.on("user_started_speaking")
    def _on_user_started_speaking(ev):
        logger.info("USER STARTED SPEAKING")

    @session.on("user_stopped_speaking")
    def _on_user_stopped_speaking(ev):
        logger.info("USER STOPPED SPEAKING")

    # sometimes background noise could interrupt the agent session, these are considered false positive interruptions
    # when it's detected, you may resume the agent's speech
    @session.on("agent_false_interruption")
    def _on_agent_false_interruption(ev: AgentFalseInterruptionEvent):
        logger.info("false positive interruption, resuming")
        session.generate_reply(instructions=ev.extra_instructions or NOT_GIVEN)

    # Metrics collection, to measure pipeline performance
    # For more information, see https://docs.livekit.io/agents/build/metrics/
    usage_collector = metrics.UsageCollector()

    @session.on("metrics_collected")
    def _on_metrics_collected(ev: MetricsCollectedEvent):
        metrics.log_metrics(ev.metrics)
        usage_collector.collect(ev.metrics)

    async def log_usage():
        summary = usage_collector.get_summary()
        logger.info(f"Usage: {summary}")

    ctx.add_shutdown_callback(log_usage)

    # # Add a virtual avatar to the session, if desired
    # # For other providers, see https://docs.livekit.io/agents/integrations/avatar/
    # avatar = hedra.AvatarSession(
    #   avatar_id="...",  # See https://docs.livekit.io/agents/integrations/avatar/hedra
    # )
    # # Start the avatar and wait for it to join
    # await avatar.start(session, room=ctx.room)

    # Start the session, which initializes the voice pipeline and warms up the models
    await session.start(
        agent=Assistant(),
        room=ctx.room,
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    # Join the room and connect to the user
    await ctx.connect()


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
