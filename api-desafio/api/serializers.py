from api.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.CharField(source='django_user.email')
    password = serializers.CharField(source='django_user.password')

    class Meta:
        model = User
        fields = [
            'name',
            'born_date',
            'email',
            'password',
            'register',
        ]

    # def update(self, instance, validated_data):
    #     instance.save()
    #     return instance
        
