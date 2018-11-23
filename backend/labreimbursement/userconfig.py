#-*-coding: utf-8 -*-

class ConfigItem:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

quotes = [('"','"'), ("'","'")]

def asfloat(s):
    try:
        val = float(s)
        return val
    except ValueError:
        return None

def asint(s):
    try:
        val = int(s)
        return val
    except ValueError:
        return None

def asbool(s):
    if s.lower() == "true":
        return True
    elif s.lower() == "false":
        return False
    else:
        return None


def parseline(linestr):
    lineparts = linestr.split("=")
    if len(lineparts) < 2:
        return None
    paramname = lineparts[0].strip().lower()
    paramvalue = ".".join(lineparts[1:]).strip()
    if len(paramname) == 0:
        return None
    # if paramvalue is quoted, remove the quotes
    quoted = False
    for quote in quotes:
        if paramvalue.startswith(quote[0]) and paramvalue.endswith(quote[1]):
            startpos = len(quote[0])
            endpos = len(paramvalue) - len(quote[1])
            paramvalue = paramvalue[startpos:endpos]
            quoted = True
            break
    if not quoted:
        val = None
        if val is None: val = asint(paramvalue)
        if val is None: val = asfloat(paramvalue)
        if val is None: val = asbool(paramvalue)
        if not val is None:
            paramvalue = val
    return ConfigItem(paramname, paramvalue)

class ConfigSet:
    def __init__(self):
        self._dict = {}
    def __getattr__(self, name):
        if name in self._dict:
            return self._dict[name]
        else:
            return None

def loadconfig(filename, configset=None):
    if configset is None:
        configset = ConfigSet()
    with open(filename, "r") as f:
        while True:
            line = f.readline()
            if not line: break
            item = parseline(line)
            if not item: continue
            configset._dict[item.name] = item.value
    return configset

import os
project_path = os.path.join(os.path.dirname(__file__),"..")
configfiles = [os.path.join(project_path, "config.example.conf"), os.path.join(project_path, "config.conf")]
userconfig = None
for configfilename in configfiles:
    if os.path.isfile(configfilename):
        userconfig = loadconfig(configfilename, userconfig)
