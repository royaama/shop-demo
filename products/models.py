from django.db import models
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200) # שם המוצר
    price = models.DecimalField(max_digits=10, decimal_places=2) # מחיר (למשל 99.90)
    stock = models.IntegerField() # כמה יש במלאי
    image_url = models.CharField(max_length=2000, blank=True) # לינק לתמונה (אופציונלי)

    def __str__(self):
        return self.title