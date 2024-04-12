from rest_framework import serializers
from ...models.socialmedia_metrics import SocialMediaMetrics


class SocialMediaMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaMetrics
        fields = '__all__'