from django.db import models
from utilities.pinyin import translate_hz2pyc

class HanziPinyinC(models.Model):
    hanzi = models.CharField(max_length=128)
    pinyinc = models.CharField(max_length=128)
    
    def create(hanzi=None):
        records = HanziPinyinC.objects.filter(hanzi=hanzi)
        if records.count() == 0:
            pinyincs = translate_hz2pyc(hanzi)
            records = []
            for pinyinc in pinyincs:
                rec = HanziPinyinC(hanzi=hanzi, pinyinc=pinyinc)
                rec.save()
                records.append(rec)
        return records

