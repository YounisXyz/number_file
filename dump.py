import os, sys
os.system("git pull")
try:
    __import__("YOUNISXD").YOUNISXD()
except Exception as e:
    exit(str(e))
