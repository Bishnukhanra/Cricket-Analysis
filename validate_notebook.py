import nbformat
from IPython.display import display

path = "Analyze_Cricket.ipynb"
nb = nbformat.read(path, as_version=4)
ns = {"display": display}

for i, cell in enumerate(nb.cells):
    if cell.cell_type != "code":
        continue
    try:
        exec(compile(cell.source, f"{path}:cell-{i+1}", "exec"), ns)
    except Exception as exc:
        print(f"FAIL cell {i+1}: {type(exc).__name__}: {exc}")
        raise

print("EXECUTED_OK")
