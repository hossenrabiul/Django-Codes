from django.db import models
from catagories.models import Category
from author.models import Author
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #one to many relationship

    def __str__(self):
        return f"name : {self.title}"
