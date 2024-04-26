from celery import shared_task
from .models import ScheduledPost
from django.conf import settings

import tweepy

@shared_task
def publicar_postagem_agendada(scheduled_post_id):
    scheduled_post = ScheduledPost.objects.get(pk=scheduled_post_id)
    client = tweepy.Client(consumer_key=settings.API_KEY, consumer_secret=settings.API_KEY_SECRET, access_token=settings.ACCESS_TOKEN, access_token_secret=settings.ACCESS_TOKEN_SECRET)
    response = client.create_tweet(text=scheduled_post.post.text)

    scheduled_post.delete()  # Exclui a postagem agendada após a publicação
