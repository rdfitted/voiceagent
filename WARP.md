# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Development Commands

### Frontend (Next.js)
- `pnpm install` - Install dependencies
- `pnpm dev` - Start development server with TurboWhatPack at http://localhost:3000
- `pnpm build` - Build for production
- `pnpm start` - Start production server
- `pnpm lint` - Run ESLint
- `pnpm format` - Format code with Prettier
- `pnpm format:check` - Check code formatting

### Agent (Python)
- `cd agent && uv sync` - Install Python dependencies in virtual environment
- `cd agent && uv run python src/agent.py download-files` - Download required models (run before first use)
- `cd agent && uv run python src/agent.py console` - Test agent directly in terminal
- `cd agent && uv run python src/agent.py dev` - Run agent for development (connects to frontend)
- `cd agent && uv run python src/agent.py start` - Run agent for production
- `cd agent && uv run pytest` - Run agent tests and evaluations

### Combined Development
- `pnpm dev:full` - Start both frontend and agent simultaneously
- `pnpm dev:agent` - Start just the Python agent from root directory

### Task Runner Commands
Both root and agent directories have `taskfile.yaml`:
- `task install` - Bootstrap dependencies
- `task dev` - Start development mode

## Architecture Overview

This is a **dual-stack voice AI application** using LiveKit for real-time communication:

### Frontend Architecture (Next.js + React)
- **App Router structure** with server components in `app/` directory
- **Component organization**:
  - `components/livekit/` - LiveKit-specific React components (chat, media tiles, agent controls)
  - `components/ui/` - Shadcn/UI base components with Radix UI primitives
  - `hooks/` - Custom React hooks for chat, connection management, and debug mode
- **Configuration system**: `app-config.ts` controls branding, features, and UI behavior
- **Real-time features**: Voice interaction, video streaming, screen sharing, chat messaging
- **Styling**: TailwindCSS with CSS variables for theming, motion animations with Framer Motion

### Backend Architecture (Python Agent)
- **LiveKit Agents framework** for voice AI pipeline
- **Modular AI stack**:
  - LLM: OpenAI (configurable to other providers)
  - TTS: Cartesia (configurable)
  - STT: Deepgram (configurable)  
  - Turn detection: LiveKit Turn Detector
  - VAD: Silero Voice Activity Detection
- **Production ready** with Docker support and comprehensive eval suite

### Key Integration Points
- **Environment variables**: Both frontend and agent share LiveKit credentials (`.env.local`)
- **Real-time communication**: WebRTC through LiveKit rooms for bidirectional audio/video/data
- **Agent lifecycle**: Frontend triggers agent connection, agent manages conversation state
- **Message flow**: Chat messages and transcriptions synchronized between frontend and agent

### Development Workflow
1. **Environment setup**: Copy `.env.example` to `.env.local` with LiveKit credentials
2. **Model initialization**: Run agent download-files command before first use  
3. **Dual development**: Use `pnpm dev:full` to run both frontend and agent together
4. **Component testing**: Visit `/components/base` and `/components/livekit` for UI component showcase

### Production Deployment
- **Frontend**: Standard Next.js deployment (build → start)
- **Agent**: Containerized Python service with included Dockerfile
- **Infrastructure**: Requires LiveKit Cloud or self-hosted LiveKit server
