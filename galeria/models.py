from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    nomeUsuario = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    # Armazene a senha com hash e sal
    senha = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f'Nome [nome={self.nome}]'