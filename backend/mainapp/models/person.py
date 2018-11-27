from .common import models
from .pinyin import HanziPinyinCEntryModel
from .auth import User
import re

class Person(HanziPinyinCEntryModel):
    createuser = models.ForeignKey(User, on_delete=models.CASCADE)
