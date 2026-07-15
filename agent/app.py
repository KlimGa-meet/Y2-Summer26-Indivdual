import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type "exit" to quit or "reset" to clear the conversation)')
    system_message = (
        "Your name is Alex. You are a helpful and friendly assistant who "
        "helps students learn about technology and computer science. "
        "You explain things clearly and always encourage curiosity."
    )
    history = []

    while True:
        turn = len(history) // 2 + 1
        user_input = input(f'[Turn {turn}] You: ')

        if user_input.lower() == 'exit':
            break

        if user_input.lower() == 'reset':
            history.clear()
            print("Conversation history cleared. Starting a new conversation.")
            continue

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')

        history.append({'role': 'assistant', 'content': reply})

run_chat()


#1 · Personal Analogy — Conversation Memory
#To me, it's like running a business. Every time I start working on a new idea or opportunity, I have to bring all of my skills, experience, creativity, and knowledge with me. If I showed up without those things, I wouldn't be the same entrepreneur, just like an AI without the conversation history wouldn't know what was discussed before. Unlike carrying a physical object, I carry my abilities and everything I've learned wherever I go.
#2 · If I Deleted This Line
#history.append({'role': 'assistant', 'content': reply})
#I predicted that the AI would stop remembering its own responses, and that's exactly what happened. It could still see what I said, but it forgot what it had previously replied, making the conversation less consistent.
#load_dotenv()
#I predicted the program would start but fail when trying to use the API key. That was correct because without loading the .env file, the environment variables—including the API key—aren't available.
#break inside if user_input.lower() == 'exit':
#I predicted that typing "exit" would no longer quit the program. Instead, it would keep looping and continue asking for more input because nothing tells the loop to stop.
#3 · Bug Diary
#The biggest issue I ran into today was that my API key wasn't working, and before figuring it out I also couldn't get pip to work even though it seemed to work for everyone else. At first, I thought there was something wrong with the API itself, but the real problems were with my local setup and configuration. The gap between my first guess and the actual issue showed me that errors often come from the environment or installation, not necessarily from the code I'm writing.

