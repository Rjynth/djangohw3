from django.db import models


class Phone(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    image = models.CharField(max_length=200)
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=20)