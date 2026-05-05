import ollama

chat_memory = []

def ask_ai(message):
    global chat_memory

    try:
        # Save user message
        chat_memory.append({
            "role": "user",
            "content": message
        })

        # Keep memory short
        messages = [
            {
                "role": "system",
                "content": "You are a smart, helpful, professional AI assistant."
            }
        ] + chat_memory[-6:]

        # Use memory messages
        response = ollama.chat(
            model="phi3",
            messages=messages
        )

        reply = response["message"]["content"]

        # Save AI reply
        chat_memory.append({
            "role": "assistant",
            "content": reply
        })

        return reply

    except Exception as e:
        return str(e)