from django.urls import path, include
from . import views

urlpatterns = [
    #acao
    path('acao/', views.acao_list),

    #campeonato
    path('campeonato/', views.campeonato_list),

    #equipa
    path('equipa/', views.equipa_list),

    #jogador
    path('jogador/', views.jogador_list),
    path('jogador/novo/', views.jogador_novo,name='jogador_novo'), # get and post req. for insert operation

    #jogo
    path('jogo/', views.jogo_list),

    #marcacao
    path('marcacao/', views.marcacao_list),

    #pontuacao
    path('pontuacao/', views.pontuacao_list),

    #resultado
    path('resultado/', views.resultado_list),

    #substituicao
    path('substituicao/', views.substituicao_list),

]