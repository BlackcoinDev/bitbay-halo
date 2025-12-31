
import sys
import tokenize
from io import BytesIO

def fix_line(line):
    # Check if line has #
    if '#' not in line:
        return line

    # Use generator to handle TokenError
    g = tokenize.tokenize(BytesIO(line.encode('utf-8')).readline)
    tokens = []
    comment_start = -1
    
    try:
        for tok in g:
            tokens.append(tok)
            if tok.type == tokenize.COMMENT:
                comment_start = tok.start[1]
                break
    except tokenize.TokenError:
        pass

    if comment_start == -1:
        return line 

    code_part = line[:comment_start]
    comment_part = line[comment_start:]

    # Count parens in code_part
    open_p = code_part.count('(')
    close_p = code_part.count(')')
    
    if open_p > close_p:
        # Code needs closing paren
        new_comment = comment_part.rstrip()
        if new_comment.endswith(')'):
             new_comment = new_comment[:-1]
             return code_part + ")" + new_comment + "\n"
    
    elif close_p > open_p:
        # Code has extra closing paren?
        # Check if code ends with )
        stripped_code = code_part.rstrip()
        if stripped_code.endswith(')'):
            # Move ) to comment (or just remove from code if comment has ) at end?)
            # Actually Global fix put ) at end of line.
            # So comment likely ends with ).
            # If we remove ) from code, we should check if we need to put it somewhere.
            # If original comment matched ) in code? No, sed issues.
            # Assume extra ) belongs to comment or is duplicate.
            # Just removing it from code makes code balanced.
            # And we can append ) to comment if not there? 
            # Or just ensure it is in comment.
            # Safer to just move it to comment start.
            
            new_code = stripped_code[:-1]
            # preserve whitespace between code and #?
            # code_part includes trailing spaces before #
            # split spaces
            trailing_spaces = code_part[len(stripped_code):]
            
            # Result: new_code + spaces + ) + comment
            # This puts ) effectively into comment (before #? No, )#)
            # Wait. If we make it )#, it is Code ) #.
            # We want to put it AFTER #.
            # Or just append to line end?
            
            return new_code + trailing_spaces + "#" + ")" + comment_part[1:]
            
    return line

with open("Halo.py", "r") as f:
    lines = f.readlines()

new_lines = [fix_line(l) for l in lines]

with open("Halo.py", "w") as f:
    f.writelines(new_lines)
