import json


def test_case_creator(test_file):
    # Loads the test files from github
    tests = open(test_file, "r").read()
    tests = json.loads(tests)
    test_files = []
    for counter, test in enumerate(tests):
        file_name = "temp/test_inputs/input" + str(counter + 1)
        new_file = open(file_name, "w")
        for num in tests[test]["input"]:
            new_file.write(str(num) + "\n")
        test_files.append(file_name)
        new_file.close()
    output_files = []
    for counter, test in enumerate(tests):
        file_name = "temp/test_outputs/output" + str(counter + 1)
        new_file = open(file_name, "w")
        for num in tests[test]["output"]:
            new_file.write(str(num) + "\n")
        output_files.append(file_name)
        new_file.close()
    return test_files, output_files
