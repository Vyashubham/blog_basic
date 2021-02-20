from django.db import models
from django.db.models.fields import TextField
from django.urls import reverse
# from tinymce.models import HTMLField
from django.utils.text import slugify


class Post(models.Model):

    Title = models.CharField(max_length=100)
    Content = TextField()
    Date = models.DateTimeField(auto_now_add=True)
    Last_Modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('post_detail_view', kwargs={'slug': self.slug})


class VyasProfile(models.Model):

    profile_options =[
        ('award', 'Award'),
        ('favourite', 'Favourite'),
        ('code', 'Code'),
        ('community', 'Community'),
    ]



    Title = models.CharField(max_length=100)
    Description = TextField()
    Date_started = models.DateField()
    Date_ended = models.DateField(blank=True, null=True)
    Category= models.CharField(max_length=30, choices=profile_options, default='Community')
    profile_image = models.ImageField(default='default.jpg', upload_to='logos')


    def __str__(self):
        return f'{self.Title}'

    def get_absolute_url(self):
        return reverse('profile' )