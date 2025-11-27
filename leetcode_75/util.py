from multiprocessing import Value


def display_test_case(test_case, expected, index):
    print(
        f"""
{f"# {index}" if index else ""}
Test Case: {test_case}
Expected: {expected}
""",
        end="",
    )


DEBUG = False


def set_flag_debug(value):
    global DEBUG
    DEBUG = value


def debug_print(*args):
    if DEBUG:
        print(*args)
