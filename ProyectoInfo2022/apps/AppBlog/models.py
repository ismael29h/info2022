from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


#....
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    imagen = models.ImageField(upload_to='posts/imagenes', default='')
    intro = RichTextField()
    body = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    
    body = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
    
    def __str__(self):
        return self.body