from functions.write_file import write_file

def test_runs(working_directory, file_path, content):
    response = write_file(working_directory,file_path,content)
    print(response)

if __name__ == "__main__":
    test_runs("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    test_runs("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    test_runs("calculator", "/tmp/temp.txt", "this should not be allowed")