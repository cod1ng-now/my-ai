from django.db import models

# Create your models here.
class Image(models.Model):
    pharse = models.CharField(max_length=200)
    ai_image = models.ImageField(upload_to="images")
    
    def __str__(self):
        return self.pharse