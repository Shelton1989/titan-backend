from rest_framework import serializers
from api.models import User, UserProfile, Garage, Asset

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('title', 'photo', 'employee_number', )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.title = profile_data.get('title', profile.title)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.employee_number = profile_data.get('employee_number', profile.employee_number)
        profile.save()

        return instance

class GarageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Garage
        fields = (
            'url',
            'title',
            'manager_title',
            'manager_name',
            'email_address',
            'contact_number',
            'street_address',
            'suburb',
            'ext',
            'city',
            'province',
        )

class AssetSerializer(serializers.HyperlinkedModelSerializer):
    garage = GarageSerializer(read_only=True)

    class Meta: 
        model = Asset
        fields = (
            'url',
            'garage',
            'asset_serial_number',
            'make',
            'model',
            'receiver_size',
            'receiver_serial_number',
            'receiver_manufacturer',
            'belt_size',
            'belt_section',
            'block_serial_number',
            'block_model',
            'motor_size',
            'motor_amps',
            'pressure_switch_details',
            'water_trap',
            'installation_date',
            'last_service',
        )