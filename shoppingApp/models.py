from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Item(models.Model):
    itemName = models.CharField(max_length=50)
    itemInfo = models.CharField(max_length=100)
    itemPrice = models.FloatField()
    itemCount = models.IntegerField()
    itemImage = ProcessedImageField(
                processors=[ResizeToFill(300,300)],
                format='JPEG',
                options={'quality':90},
            )
    # itemImage = models.ImageField(null=True)
    
    def __str__(self):
        return self.itemName
