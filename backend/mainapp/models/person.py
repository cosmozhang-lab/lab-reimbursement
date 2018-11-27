from django.db import models
from .pinyin import HanziPinyinC
from .auth import User
import re

class PersonManager(models.Manager):
    def filter(self, **kwargs):
        for kw in kwargs:
            kwparts = kw.split("__")
            if kwparts[0] in ["name", "names"]:
                oldval = kwargs[kw]
                del(kwargs[kw])
                kwparts[0] = "names"
                def default_field(val):
                    for ch in oldval:
                        chascii = ord(ch)
                        if chascii > 0x7f:
                            return "hanzi"
                    return "pinyinc"
                if len(kwparts) > 1:
                    if not kwparts[1] in ["hanzi", "pinyinc"]:
                        kwparts = kwparts[0:1] + [default_field(oldval)] + kwparts[1:]
                else:
                    kwparts.append(default_field(oldval))
                newkw = "__".join(kwparts)
                kwargs[newkw] = oldval
        return models.Manager.filter(self, **kwargs)

class Person(models.Model):
    names = models.ManyToManyField(HanziPinyinC)
    createtime = models.DateTimeField(auto_now=True)
    createuser = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = PersonManager()

    def create(name=None, user=None, **kwargs):
        if user: kwargs["createuser"] = user
        person = Person(**kwargs)
        person.save()
        if name:
            person.name = name
        return person

    @property
    def name(self):
        return self.names.first().hanzi
    @name.setter
    def name(self, name=None):
        hzpycs = HanziPinyinC.create(hanzi=name)
        self.names.set(hzpycs)
