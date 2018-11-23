#!/usr/bin/env python
import os, re
from .utils.util import django_management_execute

def execute(argv):
    basedir = os.path.join(os.path.dirname(__file__), "..")
    django_management_execute(["manage.py", "makemigrations"])
    django_management_execute(["manage.py", "migrate"])
