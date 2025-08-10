#!/bin/sh
ollama serve &
# Wait for the server to be up
until curl -s http://localhost:11434 > /dev/null; do
  echo "Waiting for Ollama server..."
  sleep 2
done
ollama pull llama3
wait