from django.db import models
from django.utils import timezone 

# Create your models here.
class SoilMoistureReading(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    soil_moisture_percentage = models.IntegerField()
    
    
    def __str__(self):
        return f'Soil Moisture Reading at {self.timestamp.strftime("%Y-%m-%d %H:%M:%S")} - {self.soil_moisture_percentage}'


