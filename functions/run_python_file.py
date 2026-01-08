import os,subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False
        valid_target_path = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        # Building the command to run
        command = ["python", target_file]
        if args:
            command.extend(args)
        process_response = subprocess.run(command,capture_output=True,text=True,timeout=30)
        if process_response.returncode != 0:
            return f"Process exited with code {process_response.returncode}"
        if len(process_response.stdout) == 0 and len(process_response.stderr) == 0:
            return f"No output produced"
        return f"STDOUT: {process_response.stdout} \nSTDERR: {process_response.stderr}"
    except Exception as e:
        return f"Error: executing Python file: {e}"
