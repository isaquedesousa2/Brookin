from django.db import models
from authentication.models import User


class Base(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True, null=True, verbose_name='Usuário')
    comment = models.CharField(max_length=200, verbose_name='Comentário')

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return self.comment

class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT,default='Usuário excluido', verbose_name='Usuário')
    response = models.CharField(max_length=10000, verbose_name='Resposta')
    number_assessments = models.IntegerField(verbose_name='Número de avaliações', blank=True,  default=0)
    assessments = models.IntegerField(verbose_name='Avaliações', blank=True,  default=0)
    assessments_voted = models.BooleanField('Usuário atual votou?', default=False)
    users_assessments = models.ManyToManyField(User, related_name='users_as', blank=True, verbose_name='Usuário que avaliaram')
    likes = models.IntegerField(verbose_name='Curtidas', blank=True,  default=0)
    likes_voted = models.BooleanField('Usuário atual curtiu?', default=False)
    users_likes = models.ManyToManyField(User, related_name='users_lk', blank=True, verbose_name='Usuário que curtiram')
    comments = models.ManyToManyField('Comments', related_name='comment_users', blank=True, verbose_name='Comentários')

    def get_average(self):
        if self.assessments == 0:
            return 0
        else:
            return self.assessments / self.number_assessments 

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'

    def __str__(self):
        return self.user.username

class Questions(models.Model):
    levels = (
            ('Ensino fundamental (básico)', 'Ensino fundamental (básico)'),
            ('Ensino médio (secundário)', 'Ensino médio (secundário)'),
            ('Ensino superior', 'Ensino superior'),
    )
    was_answered = models.BooleanField(default=False, verbose_name='Foi respondida?')
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, verbose_name='Usuário')
    date = models.DateField(auto_now_add=True, verbose_name='Data de criação')
    level = models.CharField(max_length=50, choices=levels)
    question = models.CharField(max_length=20000, verbose_name='Questão')
    answers = models.ManyToManyField('Answers', related_name='answer', blank=True, verbose_name='Respostas')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Questâo'
        verbose_name_plural = 'Questões'
