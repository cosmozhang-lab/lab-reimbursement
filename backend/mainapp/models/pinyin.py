from django.db import models
from .common import CommonManager, CommonModel
from utilities.pinyin import translate_hz2pyc

class HanziPinyinC(models.Model):
    hanzi = models.CharField(max_length=128)
    pinyinc = models.CharField(max_length=128)
    
    @classmethod
    def create(cls, hanzi=None):
        records = list(HanziPinyinC.objects.filter(hanzi=hanzi))
        if len(records) == 0:
            pinyincs = translate_hz2pyc(hanzi)
            records = []
            for pinyinc in pinyincs:
                rec = HanziPinyinC(hanzi=hanzi, pinyinc=pinyinc)
                rec.save()
                records.append(rec)
        return records

    @classmethod
    def get(cls, hanzi=None):
        records = list(HanziPinyinC.objects.filter(hanzi=hanzi))

    @classmethod
    def process_filter_args(cls, kwargs, paramname, real_paramname):
        newkwargs = {}
        for kw in kwargs:
            kwparts = kw.split("__")
            if kwparts[0] in [paramname, real_paramname]:
                oldval = kwargs[kw]
                kwparts[0] = real_paramname
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
                newkwargs[newkw] = oldval
            else:
                newkwargs[kw] = kwargs[kw]
        return newkwargs

class HanziPinyinCEntryModelManager(CommonManager):
    def filter(self, **kwargs):
        kwargs = HanziPinyinC.process_filter_args(kwargs, "name", "names")
        print(kwargs)
        return CommonManager.filter(self, **kwargs)

class HanziPinyinCEntryModel(CommonModel):
    names = models.ManyToManyField(HanziPinyinC)

    objects = HanziPinyinCEntryModelManager()

    @classmethod
    def create(cls, name=None, **kwargs):
        entry = cls(**kwargs)
        entry.save()
        if name:
            entry.name = name
        return entry

    @property
    def name(self):
        return self.names.first().hanzi
    @name.setter
    def name(self, name=None):
        hzpycs = HanziPinyinC.create(hanzi=name)
        self.names.set(hzpycs)

