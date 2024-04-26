from django.db import models
from socialmedia.models.post import Post
from socialmedia.models.account import SocialMediaAccount


class ScheduledPost(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    social_media_account = models.ForeignKey(
        SocialMediaAccount,
        on_delete=models.CASCADE
    )

    scheduled_date_time = models.DateTimeField()

    class Meta:
        verbose_name = 'Postagem Agendada'
        verbose_name_plural = 'Postagens Agendadas'

    def __str__(self):
        return f'Postagem Agendada para {self.social_media_account} em {self.scheduled_date_time}'
