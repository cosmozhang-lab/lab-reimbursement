#-*- coding: utf-8 -*-

import os

file = open(os.path.join(os.path.dirname(__file__), "pinyin.txt"), "rb")
content = file.read()
content = content.decode("utf-8")
file.close()

table = {}
entries = content.replace("\n", "").replace(" ","").split(",")
print(len(entries))
for entry in entries:
    ch = entry[0]
    py = entry[1:]
    table[ch] = py

def translate(hanzi_str):
    return [table[ch] for ch in hanzi_str]

if __name__ == "__main__":
    import sys
    ch = sys.argv[1]
    print("汉字: %s" % ch)
    print("拼音: %s" % " ".join(translate(ch)))

