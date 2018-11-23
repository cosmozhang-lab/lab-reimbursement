from random import random

def randomstring(length=32):
    choices = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nchoices = len(choices)
    out = ""
    for i in range(length):
        out += choices[int(random()*nchoices)]
    return out
