from django.db import models


class Author(models.Model):
    first_name = models.CharField("First Name", max_length=64)
    last_name = models.CharField("Last Name", max_length=64)
    birthday_year = models.PositiveIntegerField("Year")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Biography(models.Model):
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    title = models.CharField(max_length=64)
    authors = models.ManyToManyField(Author)
