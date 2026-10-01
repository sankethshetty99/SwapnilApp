#!/usr/bin/env python3
"""Inject page.html + data.json into worker.js at deploy time.

Replaces __DATA_JSON__ in page.html with the data, then replaces
__PAGE_HTML__ in worker.js with the result as a JS string literal.
"""
import json
import sys

page = open("page.html").read()
data = json.load(open("data.json"))
if "__DATA_JSON__" not in page:
    sys.exit("data placeholder missing from page.html")
page = page.replace("__DATA_JSON__", json.dumps(data))

src = open("worker.js").read()
if "__PAGE_HTML__" not in src:
    sys.exit("page placeholder missing from worker.js")
open("worker.js", "w").write(src.replace("__PAGE_HTML__", json.dumps(page)))
print("injected page:", len(page), "bytes")
