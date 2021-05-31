from rest_framework import serializers
from .models import Mem

class MemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mem
        fields = ('user_id','title', 'url','description')