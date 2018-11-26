from django.db import models
from utilities.pinyin import translate_hz2pyc

class HanziWord(models.Model):
    table = models.CharField(max_length=128)
    recid = models.IntegerField()
    hanzi = models.CharField(max_length=128)
    pinyinc = models.CharField(max_length=128)
    def create(table, hanzi):
        if HanziWord.objects.filter(table=table, hanzi=hanzi).count() == 0:
            pinyincs = translate_hz2pyc(hanzi)

