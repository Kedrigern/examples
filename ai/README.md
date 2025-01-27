# AI Examples Repository

This repository demonstrates AI integration using two powerful libraries:
- [Pydantic AI](https://ai.pydantic.dev/) - A type-safe framework for AI model interactions
- [Autogen](https://microsoft.github.io/autogen/) (v0.4) - A framework for building AI agents

## Model Provider Comparison

### Development Consoles and Pricing

| Provider | Development Console | Pricing Plans |
|----------|-------------------|---------------|
| Google | [AI Studio](https://aistudio.google.com) | [Plan Details](https://aistudio.google.com/plan_information) |
| OpenAI | [Platform](https://platform.openai.com) | [Pricing](https://openai.com/api/pricing/) |
| Anthropic | [Console](https://console.anthropic.com) | [Usage Limits](https://console.anthropic.com/settings/limits) |
| Groq | [Console](https://console.groq.com) | TBA |

### Available Models and Rate Limits

| Provider | Model | Free Tier Rate Limit |
|----------|-------|---------------------|
| Google | gemini-1.5-flash | 15 RPM |
| Google | gemini-1.5-pro | 2 RPM |
| OpenAI | gpt-4-turbo | - |
| OpenAI | gpt-4 | - |
| Anthropic | claude-3-sonnet | 5 RPM |
| Groq | llama-3.3-70b-versatile | 30 RPM |

*RPM = Requests Per Minute*

## Getting Started

Structure is `/framework/example`. Each example is managed by [uv](https://docs.astral.sh/uv/), so just:

```
uv sync
uv run <script>.py
```

before you need to create `.env` file in root directory. There is `.env.example`.

## Library Details

### Pydantic AI

Pydantic AI is a clean, user-friendly framework that provides comprehensive coverage of available AI models. Key features:
- Type-safe interactions with AI models
- Built-in validation and error handling
- Seamless integration with popular AI providers
- Extensive model support

### Autogen

Autogen is a powerful framework for creating and managing AI agents. Important notes:

- **Version Compatibility**: Major changes exist between versions 0.2 and 0.4
- **Web Interface**: Launch with `autogenstudio ui --port 8080`
- **Key Features**:
  - Easy agent configuration
  - Multi-agent task solving
  - Built-in collaboration capabilities
  - Flexible architecture for custom workflows
