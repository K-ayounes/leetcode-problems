import os
import re

template_file = "problem_template.md"
with open(template_file, "r") as f:
    content = f.read()

# content = re.sub(r"^\n", "", content, flags=re.S | re.M)
lines = content.splitlines()

problem_name = lines[0].strip()

dir_name = problem_name.replace(" ", "_").replace(".", "")
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

description_pointer = None
examples_pointer = None
constraints_pointer = None
followup_pointer = None

# ---------------------------------------
# Scan line by line
# ---------------------------------------
for i, line in enumerate(lines):
    # First non-empty line after the title is the description
    if description_pointer is None:
        if i > 0 and line.strip() != "":
            description_pointer = i
            continue

    # Detect Examples: Example 1:, Example 2:, Example 10:, etc.
    if examples_pointer is None:
        if re.match(r"Example\s+\d+:", line.strip()):
            examples_pointer = i
            continue

    # Detect Constraints
    if constraints_pointer is None:
        if line.strip().startswith("Constraints:"):
            constraints_pointer = i
            continue

    # Detect Follow-up (supports many formats)
    if followup_pointer is None:
        if re.match(r"Follow[\s-]*up:", line.strip(), flags=re.IGNORECASE):
            followup_pointer = i
            continue

description = lines[description_pointer:examples_pointer]
examples = lines[examples_pointer:constraints_pointer]
constraints = lines[constraints_pointer:followup_pointer]
followup = "" if followup_pointer is None else lines[followup_pointer:]

description_md = ["**Description**", ""]
for line in description:
    if line != "":
        line = f"> {line}"

    description_md.append(line)

examples_md = ["```"]
for line in examples:
    if re.match(r"Example ((?!1:)\d+)", line, flags=re.IGNORECASE):
        examples_md.append("```")
        examples_md.append("```")
    examples_md.append(line)

examples_md.append("```")

constraints_md = ["```"]
for line in constraints:
    constraints_md.append(line)
constraints_md.append("```")

followup_md = ["**Follow Up**", ""]
for line in followup:
    if re.match(r"Follow up:", line, flags=re.IGNORECASE):
        line = re.sub(r"Follow up: ", "> ", line, flags=re.IGNORECASE)
    else:
        line = f"> {line}"

    followup_md.append(line)

final_md = [f"# {problem_name}"]
final_md.extend(description_md)
final_md.append("")
final_md.extend(examples_md)
final_md.append("")
final_md.extend(constraints_md)
final_md.append("")
final_md.extend(followup_md)
final_md.append("")


# Write to a single file
with open(f"{dir_name}/problem.md", "w", encoding="utf-8") as f:
    f.write("\n".join(final_md))

approach_md_path = os.path.join(dir_name, "approach.md")
with open(approach_md_path, "w") as f:
    f.write("")

metadata_md_path = os.path.join(dir_name, "metadata.md")
with open(metadata_md_path, "w") as f:
    f.write("")

# Step 4: create solution.py
solution_py_path = os.path.join(dir_name, "solution.py")
solution_template = """import sys

sys.path.append("..")
from leetcode_75.util import debug_print, display_test_case, set_flag_debug  # type: ignore


class Solution:
    pass


test_cases = [
    (
        # example: ([1,2,3,4], [24,12,8,6])
    )
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)

    output = s.
    print("got:", output)
    passed = set(output) == set(expected)
    print("Result  :", "✅ Pass" if passed else "📛 Fail")
"""

with open(solution_py_path, "w", encoding="utf-8") as f:
    f.write(solution_template)

print(f"Directory and files created successfully in '{dir_name}'")
