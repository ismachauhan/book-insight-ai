from rest_framework.serializers import ModelSerializer
from .models import BookData

class BookDataSerializer(ModelSerializer):
    class Meta:
        model = BookData
        fields = '__all__'