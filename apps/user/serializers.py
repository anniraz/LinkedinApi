from rest_framework import serializers

from apps.user.models import User,Position,Skills,EducationInformation


class IsPremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['is_premium','premium_date','email']
        read_only_fields=('email','premium_date',)



class PositionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Position
        fields='__all__'
        read_only_fields=('user',)



class SkillsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Skills
        fields='__all__'
        read_only_fields=('user',)



class EducationInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model=EducationInformation
        fields='__all__'
        read_only_fields=('user',)




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