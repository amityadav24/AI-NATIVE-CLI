# command_parser.py
import json
import subprocess
import os

def execute_command(ai_response):
    """
    Parses the AI's JSON response and executes the commanded action.
    """
    try:
        command_data = json.loads(ai_response)
        cmd_name = command_data['command']['name']
        params = command_data['command']['parameters']

        print(f"🤖 Executing command: {cmd_name}")

        if cmd_name == "run_shell_command":
            command_to_run = params['command']
            print(f"💻 Running shell command: {command_to_run}")
            # Run the command and capture output
            result = subprocess.run(command_to_run, shell=True, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                return {"status": "success", "output": result.stdout}
            else:
                return {"status": "error", "output": result.stderr}

        elif cmd_name == "write_file":
            file_path = params['file_path']
            content = params['content']
            print(f"📄 Writing to file: {file_path}")

            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(content)
            return {"status": "success", "output": f"File '{file_path}' successfully written."}

        elif cmd_name == "git_commit":
            message = params['message']
            print(f"🔨 Committing to git with message: '{message}'")

            # Step 1: git add all changes
            add_result = subprocess.run('git add .', shell=True, capture_output=True, text=True)
            if add_result.returncode != 0:
                return {"status": "error", "output": f"Git add failed: {add_result.stderr}"}

            # Step 2: git commit
            commit_result = subprocess.run(f'git commit -m "{message}"', shell=True, capture_output=True, text=True)
            if commit_result.returncode == 0:
                return {"status": "success", "output": commit_result.stdout}
            else:
                return {"status": "error", "output": commit_result.stderr}

        elif cmd_name == "no_op":
            return {"status": "success", "output": "No operation performed. (Request was a greeting or unclear.)"}

        else:
            return {"status": "error", "output": f"Unknown command: {cmd_name}"}

    except json.JSONDecodeError:
        return {"status": "error", "output": "AI did not return valid JSON. It might have provided an explanation instead of a command."}
    except KeyError as e:
        return {"status": "error", "output": f"AI response missing a key: {e}."}
    except subprocess.TimeoutExpired:
        return {"status": "error", "output": "Command timed out after 30 seconds."}
    except Exception as e:
        return {"status": "error", "output": f"An unexpected error occurred: {e}."}