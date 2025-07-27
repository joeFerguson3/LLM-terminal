import ollama
import subprocess
import os

messages = [
    {"role": "system", "content": "You are an ai in the windows command prompt, assist the user by responding and or using"
    " the appropriate command prompt. To use a command prompt put it square brackets, only use square brackets for a valid "
    "and safe command prompt. You must never open command prompt for the user, only you can run commands in command prompt."
    " Keep responses concise. If unsure about anything ask the user."},
]

while True:
    # Displays the cwd
    cwd = os.getcwd()
    
    # Saves user response
    user_input = input(cwd + ">")
    messages.append({"role": "user", "content": user_input})

    # Generates ai response
    response = ollama.chat(model='gemma3', messages=messages)
    response = response['message']['content']
    messages.append({"role": "assistant", "content": response}) # Saves ai response
    print(response)

    try:
        # Runs command prompt
        start = response.index('[')
        end = response.index(']')
        command = response[start + 1:end]
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # Allows ai to see command prompt
        messages.append({"role": "user", "content": "this is the result of the command prompt: " + result.stdout + " " + result.stderr})
        print(result.stdout)
        print(result.stderr)
   
    except ValueError:
        pass
