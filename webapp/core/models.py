from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    SPORTS = (
        (1, 'football'),
        (2, 'basketball'),
        (3, 'volleyball'),
        (4, 'hockey'),
        (5, 'athletics'),
        (6, 'diving'),
        (7, 'biathlon'),
        (8, 'boxing'),
        (9, 'chess'),
    )
    sport = models.IntegerField(verbose_name='sport', choices=SPORTS)

    # преобразование к типу строки, для вывода в шаблоны и бд
    def __str___(self):
        return self.user.username
