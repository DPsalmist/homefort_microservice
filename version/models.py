from django.db import models

# Create your models here.
class AppVersion(models.Model):
    android_version = models.CharField(max_length=20, blank=True)
    ios_version = models.CharField(max_length=20, blank=True)
    android_dismissible = models.BooleanField(max_length=20, blank=True, default=False)
    ios_dismissible = models.BooleanField(max_length=20, blank=True, default=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}{}'.format(str(self.android_version), str(self.ios_version))