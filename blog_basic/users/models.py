from django.db import models
from django.db.models.fields import TextField
from tinymce.models import HTMLField
from django.urls import reverse


class VyasProfile(models.Model):

    profile_options =[
        ('award', 'Award'),
        ('favourite', 'Favourite'),
        ('code', 'Code'),
        ('community', 'Community'),
    ]



    Title = models.CharField(max_length=100)
    # Description = HTMLField()
    Description = TextField()
    Date_started = models.DateField()
    Date_ended = models.DateField(blank=True, null=True)
    Category= models.CharField(max_length=30, choices=profile_options, default='Community')
    # profile_image = models.ImageField(default='default.jpg', upload_to='logos')


    def __str__(self):
        return f'{self.Title}'

    def get_absolute_url(self):
        return reverse('profile' )