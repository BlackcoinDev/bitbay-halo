import ast
import os

modules = [
    "bci", "blocks", "composite", "deterministic", "main",
    "mnemonic", "ripemd", "segwit", "specials", "stealth", "transaction",
]

base_path = "pybitcointools"
all_exports = []
imports_code = []


def get_public_symbols(module_name):
    file_path = os.path.join(base_path, module_name + ".py")
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        tree = ast.parse(f.read())

    symbols = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if not node.name.startswith("_"):
                if module_name == "ripemd" and node.name == "is_python2":
                    continue
                symbols.append(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if not target.id.startswith("_"):
                        if module_name == "segwit" and target.id == "apply_multisignatures":
                            continue
                        symbols.append(target.id)
                elif isinstance(target, ast.Tuple):
                    for elt in target.elts:
                        if isinstance(elt, ast.Name) and not elt.id.startswith("_"):
                            symbols.append(elt.id)

    return sorted(list(set(symbols)))


for mod in modules:
    symbols = get_public_symbols(mod)
    if symbols:
        all_exports.extend(symbols)
        syms_str = ", ".join(symbols)
        if len(syms_str) > 80:
            imports_code.append(f"from .{mod} import (")
            chunk: list[str] = []
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
print("\n__all__ = (")
for s in sorted(list(set(all_exports))):
    print(f"    '{s}',")
print(")")
