from django.db import models

# Create your models here.
class Record(models.Model):
    image = models.FileField(upload_to="my_picture", blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    species = models.CharField(max_length=100, null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

