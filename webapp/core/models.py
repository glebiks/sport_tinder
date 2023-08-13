from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import int_list_validator

User = get_user_model()

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    tg_link = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(
        upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    SPORTS = (
        ('football', 'football'),
        ('basketball', 'basketball'),
        ('volleyball', 'volleyball'),
        ('hockey', 'hockey'),
        ('athletics', 'athletics'),
        ('diving', 'diving'),
        ('biathlon', 'biathlon'),
        ('boxing', 'boxing'),
        ('chess', 'chess'),
    )

    sport = models.CharField(max_length=16, choices=SPORTS, null=True, blank=True, default='football')

    matches = models.CharField(default=f'{id_user}',validators=[int_list_validator], max_length=256)  

    # преобразование к типу строки, для вывода в шаблоны и бд
    def __str___(self):
        return self.user.username