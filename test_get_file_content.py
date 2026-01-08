from functions.get_files_content import get_file_content

def test_runs(working_directory, file_path):
    response = get_file_content(working_directory, file_path)
    print(response)

if __name__ == "__main__":
    test_runs("calculator", "main.py")
    test_runs("calculator", "pkg/calculator.py")
    test_runs("calculator", "/bin/cat")
    test_runs("calculator", "pkg/does_not_exist.py")
    