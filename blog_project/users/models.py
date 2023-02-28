from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Profile(models.Model):
    gender_list=(
        ('','-------Select Gender-------'),
        ('Male','Male'),
        ('Female','Female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    gender = models.CharField(choices=gender_list, max_length=10)
    age = models.IntegerField()
    marital_status = models.BooleanField(default=False)
    mobile = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail (output_size)
            img.save(self.image.path)


