from django.urls import path, include
from . import views

urlpatterns = [
    #main
    path('', views.main_view),

    #acao
    path('acao/', views.acao_list),
    path('acao/novo/', views.acao_novo, name='acao_novo'),

    #campeonato
    path('campeonato/', views.campeonato_list),
    path('campeonato/novo/', views.campeonato_novo, name='campeonato_novo'),

    #convocatoria
    path('convocatoria/', views.convocatoria_list),
    path('convocatoria/novo/', views.acao_novo, name='convocatoria_novo'),

    #epoca
    path('epoca/', views.epoca_list),
    path('epoca/novo/', views.epoca_novo, name='epoca_novo'),

    #equipa
    path('equipa/', views.equipa_list),
    path('equipa/novo/', views.equipa_novo, name='equipa_novo'),

    #faixa_etaria
    path('faixa_etaria/', views.faixa_etaria_list),
    path('faixa_etaria/novo/', views.faixa_etaria_novo, name='faixa_etaria_novo'),

    #jogador
    path('jogador/', views.jogador_list),
    path('jogador/novo/', views.jogador_novo, name='jogador_novo'), # get and post req. for insert operation

    #jogo
    path('jogo/', views.jogo_list),
    path('jogo/novo/', views.jogo_novo, name='jogo_novo'),

    #marcacao
    path('marcacao/', views.marcacao_list),
    path('marcacao/novo/', views.marcacao_novo, name='marcacao_novo'),

    #modalidade
    path('modalidade/', views.modalidade_list),
    path('modalidade/novo/', views.modalidade_novo, name='modalidade_novo'),

    #pontuacao
    path('pontuacao/', views.pontuacao_list),
    path('pontuacao/novo/', views.pontuacao_novo, name='pontuacao_novo'),

    #resultado
    path('resultado/', views.resultado_list),
    path('resultado/novo/', views.resultado_novo, name='resultado_novo'),

    #substituicao
    path('substituicao/', views.substituicao_list),
    path('substituicao/novo/', views.substituicao_novo, name='substituicao_novo'),

    #tipo_acao
    path('tipo_acao/', views.tipo_acao_list),
    path('tipo_acao/novo/', views.tipo_acao_novo, name='tipo_acao_novo'),

    #tipo_pontuacao
    path('tipo_pontuacao/', views.tipo_pontuacao_list),
    path('tipo_pontuacao/novo/', views.tipo_pontuacao_novo, name='tipo_pontuacao_novo'),
]