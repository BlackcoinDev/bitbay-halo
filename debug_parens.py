import sys
import tokenize
from io import BytesIO


def check_line(line_num, line):
    if 'f.write("server=1' not in line and line_num != 831:
        return

    print(f"Checking line {line_num}: {line.strip()}")
    if not line.strip().endswith(")") or "#" not in line:
        print("Skipped: No ) at end or no #")
        return

    try:
        tokens = list(tokenize.tokenize(BytesIO(line.encode("utf-8")).readline))
        print("Tokens found:", [(t.type, t.string) for t in tokens])
    except tokenize.TokenError as e:
        print(f"TokenError: {e}")
        return

    comment_start = -1
    for tok in tokens:
        if tok.type == tokenize.COMMENT:
            comment_start = tok.start[1]
            break

    if comment_start == -1:
        print("No comment token found")
        return

    code_part = line[:comment_start]
    comment_part = line[comment_start:]
    print(f"Code: '{code_part}'")
    print(f"Comment: '{comment_part}'")

    if not comment_part.rstrip().endswith(")"):
        print("Comment does not end with )")
        return

    open_p = code_part.count("(")
    close_p = code_part.count(")")
    print(f"Open: {open_p}, Close: {close_p}")

    if open_p > close_p:
        print("Would fix!")
    else:
        print("Balanced, no fix.")


with open("Halo.py", "r") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    check_line(i + 1, l)
