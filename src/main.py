import sys
from gpt_api import BotHandler
from executor import CommandExecutor
import os
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <prompt>")
        sys.exit(1)
    prompt = " ".join(sys.argv[1:])
    bot_handler = BotHandler()
    #fetch systemprompt from config/gpt_prompt.txt
    promptpath = os.path.join(os.path.dirname(__file__), '../config/gpt_prompt.txt')
    with open(promptpath,"r") as f:
        systemprompt = f.read()
    bot = bot_handler.create_bot(systemprompt)

    current_dir = os.getcwd()
    dir_contents = os.listdir(current_dir)
    dir_listing = "\n".join(dir_contents)

    # Generate a formatted message for the bot with working directory context
    assistant_info = f"""You are currently in the following directory:
    Path: {current_dir}
    Contents:
    {dir_listing}
    """
    messageaddition = [{"role": "assistant", "content": assistant_info},{"role": "user", "content": prompt}]
    messages = bot.getmessageheader() + messageaddition
    print(f"Generating commands for the prompt: {prompt}")
    try:
        commands_output = bot.promptgpt(messages)
    except Exception as e:
        print(f"Error generating commands: {e}")
        sys.exit(1)
    commands = [cmd.strip() for cmd in commands_output.split("|||") if cmd.strip()]

    print("\nGenerated Commands:")
    for i, cmd in enumerate(commands, start=1):
        print(f"{i}. {cmd}")

    # Confirm and execute the commands
    print("\nStarting execution...")
    executor = CommandExecutor(commands)
    executor.execute()

if __name__ == "__main__":
    main()