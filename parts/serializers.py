from rest_framework import serializers
from .models import SparePart

class SparePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SparePart
        fields = ['id', 'article', 'quantity', 'price', 'link', 'created_at']


