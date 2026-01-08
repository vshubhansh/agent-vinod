from functions.get_files_info import get_files_info

def test_runs(working, directory):
    response = get_files_info(working, directory)
    dir_string = "current" if directory == '.' else f"'{directory}'"
    print(f"Result for {dir_string} directory:")
    if isinstance(response, str):
        print(f"    {response}")
    else:
        for item in response:
            print(f"    {item}")

if __name__ == "__main__":
    test_runs("calculator", ".")
    test_runs("calculator", "pkg")
    test_runs("calculator", "/bin")
    test_runs("calculator", "../")
