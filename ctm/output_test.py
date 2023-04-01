def content_filter(filepath):
    new_file = open(filepath, "r")
    contents = new_file.readlines()
    filtered = [i.replace("\n", "") for i in contents]
    return filtered


def output_tester(output_files):
    for counter, i in enumerate(output_files):
        test_output = "temp/test_outputs/output" + str(counter + 1)
        user_output = "temp/user_outputs/user_output" + str(counter + 1)

        test_output = content_filter(test_output)
        user_output = content_filter(user_output)

        if test_output[0] != user_output[0]:
            return False
    return True
