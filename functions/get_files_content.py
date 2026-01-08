import os
from config import LIMIT

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False
        valid_target_path = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        print(f"Valid file path: {valid_target_path}")
        with open(target_file, "r") as f:
            content = f.read(LIMIT)
            # After reading the first MAX_CHARS...
            if f.read(1):
                content += f'[...File "{valid_target_path}" truncated at {LIMIT} characters]'
            return content
    except Exception as e:
        return f"Error: Exception encountered {e}"
