#!/usr/bin/env python
import os, re

def execute(argv):
    basedir = os.path.join(os.path.dirname(__file__), "..")
    files = os.listdir(basedir)
    # remove migration files
    for dirname in files:
        migdir = os.path.join(basedir, dirname, "migrations")
        if os.path.isdir(migdir):
            migfiles = os.listdir(migdir)
            for filename in migfiles:
                filepath = os.path.join(migdir, filename)
                if re.match(r"^\d+_\w+\.py$", filename) is None: continue
                if not os.path.isfile(filepath): continue
                os.remove(filepath)
                print("remove migration file:", os.path.join(dirname, "migrations", filename))
    # remove the db
    for filename in files:
        filepath = os.path.join(basedir, filename)
        if re.match(r".+\.(sqlite|sqlite3)$", filename) is None: continue
        if not os.path.isfile(filepath): continue
        os.remove(filepath)
        print("remove db file:", filename)
