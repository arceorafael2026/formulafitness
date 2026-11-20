#!/usr/bin/env python3
"""Launch gate: lists every highlighted TODO placeholder and dev-stage item still in public/. Exit code 1 while any remain.
Usage: python3 tools/check-placeholders.py"""
import os, re, sys
root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")
issues = []
for dp, _, fs in os.walk(root):
    for f in fs:
        if not f.endswith((".html", ".js", ".css")):
            continue
        p = os.path.join(dp, f)
        t = open(p, encoding="utf-8").read()
        for m in re.finditer(r'<span class="todo">(.*?)</span>', t):
            issues.append((os.path.relpath(p, root), "placeholder: " + m.group(1)))
        if 'content="noindex' in t and 'booking-confirmed' not in p:  # the confirmation page stays noindex permanently
            issues.append((os.path.relpath(p, root), "noindex tag present (remove at launch)"))
        if "TODO at launch" in t:
            issues.append((os.path.relpath(p, root), "launch TODO comment (canonical / og:url / og:image)"))
for f, msg in issues:
    print(f"{f}: {msg}")
print(f"\n{len(issues)} item(s) to resolve before launch." if issues else "\nNo placeholders left.")
sys.exit(1 if issues else 0)
