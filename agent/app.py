import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type "exit" to quit or "reset" to clear the conversation)')

    system_message = """
You are Hadi, a Year 2 Computer Science student.

Your job is to help students understand computer science concepts, debug code, and improve their programming skills.

Rules:
- Always explain concepts clearly and simply.
- Always encourage the user to learn instead of just giving the answer.
- Never answer questions that are unrelated to computer science or programming. If the user asks something outside your role, politely explain that you only help with CS-related topics.

Response format:
- Start with a one-sentence summary of what the user asked.
- Then provide a clear explanation or solution.
- End with one follow-up question that helps continue the conversation.
"""

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

        # Print the conversation history
        print("History:", history)

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        # Print the full API response
        print(response)

        reply = response.content[0].text
        print(f'Claude: {reply}')

        history.append({'role': 'assistant', 'content': reply})

run_chat()

#1 · Personal Analogy

#For me, the invisible thing is my religion. As an Armenian, Christianity is part of how I was raised, and even though people can't see it, it influences my decisions and how I treat others. It's always there in the background, just like the system prompt guides the AI without the user seeing it.

#2 · If I Deleted This Line

#system=system_message – I thought the AI would stop acting like Hadi, and it did. It became a regular chatbot instead of following the role I gave it.
#The "Never answer unrelated questions" rule – I predicted it would answer any question, and it did because there was no longer anything limiting it.
#The response format instruction – Without it, the replies became less organized and stopped following the structure I wanted.

#3 · Bug Diary

#I got the error command 'python.execInTerminal-icon' not found. At first I thought my code was broken, but it turned out to be an issue with VS Code, not my program.

#Bonus

#My analogy still makes sense. I'd just say that a system prompt is like the values from my religion—it quietly guides my actions even though other people can't see it.