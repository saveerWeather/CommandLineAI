import subprocess

class CommandExecutor:
    def __init__(self,commands):
        self.commands = commands
    def execute(self):
        for i,command in enumerate(self.commands):
            confirmation = input(f"Execute command {i+1}/{len(self.commands)}: {command}, y/n/skip: ")
            if confirmation.lower() == 'y':
                self._run_command(command)
                
            elif confirmation.lower()=='skip':
                print(f"Skipping")
            else:
                print("Stopping all commands")
                break
    def _run_command(self,command):
        try:
            print(f"\nExecuting: {command}")
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print(f"Output:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e.stderr}")
"""
Usage: 
if __name__ == "__main__":
    commands = [
        "echo 'Hello, World!'",
        "ls -l",
        "invalid_command"  
    ]
    executor = CommandExecutor(commands)
    executor.execute()
"""