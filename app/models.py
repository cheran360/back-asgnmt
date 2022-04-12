import sys
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.
class Record(models.Model):
    image = models.ImageField(upload_to="my_picture", blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    species = models.CharField(max_length=100, null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((140, 140))

        # after modifications, save it to the output
        im.save(output, format='PNG', quality=90)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.png" % self.image.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(Record, self).save(*args, **kwargs)
