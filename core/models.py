from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, default='비공개')
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"


class Farm(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='Fororo')

    # Basic Animals
    donkey = models.BooleanField(default=False)
    dog = models.BooleanField(default=False)
    cat = models.BooleanField(default=False)
    rooster = models.BooleanField(default=False)
    chick = models.BooleanField(default=False)

    farm = models.ManyToManyField('CustomAnimal', through='Farmer')

    def __str__(self):
        return f"{self.owner}'s Farm: {self.name}"


class CustomAnimal(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    photo = models.ImageField(blank=True, null=True)
    audio = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.owner}'s Animal: {self.name}"


class Farmer(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    custom_animal = models.ForeignKey(CustomAnimal, on_delete=models.CASCADE)
    is_placed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.farm} {self.custom_animal} {self.is_placed}"
