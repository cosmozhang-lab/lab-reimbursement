#-*- coding: utf-8 -*-

import os
import re


def unique(arr):
    ret = []
    for item in arr:
        if not item in ret:
            ret.append(item)
    return ret

def load_data():
    dirname = os.path.dirname(__file__)
    filenames = os.listdir(dirname)
    # filenames = ["pinyin.2.txt"]
    content = ""
    for filename in filenames:
        if re.match(r"pinyin", filename) is None: continue
        file = open(os.path.join(os.path.dirname(__file__), filename), "rb")
        thecontent = file.read()
        thecontent = thecontent.decode("utf-8")
        content += thecontent
        file.close()
    table = {}
    entries = content.replace("\n", "").replace(" ","").split(",")
    for entry in entries:
        if not entry: continue
        ch = entry[0]
        py = entry[1:]
        if ch in table:
            if not py in table[ch]:
                table[ch].append(py)
        else:
            table[ch] = [py]
    for ch in table:
        table[ch] = unique(table[ch])
    return table

table = load_data()

py2pya_dict = {"ā":"a","á":"a","ǎ":"a","à":"a","ō":"o","ó":"o","ǒ":"o","ò":"o","ē":"e","é":"e","ě":"e","è":"e","ī":"i","í":"i","ǐ":"i","ì":"i","ū":"u","ú":"u","ǔ":"u","ù":"u","ü":"v","ǘ":"v","ǚ":"v","ǜ":"v"}
def py2pya(py):
    for k in py2pya_dict:
        py = py.replace(k, py2pya_dict[k])
    return py

def translate_hz2py(hanzi_str):
    results = [[]]
    for ch in hanzi_str:
        newresults = []
        for oldresult in results:
            table_record = [ch] if re.match("[\x00-\x7f]", ch) else table[ch]
            for py in table_record:
                newresults.append(oldresult + [py])
        results = newresults
    return results

def translate_hz2pya(hanzi_str):
    results = [py2pya(" ".join(item)) for item in translate_hz2py(hanzi_str)]
    results = [item.split(" ") for item in unique(results)]
    return results

def translate_hz2pyc(hanzi_str):
    return unique(["".join([word[0].upper() for word in item]) for item in translate_hz2pya(hanzi_str)])

if __name__ == "__main__":
    import sys
    ch = sys.argv[1]
    print("汉字: %s" % ch)
    print("==============")
    for result in translate_hz2py(ch):
        print("拼音: %s" % " ".join(result))
    print("==============")
    for result in translate_hz2pya(ch):
        print("英拼: %s" % " ".join(result))
    print("==============")
    for result in translate_hz2pyc(ch):
        print("简拼: %s" % result)


