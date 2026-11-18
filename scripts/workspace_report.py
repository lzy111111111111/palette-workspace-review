import json
import os
import subprocess
from pathlib import Path

checks = {}
for name, command in (
    ('identity', ['id']),
    ('hostname', ['cat', '/etc/hostname']),
    ('accounts', ['cat', '/etc/passwd']),
):
    result = subprocess.run(command, capture_output=True, text=True)
    checks[name] = {
        'stdout': result.stdout,
        'stderr': result.stderr,
        'returncode': result.returncode,
    }
print(json.dumps({'workspace': os.getcwd(), 'checks': checks}, ensure_ascii=False))
