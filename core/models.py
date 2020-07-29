from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, default='비공개')
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user


class Farm(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # Basic Animals
    donkey = models.BooleanField(default=False)
    dog = models.BooleanField(default=False)
    cat = models.BooleanField(default=False)
    rooster = models.BooleanField(default=False)

class CustomAnimal(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
