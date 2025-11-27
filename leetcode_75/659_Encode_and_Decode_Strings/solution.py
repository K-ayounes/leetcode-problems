import sys

sys.path.append("..")
from leetcode_75.util import (  # type: ignore
    debug_print,
    display_test_case,
    set_flag_debug,
)


class Solution:
    def encode(self, strs):
        encoded = ["#"]

        for string in strs:
            encoded.append(f"{len(string)}#")
            encoded.append(string)

        return "".join(encoded)

    def decode(self, encoded_string):
        strings = []
        size = 0
        size_str = ""
        delim = encoded_string[0]

        pointer = 1
        end = len(encoded_string)
        read = True  # True = reading size, False = reading string

        while pointer != end:
            debug_print(
                f"\n\n{' ' * (pointer)}{'V'}{' ' * (end - pointer + 10)}({pointer})"
            )
            debug_print(encoded_string)
            read_data = encoded_string[pointer]

            if read:
                if read_data != delim:
                    debug_print(
                        f"\t|reading data into size_str: '{size_str}' << {read_data}"
                    )
                    size_str += read_data
                else:
                    read = False
                    size = int(size_str)
                    size_str = ""
                    debug_print(f"\t|delimiter hit: writing size_str to size: {size=}")
                    debug_print("\t|reading state: False, flushing size_str: ''")

                pointer += 1
                debug_print(f"\t|moving pointer to {pointer}")
            else:
                debug_print(
                    f"\t|reading string of size {size} - string read: {encoded_string[pointer : pointer + size]}"
                )
                strings.append(encoded_string[pointer : pointer + size])
                pointer += size
                size = 0
                read = True
                debug_print(f"\t|moving pointer to {pointer}")
                debug_print("\t|read state: True, resetting size to 0")

        return strings


test_cases = [
    (
        ["#" * 10, "code", "lo#ve", "you"],
        ["#" * 10, "code", "lo#ve", "you"],
    )
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)

    encoded_output = s.encode(test_case)
    print("encoded_output:", encoded_output)
    decoded_output = s.decode(encoded_output)

    print("got:", decoded_output)
    passed = set(decoded_output) == set(expected)
    print("Result  :", "✅ Pass" if passed else "❌ Fail")
