from rest_framework import serializers
from ...models.account import SocialMediaAccount


class SocialMediaAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaAccount
        fields = '__all__'