from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    User serializer for API responses.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'role', 'is_active']
        read_only_fields = ['id']

class UserDetailSerializer(serializers.ModelSerializer):
    """
    Detailed user serializer with extra fields.
    """
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'full_name', 'phone_number', 'role', 'is_active', 'created_at']
        read_only_fields = fields
    
    def get_full_name(self, obj):
        return obj.get_full_name() or obj.username
