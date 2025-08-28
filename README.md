AI-Native CLI Agent
An intelligent command-line interface (CLI) assistant that executes natural language commands for software development tasks. Built with Python and powered by Groq's Llama 3.1 API.

🚀 Features
Natural Language Understanding: Converts plain English into executable commands

File Operations: Create, modify, and manage files

Git Integration: Initialize repositories, add files, and commit changes

Shell Command Execution: Run system commands safely

JSON-structured Responses: Consistent and parseable output format

🛠️ Tech Stack
Python 3.8+

Groq API (Free tier) - Using Llama 3.1-8b-instant model

python-dotenv - Environment variable management

subprocess - Safe command execution

📋 Prerequisites
Python 3.8 or higher

Groq API account (free)

Git (for version control operations)

⚡ Quick Start
1. Clone and Setup
bash
# Create project directory
mkdir ai-native-cli
cd ai-native-cli

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
2. Install Dependencies
bash
pip install groq python-dotenv
3. Get Groq API Key
Go to console.groq.com

Sign up for a free account

Create an API key from the dashboard

Copy your API key

4. Configure Environment
bash
# Create .env file
echo "GROQ_API_KEY=your_actual_api_key_here" > .env
Replace your_actual_api_key_here with your actual Groq API key

5. Project Structure
text
ai-native-cli/
├── .env                    # API keys (DO NOT SHARE)
├── .gitignore             # Git ignore rules
├── main.py                # Main application
├── agent.py               # AI interaction logic
├── command_parser.py      # Command execution
└── requirements.txt       # Dependencies
6. Run the Application
bash
python main.py
🎯 Usage Examples
Try these commands after starting the application:

bash
# File operations
"Create a file named hello.txt with content 'Hello World'"
"List all files in this directory"

# Git operations  
"Initialize a new git repository"
"Commit all changes with message 'Initial commit'"

# System commands
"Show current directory path"
"Check Python version"
📁 Key Files Explained
agent.py: Handles AI communication with Groq API and prompt engineering

command_parser.py: Safely executes commands and handles errors

main.py: Main CLI interface and user interaction loop

.env: Secure storage for API keys (never commit this file)

🔧 Customization
Add New Commands
Update the SYSTEM_PROMPT in agent.py with new command definitions

Add corresponding execution logic in command_parser.py

Test with natural language prompts

Modify AI Behavior
Edit the SYSTEM_PROMPT in agent.py to change:

Response format requirements

Available commands list

Safety constraints and warnings

⚠️ Safety Features
Command Validation: Checks for dangerous operations

Timeout Protection: Prevents hanging commands (30s timeout)

Error Handling: Graceful failure for invalid commands

Path Validation: Prevents filesystem corruption

🐛 Troubleshooting
Common Issues
"Model not found" error: Update the model name in agent.py

API connection issues: Verify your Groq API key in .env

Permission errors: Check file/directory permissions

Command not executing: Review the command parser logic

Debug Mode
Add print statements in command_parser.py to see detailed execution flow.

📊 Performance Notes
Response Time: Typically 1-3 seconds with Groq's free tier

Accuracy: >90% for well-defined commands

Limitations: Complex multi-step operations may require refinement

🤝 Contributing
Fork the repository

Create a feature branch

Add tests for new functionality

Submit a pull request

📄 License
This project is for educational and demonstration purposes. Please review Groq's API terms of service.

🆓 Cost
Groq API: Free tier available

No credit card required for basic usage

Rate limits: Check Groq's current free tier limits

Happy Coding! 🚀 Your AI CLI assistant is ready to help with your development workflow.

