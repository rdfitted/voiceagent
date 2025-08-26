# Voice AI Assistant Boilerplate

A production-ready boilerplate for building intelligent voice AI assistants. Features a modern React frontend with a Python agent backend that includes internet search, website scraping, and an extensible tool system.

**Built with:** LiveKit Agents, React, Next.js, OpenAI, Exa AI, and FireCrawl.

**Created by [Fitted Automation](https://github.com/fitted-automation)** - Intelligent automation solutions.

<picture>
  <source srcset="./.github/assets/readme-hero-dark.webp" media="(prefers-color-scheme: dark)">
  <source srcset="./.github/assets/readme-hero-light.webp" media="(prefers-color-scheme: light)">
  <img src="./.github/assets/readme-hero-light.webp" alt="App screenshot">
</picture>

### Features:

**🎙️ Voice AI Capabilities:**
- Real-time voice interaction with LiveKit Agents
- Internet search powered by Exa AI
- Website scraping and analysis via FireCrawl
- Extensible tool system for adding new capabilities

**💻 Frontend (Next.js):**
- Modern React 19 + Next.js 15 interface
- Real-time audio visualization and controls
- Camera video streaming and screen sharing
- Light/dark theme with system detection
- Customizable branding and configuration

**🐍 Backend (Python Agent):**
- LiveKit Agents framework with OpenAI GPT-4
- Deepgram speech-to-text + Cartesia text-to-speech
- Function calling tool system
- Production-ready error handling and logging

This template is built with Next.js and is free for you to use or modify as you see fit.

### Project structure

```
agent-starter-react/
├── app/
│   ├── (app)/
│   ├── api/
│   ├── components/
│   ├── fonts/
│   ├── globals.css
│   └── layout.tsx
├── components/
│   ├── livekit/
│   ├── ui/
│   ├── app.tsx
│   ├── session-view.tsx
│   └── welcome.tsx
├── hooks/
├── lib/
├── public/
└── package.json
```

## Getting started

**⚡ Quick Start Guide** - Get your voice AI assistant running in minutes!

Clone this repository to get started:

```bash
git clone https://github.com/rdfitted/voiceagent.git
cd voiceagent
```

Then run the development environment:

```bash
# Install frontend dependencies
npm install

# Install Python agent dependencies
cd agent && uv sync
cd ..

# Run both frontend and agent together
npm run dev:full
```

Open http://localhost:3000 in your browser and start talking to your AI assistant!

**Alternative commands:**
- `npm run dev` - Frontend only
- `npm run dev:agent` - Python agent only

## Configuration

This starter is designed to be flexible so you can adapt it to your specific agent use case. You can easily configure it to work with different types of inputs and outputs:

#### Example: App configuration (`app-config.ts`)

```ts
export const APP_CONFIG_DEFAULTS = {
  companyName: 'LiveKit',
  pageTitle: 'LiveKit Voice Agent',
  pageDescription: 'A voice agent built with LiveKit',
  supportsChatInput: true,
  supportsVideoInput: true,
  supportsScreenShare: true,
  logo: '/lk-logo.svg',
  accent: '#002cf2',
  logoDark: '/lk-logo-dark.svg',
  accentDark: '#1fd5f9',
  startButtonText: 'Start call',
};
```

You can update these values in [`app-config.ts`](./app-config.ts) to customize branding, features, and UI text for your deployment.

#### Environment Variables

Copy `.env.example` to `.env` and configure your API keys:

```env
# LiveKit Configuration (required)
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=https://your-livekit-server-url

# AI Provider APIs
OPENAI_API_KEY=your_openai_api_key
DEEPGRAM_API_KEY=your_deepgram_api_key
CARTESIA_API_KEY=your_cartesia_api_key

# Tool APIs (optional)
EXA_API_KEY=your_exa_api_key           # For internet search
FIRECRAWL_API_KEY=your_firecrawl_api_key # For website scraping
```

**Required for basic functionality:**
- LiveKit credentials (create free account at [livekit.io](https://livekit.io))
- OpenAI API key for the LLM brain
- Deepgram API key for speech-to-text  
- Cartesia API key for text-to-speech

**Optional for enhanced features:**
- Exa API key enables internet search capabilities
- FireCrawl API key enables website scraping

## Built-in Tools

The assistant comes with three powerful tools:

1. **🔍 Internet Search** (`search_internet`) - Uses Exa AI to search the web for current information
2. **🌐 Website Scraper** (`scrape_website`) - Uses FireCrawl to analyze any website URL
3. **💡 Capabilities Guide** (`get_capabilities`) - Explains what the assistant can do

### Adding New Tools

To add your own tools, simply add a new method to the `Assistant` class:

```python
@function_tool
async def your_custom_tool(self, context: RunContext, param: str):
    """Tool description for the LLM."""
    # Your tool logic here
    return "Tool response"
```

## Contributing

This boilerplate is open source and we welcome contributions! Please open a PR or issue through GitHub.

## About Fitted Automation

Fitted Automation specializes in intelligent automation solutions. This voice AI assistant boilerplate represents our commitment to making advanced AI technology accessible and easy to implement.

For more automation solutions and tools, visit [Fitted Automation](https://fitted-automation.com/).
