from django.db import models

class CommonManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
class CommonModel(models.Model):
    deleted = models.BooleanField(default=False)
    createtime = models.DateTimeField(auto_now=True)
    objects = CommonManager()
    def delete(self):
        self.deleted = True
        self.save()
    def delete_from_db(self):
        models.Model.delete(self)
