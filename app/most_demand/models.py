from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class MostDemand(models.Model):
    category=models.CharField(_('category'),max_length=255,blank=True,null=True)
    quantity=models.IntegerField(_('quantity'),blank=True,null=True,default=1)
    timestamp = models.DateTimeField(
        _('timestamp'), default=timezone.now)


    class Meta:
        ordering = ["-id"]
