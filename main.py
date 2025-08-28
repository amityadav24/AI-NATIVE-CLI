# main.py
from agent import get_ai_response
from command_parser import execute_command
import json

def main():
    print("""
    🤖 Welcome to the AI-Native CLI Agent (Free Edition!)
    ------------------------------------------------------
    I can help you create files, run commands, and manage git.
    Example: "Create a text file called hello.txt with the message 'Hello, World!'"
    Type 'exit' or 'quit' to end the session.
    ------------------------------------------------------
    """)

    # This list keeps track of the conversation for context
    conversation_history = []

    while True:
        user_input = input("You: ").strip()

        # Check if the user wants to exit
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye! 👋")
            break

        if not user_input:
            continue

        # Step 1: Get the AI's plan
        print("AI is thinking...")
        ai_json_response = get_ai_response(user_input, conversation_history)

        # Add this interaction to history for context
        conversation_history.append({"role": "user", "content": user_input})
        # We add the raw JSON to history to keep the context clean for the AI
        conversation_history.append({"role": "assistant", "content": ai_json_response})

        # Step 2: Parse and print the AI's thoughts for the user to see
        try:
            ai_response_parsed = json.loads(ai_json_response)
            print(f"\n💭 Reasoning: {ai_response_parsed['thoughts']['reasoning']}")
            # print(f"📋 Plan: {ai_response_parsed['thoughts']['plan']}") # Optional: can be verbose
            print(f"⚠️  Criticism: {ai_response_parsed['thoughts']['criticism']}")
        except json.JSONDecodeError:
            # If the AI didn't return JSON, just show the raw response (usually an error message)
            print(f"\n❌ AI Response (Raw): {ai_json_response}")
            continue

        # Step 3: Execute the command from the AI
        execution_result = execute_command(ai_json_response)

        # Step 4: Show the user the result
        print(f"\n🔄 Status: {execution_result['status'].upper()}")
        print(f"📤 Output: {execution_result['output']}")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    main()