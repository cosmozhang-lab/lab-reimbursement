#!/usr/bin/env python
import os
import sys
import re

class CustomExecutableGroup:
    def __init__(self, items):
        self.items = items
    def get(self, name):
        for item in self.items:
            if name == item.name:
                return item
        return None

class CustomExecutable:
    def __init__(self, name, path, modname):
        self.name = name.lower()
        self.path = os.path.realpath(path)
        self.modname = modname
    def get_execute(self):
        mod = __import__(self.modname, fromlist=tuple(self.modname.split(".")[-1]))
        return mod.execute

def get_custom_executables(basedir):
    custom_executables = []
    bindir = os.path.join(basedir, "bin")
    if not os.path.isdir(bindir):
        return CustomExecutableGroup(custom_executables)
    files = os.listdir(bindir)
    for filename in files:
        filepath = os.path.join(bindir, filename)
        if not os.path.isfile(filepath): continue
        if filename == "__init__.py": continue
        match = re.match(r"(^\w+).py$", filename)
        if match is None: continue
        modname = match.group(1)
        custom_executables.append(CustomExecutable(modname, filepath, "bin."+modname))
    return CustomExecutableGroup(custom_executables)


if __name__ == '__main__':
    basedir = os.path.dirname(__file__)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labreimbursement.settings')
    command = sys.argv[1]
    custom_executable = get_custom_executables(basedir).get(command)
    if custom_executable:
        sys.path.append(basedir)
        custom_executable = custom_executable.get_execute()
        custom_executable(sys.argv)
    else:
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)
