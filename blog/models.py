from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(  # The ForeignKey, to Allow a 'many-to-one'
        'auth.User',  # Built in User model as reference
        on_delete=models.CASCADE
    )
    body = models.TextField()

    def __str__(self):
        return self.title
  
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
