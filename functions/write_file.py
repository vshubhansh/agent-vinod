import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False
        valid_target_path = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        print(f"Target file {target_file}")
        dir_tree = os.path.dirname(target_file)
        print(f"Directory tree {dir_tree}")
        os.makedirs(dir_tree, exist_ok=True)
        with open(target_file, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: Exception encountered {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the provided content into the file present at the file_path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to write the content, relative to the working directory. Creates the directory path relative to working directory if does not exist already.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the file provided in file path."
            )
        },
        required=["file_path","content"]
    ),
)