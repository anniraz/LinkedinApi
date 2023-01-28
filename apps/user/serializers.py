from rest_framework import serializers

from apps.user.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            'email',
            "first_name",
            "last_name",
            'phone_number',
            'image',
            'is_premium',
            'password',
                  )
        read_only_fields=('is_premium',)


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user