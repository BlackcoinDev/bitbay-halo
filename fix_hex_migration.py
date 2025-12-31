import re


def fix_line(line):
    # Handle .encode('hex')
    # search for .encode('hex')
    # if found, look backwards to find the start of the expression
    # wrap in safe_hexlify(...)

    # Simple state machine to find start of expression
    # match ending at .encode('hex')

    while ".encode('hex')" in line:
        idx = line.find(".encode('hex')")
        # scan backwards from idx-1
        # count parens, brackets, braces
        # stop when balanced and at a separator or existing start

        balance_paren = 0
        balance_brack = 0
        balance_brace = 0

        start_idx = idx - 1

        # skip potential whitespace? No, usually directly attached.

        for i in range(idx - 1, -1, -1):
            char = line[i]
            if char == ")":
                balance_paren += 1
            elif char == "(":
                balance_paren -= 1
            elif char == "]":
                balance_brack += 1
            elif char == "[":
                balance_brack -= 1
            elif char == "}":
                balance_brace += 1
            elif char == "{":
                balance_brace -= 1

            # If balanced and we hit a separator
            if balance_paren == 0 and balance_brack == 0 and balance_brace == 0:
                # Check if char is separator
                if char in " ,=:[{(":
                    # The expression starts at i+1
                    start_idx = i + 1
                    break
                if i == 0:
                    start_idx = 0
                    break

        # Extract expr
        expr = line[start_idx:idx]

        # Replace
        # new_expr = "safe_hexlify(" + expr + ")"
        # splice line
        line = line[:start_idx] + "safe_hexlify(" + expr + ")" + line[idx + 14 :]

    # Handle .decode('hex')
    while ".decode('hex')" in line:
        idx = line.find(".decode('hex')")
        balance_paren = 0
        balance_brack = 0
        balance_brace = 0
        start_idx = idx - 1
        for i in range(idx - 1, -1, -1):
            char = line[i]
            if char == ")":
                balance_paren += 1
            elif char == "(":
                balance_paren -= 1
            elif char == "]":
                balance_brack += 1
            elif char == "[":
                balance_brack -= 1
            elif char == "}":
                balance_brace += 1
            elif char == "{":
                balance_brace -= 1
            if balance_paren == 0 and balance_brack == 0 and balance_brace == 0:
                if char in " ,=:[{(":
                    start_idx = i + 1
                    break
                if i == 0:
                    start_idx = 0
                    break
        expr = line[start_idx:idx]
        line = line[:start_idx] + "safe_unhexlify(" + expr + ")" + line[idx + 14 :]

    return line


with open("Halo.py", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(fix_line(line))

with open("Halo.py", "w") as f:
    f.writelines(new_lines)
