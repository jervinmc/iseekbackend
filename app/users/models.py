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


class User(models.Model):
    email=models.CharField(_('email'),max_length=255,blank=True,null=True)
    password=models.CharField(_('password'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]
