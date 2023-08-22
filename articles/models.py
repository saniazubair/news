from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title