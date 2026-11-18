import json

print(json.dumps({
    'palette': ['muted sage', 'warm amber', 'soft gray'],
    'composition': 'subject on the lower-left third',
}, ensure_ascii=False))
