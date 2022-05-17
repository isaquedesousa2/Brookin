from django.db import models
from authentication.models import User

class Base(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

class Account(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    stars = models.IntegerField(default=0,verbose_name='Estrelas')

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'

    def __str__(self):
        return self.user.username

