import subprocess
import sys

result = subprocess.run(["flake8", "."], capture_output=True, text=True)
if result.returncode != 0:
    print("Errores de estilo encontrados:", file=sys.stderr)
    print(result.stdout, file=sys.stderr)
sys.exit(result.returncode)
