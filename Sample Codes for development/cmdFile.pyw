import subprocess

def run_cmd(cmd_str):
    try:
        # Define the command you want to run
        command = cmd_str

        # Run the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Print the output of the command
        # print("Output:", result.stdout)
        # print("Error:", result.stderr)
    except Exception as e:
        print("cmdFile-run_cmd"e)

run_cmd("echo Hello, World!")