from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('questão/<int:id>', views.questions, name='question'),
    path('adicionar_curtida', views.add_like, name='add_like'),
    path('adicionar_avaliacao', views.add_assessments, name='add_assessments'),
    path('adicionar_comentario', views.add_commnet, name='add_commnet'),
    path('adicionar_resposta/<int:id>', views.add_response, name='add_response'),
    path('nova_questao', views.new_question, name='new_question'),
    path('categoria/<int:id>', views.filter_category, name='filter_category'),
    path('filtro', views.filter_options, name='filter_options'),
    path('pesquisa', views.search, name='search'),
]