import ollama
import subprocess
import os

while True:
    # Displays the cwd
    cwd = os.getcwd()
    user_input = input(cwd + ">")

    messages = [
        {"role": "system", "content": "You are an ai in the windows command prompt, assist the user by responding and or using the appropriate command prompt. To use a command prompt put it square brackets. When more information is needed, use command prompts to find it or ask the user. You must never open command prompt for the user, only you can run commands in command prompt."},
        {"role": "user", "content": user_input}
    ]

    response = ollama.chat(model='gemma3', messages=messages)
    response = response['message']['content']
    print(response)

    try:
        start = response.index('[')
        end = response.index(']')
        command = response[start + 1:end]
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    except ValueError:
        pass
