from django.db import models


# Create your models here.
class Category(models.Model):
    NAME_MAX_LENGTH = 15

    name = models.CharField(max_length=NAME_MAX_LENGTH)

    def __str__(self):
        return self.name


class Todo(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
