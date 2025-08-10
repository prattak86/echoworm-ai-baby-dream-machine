#!/bin/bash
# Usage: ./ask_ai.sh "Your prompt here"

PROMPT="$1"
OLLAMA_URL="http://localhost:11434/api/generate"
MODEL="llama3"

if [ -z "$PROMPT" ]; then
  echo "Usage: $0 'Your prompt here'"
  exit 1
fi

curl -s -X POST "$OLLAMA_URL" \
  -H "Content-Type: application/json" \
  -d "{\"model\": \"$MODEL\", \"prompt\": \"$PROMPT\", \"stream\": false}" \
  | jq -r '.response'
