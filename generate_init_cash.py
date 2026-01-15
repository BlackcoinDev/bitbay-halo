import ast
import os

modules = [
    "bci", "blocks", "composite", "deterministic", "main", 
    "mnemonic", "segwit", "stealth", "transaction"
]

base_path = "pybitcoincashtools"
all_exports = []
imports_code = []

def get_public_symbols(module_name):
    file_path = os.path.join(base_path, module_name + ".py")
    with open(file_path, "r") as f:
        tree = ast.parse(f.read())
    
    symbols = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if not node.name.startswith("_"):
                symbols.append(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if not target.id.startswith("_"):
                        # Heuristic: uppercase for constants, or check usage. 
                        # simpler to just include all top level assignments that aren't _ private
                        symbols.append(target.id)
                elif isinstance(target, ast.Tuple):
                     for elt in target.elts:
                        if isinstance(elt, ast.Name) and not elt.id.startswith("_"):
                            symbols.append(elt.id)

    return sorted(list(set(symbols)))

for mod in modules:
    symbols = get_public_symbols(mod)
    if symbols:
        # Check against main.py which seems to be the core.
        # If symbols are redundant (e.g. main has everything), we should be careful.
        # But for __init__.py replacement of *, we traditionally import * from all.
        # So we should import all found public symbols.
        
        # Filtering: imports inside files shouldn't be re-exported unless they are in __all__
        # But since we are parsing, we only picking defs and assigns. 
        # Wait, if `main.py` imports `hashlib`, we don't want to export `hashlib`.
        # My AST logic above only picks FunctionDef, ClassDef, Assign. It ignores Import/ImportFrom.
        # So it should be safe.
        
        # Exception: main.py has `string_types = ...` which is an assignment.
        
        all_exports.extend(symbols)
        # formatted import
        # break into lines if too long
        syms_str = ", ".join(symbols)
        if len(syms_str) > 80:
             imports_code.append(f"from .{mod} import (")
             # chunk it
             chunk = []
             current_len = 0
             for s in symbols:
                 if current_len + len(s) + 2 > 70:
                     imports_code.append("    " + ", ".join(chunk) + ",")
                     chunk = [s]
                     current_len = len(s)
                 else:
                     chunk.append(s)
                     current_len += len(s) + 2
             if chunk:
                 imports_code.append("    " + ", ".join(chunk) + ",")
             imports_code.append(")")
        else:
            imports_code.append(f"from .{mod} import {syms_str}")

print("\n".join(imports_code))
print("\n__all__ = [")
for s in sorted(list(set(all_exports))):
    print(f'    "{s}",')
print("]")
