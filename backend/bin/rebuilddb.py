from . import cleardb
from . import builddb

def execute(argv):
    cleardb.execute(argv)
    builddb.execute(argv)
