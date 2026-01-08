from functions.run_python_file import run_python_file

def test_runs(working_directory, file_path, *args):
    response = run_python_file(working_directory,file_path, *args)
    print(response)

if __name__ == "__main__":
    test_runs("calculator", "main.py")
    test_runs("calculator", "main.py", ["3 + 5"])
    test_runs("calculator", "tests.py")
    test_runs("calculator", "../main.py")
    test_runs("calculator", "nonexistent.py")
    test_runs("calculator", "lorem.txt")