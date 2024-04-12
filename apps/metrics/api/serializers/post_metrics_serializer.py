from rest_framework import serializers
from ...models.post_metrics import PostMetrics


class PostMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMetrics
        fields = '__all__'
