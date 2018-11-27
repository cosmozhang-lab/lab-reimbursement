from .common import models, CommonModel
from .pinyin import HanziPinyinCEntryModel
from .auth import User
from .person import Person
import re

class Reimbursement(CommonModel):
    createuser = models.ForeignKey(User, on_delete=models.CASCADE)
    toperson = models.ForeignKey(Person, related_name='reimbursement_toperson', on_delete=models.CASCADE)
    submittime = models.DateTimeField()
    arrivetime = models.DateTimeField(null=True)
    arrivefee = models.DateTimeField(null=True)

class ReimbursementArrival(CommonModel):
    createuser = models.ForeignKey(User, on_delete=models.CASCADE)

class InvoiceType(HanziPinyinCEntryModel):
    createuser = models.ForeignKey(User, on_delete=models.CASCADE)

class Invoice(CommonModel):
    createuser = models.ForeignKey(User, on_delete=models.CASCADE)
    itype = models.ForeignKey(InvoiceType, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024, null=True)
    issuetime = models.DateTimeField()
    issueperson = models.ForeignKey(Person, related_name='invoice_issueperson', on_delete=models.CASCADE)
    payperson = models.ForeignKey(Person, related_name='invoice_payperson', on_delete=models.CASCADE)
    reimburse = models.ForeignKey(Reimbursement, null=True, related_name='invoice_reimbursement', on_delete=models.SET_NULL)
