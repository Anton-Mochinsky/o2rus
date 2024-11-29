from django.db import models

class SparePart(models.Model):
    article = models.CharField(max_length=36)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
