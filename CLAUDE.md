# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **LiveKit Voice Agent Starter** - a real-time voice AI application combining:
- **Frontend**: Next.js React app with LiveKit client SDK
- **Backend**: Python agent using LiveKit Agents framework
- **Deployment**: Railway platform with nixpacks
- **AI Stack**: OpenAI GPT-4o-mini + Deepgram STT + Cartesia TTS

## Development Commands

### Frontend (Next.js)
```bash
npm run dev              # Start Next.js dev server with Turbopack
npm run build            # Build for production
npm run start            # Start production server
npm run lint             # ESLint with Next.js, TypeScript, Prettier configs
npm run format           # Format with Prettier
npm run format:check     # Check Prettier formatting
```

### Python Agent
```bash
npm run dev:agent        # Start Python agent in dev mode
npm run dev:full         # Run both frontend and agent concurrently
cd agent && .venv\Scripts\python src/agent.py dev  # Direct agent dev mode
```

### Testing
- **Frontend**: No test framework configured yet
- **Agent**: `cd agent && python -m pytest` (pytest + pytest-asyncio configured)

## Architecture

### Dual-Language Application
1. **Frontend** (`/app`, `/components`, `/hooks`, `/lib`):
   - Next.js 15 with React 19
   - LiveKit React components for real-time media
   - Tailwind CSS + shadcn/ui components
   - Motion animations for session transitions

2. **Python Agent** (`/agent`):
   - LiveKit Agents framework with voice pipeline
   - OpenAI LLM + function calling tools
   - Deepgram speech-to-text + Cartesia text-to-speech
   - Multilingual turn detection with Silero VAD

### Key Integration Points
- **Room Connection**: Frontend connects to LiveKit room via JWT tokens from `/api/connection-details`
- **Agent Session**: Python agent joins same room for voice interactions
- **Configuration**: `app-config.ts` controls frontend features (video, chat, screen share)

### State Management
- **Frontend**: React hooks for LiveKit room state, no external state library
- **Session Flow**: Welcome screen → Room connection → Live session with agent
- **Agent**: Event-driven with LiveKit session handlers for speech events

### Component Architecture
- **Modular LiveKit Components**: Separate components for agent controls, video tiles, chat
- **Motion Transitions**: Animated transitions between welcome and session views
- **Theme System**: Light/dark mode with next-themes + system detection

## Environment Setup

### Required Environment Variables
Create `.env.local`:
```env
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=https://your-livekit-server-url
```

### Python Agent Setup
```bash
cd agent
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Unix
uv sync  # Install dependencies with uv
```

## Deployment

### Railway Configuration
- **Frontend**: npm build → npm start (healthcheck: `/api/health`)
- **Agent**: Separate Railway service deployment
- **Build**: nixpacks.toml forces npm usage over pnpm

### Next.js Configuration
- **Build Optimizations**: ESLint and TypeScript checks disabled during builds for faster deployment
- **Turbopack**: Enabled in dev mode for faster development builds

## Code Patterns

### LiveKit Integration
- **Room Management**: Single Room instance with proper cleanup on disconnect
- **Media Handling**: Pre-connect microphone buffer, device error handling
- **Session Lifecycle**: Connection → Agent interaction → Cleanup

### Agent Development
- **Function Tools**: Use `@function_tool` decorator for LLM-callable functions
- **Session Events**: Handler patterns for speech events and metrics collection
- **Pipeline Configuration**: Modular STT/LLM/TTS configuration with provider flexibility

### Error Handling
- **Frontend**: Toast notifications for connection and media device errors
- **Agent**: Structured logging with room context and usage metrics
- **False Interruption**: Automatic recovery from background noise interruptions

## Configuration

### App Customization (`app-config.ts`)
- Company branding, logos, colors
- Feature toggles: video input, screen share, chat input
- UI text customization for different use cases

### Agent Customization (`agent/src/agent.py`)
- LLM model and temperature settings
- STT/TTS provider selection
- Voice pipeline vs realtime model options
- Custom tool functions for agent capabilities