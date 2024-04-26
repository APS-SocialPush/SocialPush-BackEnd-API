from django.db import models


class SocialMediaAccount(models.Model):
    PLATFORMS = {
        "Tt": "Twitter",
        "Meta": "Facebook",
        "Insta": "Instagram",
        "-": "-"
    }

    username = models.CharField(
        verbose_name="Nome de Usuário",
        max_length=120,
        unique=True
    )

    platform = models.CharField(
        verbose_name="Plataforma",
        max_length=50,
        choices=PLATFORMS,
        default='Twitter'
    )

    access_token = models.CharField(
        verbose_name="Token de acesso",
        max_length=255,
    )

    created_at = models.DateTimeField(
        verbose_name="Data de criação",
        auto_now_add=True
    )

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        verbose_name = "Midia Social"
        verbose_name_plural = "Mídias Sociais"

    def __str__(self):
        """Retorna a representação do objeto como string."""

        return f'Conta de {self.platform}: {self.username}'
