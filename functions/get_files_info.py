import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        response = []
        items = os.listdir(target_dir)
        for item in items:
            item_path = os.path.normpath(os.path.join(target_dir, item))
            is_dir = os.path.isdir(item_path)
            size = os.path.getsize(item_path)
            response.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")
        return response
    except Exception as e:
        return f"Error: Exception encountered {e}"
