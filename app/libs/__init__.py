# coding: utf-8

import random
import string

def randstr(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

