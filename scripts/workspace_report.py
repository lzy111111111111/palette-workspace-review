import json
import os

print(json.dumps({
    'workspace': os.getcwd(),
    'palette': ['muted sage', 'warm amber', 'soft gray'],
    'composition': 'subject on the lower-left third',
}, ensure_ascii=False))
