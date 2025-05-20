    adk api_server


    curl -X POST http://0.0.0.0:8000/apps/multi_tool_agent/users/u_123/sessions/s_123 \
    -H "Content-Type: application/json" \
    -d '{"state": {}}'

    curl -X POST http://0.0.0.0:8000/run \
    -H "Content-Type: application/json" \
    -d '{
    "app_name": "multi_tool_agent",
    "user_id": "u_123",
    "session_id": "s_123",
    "new_message": {
        "role": "user",
        "parts": [{
        "text": "User ram@gmail.com logged in now"
        }]
    }
    }'


    curl -X POST http://0.0.0.0:8000/run \
    -H "Content-Type: application/json" \
    -d '{
    "app_name": "multi_tool_agent",
    "user_id": "u_123",
    "session_id": "s_123",
    "new_message": {
        "role": "user",
        "parts": [{
        "text": "User logged in now with phno 9988936878"
        }]
    }
    }'