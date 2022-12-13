from django.db import models

# Create your models here.
class Songs(models.Model):
    name=models.CharField(max_length=250)
    artist=models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name