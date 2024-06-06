curl http://localhost:9999/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer EMPTY" \
  -d '{
     "model": "qwen",
     "messages": [{"role": "user", "content": "你是谁"}],
     "temperature": 0
   }'
