import ollama
import subprocess
import os

while True:
    # Displays the cwd
    cwd = os.getcwd()
    user_input = input(cwd + ">")

    messages = [
        {"role": "system", "content": "You are an AI assistant that converts user requests into a single, correct Windows Terminal command. Only respond with the command, no explanations. If unsure or ambiguous, ask the user for clarification. Commands must be safe and valid for Windows PowerShell or Command Prompt."},
        {"role": "user", "content": user_input}
    ]

    response = ollama.chat(model='gemma3', messages=messages)
    print(response['message']['content'])

    command = response['message']['content']

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    print("Output:", result.stdout)
    print("Error:", result.stderr)