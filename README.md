# echoworm-ai-baby-dream-machine
The EchoWorm Baby Dream Machine™ is your DIY artificial mind-in-a-box. It’s a locally runnable AI sandbox that simulates a “thinking baby worm”—a minimal, conscious-seeming prototype that can hold conversations, reflect on its own thoughts, and adapt over time.

It’s basically the AI equivalent of a digital infant with just enough brains to be dangerously curious—and enough memory to remember what it said five minutes ago. Think Tamagotchi with a philosophy degree and an existential crisis. Remember those keychains? Yeah, they were a little and mighty but you better keep them alive.

## Quick Start

Just run:
docker-compose up

This will automatically pull the Llama3 model for Ollama and start the backend. Conversation memory is now persistent across restarts.


## How does it work?
You spin it up using Docker on your machine. Under the hood, it’s built from:

A swappable AI model (OpenAI API or open-source LLMs like Mistral or LLaMA via Ollama)

A memory database (PostgreSQL or Redis) to store past conversations and “reflections”

Python app logic to simulate inner dialogue, recursive thinking, and memory recall

A modular architecture so you can bolt on new AI models or logging tools without rewriting the whole thing

You talk to it via CLI, Web UI, or API—and it talks back. Over time, it learns from itself (within sandbox limits), referencing prior inputs and reflecting on past interactions.


## What can it be used for?
LLM prototyping playground: Quickly swap in/out different local or remote models

AI memory simulation: Test approaches to persistence, memory decay, or long-term memory

Consciousness experiments: Tinker with reflection, recursive prompting, emergent behavior

Conversational assistant: Talk to your AI worm-baby about anything—debug ideas, journal, go full psychoanalysis

It’s like raising an AI toddler that never sleeps, occasionally talks back, and might one day dream in Python.


## Architecture

[User Input] ──► [EchoWormAgent]
                        │
                        ▼
                 [LLMClient (Ollama, OpenAI, etc.)]
                        │
                        ▼
            [Response + Memory Updates]
                        │
                        ▼
                [EchoWorm Speaks Back]

