from .models import Price
from rest_framework import serializers

class PriceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'
