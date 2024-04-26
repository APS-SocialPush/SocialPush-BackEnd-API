from django.db import models
from .account import SocialMediaAccount


class Post(models.Model):
    social_media_account = models.ForeignKey(
        SocialMediaAccount,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Conta de Rede Social",
    )

    text = models.TextField(
        verbose_name="Texto da Postagem",
    )

    image = models.ImageField(
        upload_to='posts/images',
        blank=True,
        null=True,
        verbose_name = "Imagem da Postagem",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data e Hora da Criação",
    )

    scheduled_date_time = models.DateTimeField(
        verbose_name="Data e Hora do Agendamento",
    )

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        verbose_name = "Postagem"
        verbose_name_plural = "Postagem"

    def __str__(self):
        """Retorna a representação do objeto como string."""

        return f'Postagem de {self.social_media_account} em {self.scheduled_date_time}'
