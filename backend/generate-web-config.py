#/usr/bin/env python
# coding: utf-8

import sys, os

python_executable = sys.executable

wfastcgi_executable = None
for dirname in sys.path:
    filepath = os.path.join(dirname, "wfastcgi.py")
    if os.path.isfile(filepath):
        wfastcgi_executable = filepath
        break
if wfastcgi_executable is None:
    raise SystemError("Cannot find the wfastcgi executable")

project_path = os.path.realpath( os.path.dirname(__file__) )

replacements = {
    "python_executable": python_executable,
    "wfastcgi_executable": wfastcgi_executable,
    "project_path": project_path
}

infilepath = os.path.join(project_path, "web.template.config")
outfilepath = os.path.join(project_path, "web.config")
with open(infilepath, "r") as infile:
    content = infile.read()
    for repname in replacements:
        content = content.replace("$" + repname + "$", replacements[repname])
    with open(outfilepath, "w") as outfile:
        outfile.write(content)

print("web.config generation OK.")
