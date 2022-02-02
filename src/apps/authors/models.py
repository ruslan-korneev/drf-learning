from django.db import models


class Author(models.Model):
    first_name = models.CharField("First Name", max_length=64)
    last_name = models.CharField("Last Name", max_length=64)
    birthday_year = models.PositiveIntegerField("Year")