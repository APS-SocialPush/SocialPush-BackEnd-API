from rest_framework import serializers
from ...models.scheduled_post import ScheduledPost


class ScheduledPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledPost
        fields = '__all__'
