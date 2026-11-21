#!/usr/bin/env python3
"""Build static posts-data.js from Pages CMS JSON files (stdlib only)."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
posts=[]
for kind in ('news','blog'):
 for path in sorted((root/'content'/kind).glob('*.json')):
  try: obj=json.loads(path.read_text(encoding='utf-8'))
  except (json.JSONDecodeError,UnicodeError) as exc:
   raise SystemExit(f'Invalid content file {path}: {exc}')
  if not isinstance(obj,dict): raise SystemExit(f'Expected JSON object in {path}')
  obj={k:obj.get(k) for k in ('title','date','summary','cover','published','body')}
  obj.update(type=kind,id=f'{kind}-{path.stem}')
  if not isinstance(obj['published'],bool):obj['published']=False
  posts.append(obj)
(root/'posts-data.js').write_text('window.KAMASTA_POSTS = '+json.dumps(posts,ensure_ascii=False).replace('<', chr(92)+'u003c').replace('>', chr(92)+'u003e')+';\n',encoding='utf-8')
print(f'Built {len(posts)} posts')
