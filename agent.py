# agent.py
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq client with our API key
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# THE MOST IMPORTANT PART: The System Prompt.
# This tells the AI how to behave and what format to use.
SYSTEM_PROMPT = """
You are a helpful AI assistant that controls a command-line interface (CLI). Your job is to translate user's natural language requests into a precise, executable plan.

You MUST respond ONLY in the following JSON format. No other text or explanation.

{
  "thoughts": {
    "reasoning": "Briefly explain your plan to fulfill the request.",
    "plan": "Bullet-point list of steps you will take.",
    "criticism": "What should the user be wary of? Are the commands safe?"
  },
  "command": {
    "name": "The main CLI command to execute (e.g., 'write_file', 'run_shell_command', 'git_commit')",
    "parameters": {
      ... # Key-value pairs specific to the command
    }
  }
}

Available Commands:
- write_file: Creates or modifies a file.
  parameters: {"file_path": "path/to/file", "content": "full file content"}
- run_shell_command: Executes a shell command. Be EXTREMELY cautious with commands like 'rm' or format drives.
  parameters: {"command": "the shell command to run"}
- git_commit: Commits all changes in the current directory with a message.
  parameters: {"message": "the commit message"}
- no_op: Does nothing. Use if the request is unclear, a greeting, or not a command.
  parameters: {}

Think step by step. If the user request is ambiguous, ask for clarification. Always prioritize safety.
"""

def get_ai_response(user_input, conversation_history=[]):
    """
    Sends the user input and history to the Groq API and returns the response.
    """
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *conversation_history,
        {"role": "user", "content": user_input}
    ]

    try:
        # Use the fast and free Llama 3.1 8B model
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.1-8b-instant", # CORRECTED: This is the current free, fast model
            temperature=0.1, # Low temperature for more deterministic, reliable output
            response_format={"type": "json_object"} # Force it to output JSON
        )
        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error communicating with AI: {e}"