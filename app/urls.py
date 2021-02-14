from django.urls import path, include
from . import views

urlpatterns = [
    #main
    path('', views.main_view),

    #acao
    path('acao/', views.acao_list),
    path('acao/novo/', views.acao_novo, name='acao_novo'),
    path('acao/<int:id>/', views.acao_novo,name='acao_update'), # get and post req. for update operation

    #campeonato
    path('campeonato/', views.campeonato_list),
    path('campeonato/novo/', views.campeonato_novo, name='campeonato_novo'),
    path('campeonato/<int:id>/', views.campeonato_novo,name='campeonato_update'), # get and post req. for update operation

    #convocatoria
    path('convocatoria/', views.convocatoria_list),
    path('convocatoria/novo/', views.convocatoria_novo, name='convocatoria_novo'),
    #path('convocatoria/<int:id>/', views.convocatoria_novo,name='convocatoria_update'), # get and post req. for update operation

    #epoca
    path('epoca/', views.epoca_list),
    path('epoca/novo/', views.epoca_novo, name='epoca_novo'),
    #path('epoca/<int:id>/', views.epoca_novo,name='epoca_update'), # get and post req. for update operation

    #equipa
    path('equipa/', views.equipa_list),
    path('equipa/novo/', views.equipa_novo, name='equipa_novo'),
    #path('equipa/<int:id>/', views.equipa_novo,name='equipa_update'), # get and post req. for update operation

    #faixa_etaria
    path('faixa_etaria/', views.faixa_etaria_list),
    path('faixa_etaria/novo/', views.faixa_etaria_novo, name='faixa_etaria_novo'),
    #path('faixa_etaria/<int:id>/', views.faixa_etaria_novo,name='faixa_etaria_update'), # get and post req. for update operation

    #jogador
    path('jogador/', views.jogador_list),
    path('jogador/novo/', views.jogador_novo, name='jogador_novo'), # get and post req. for insert operation
    #path('jogador/<int:id>/', views.jogador_novo,name='jogador_update'), # get and post req. for update operation

    #jogo
    path('jogo/', views.jogo_list),
    path('jogo/novo/', views.jogo_novo, name='jogo_novo'),
    #path('jogo/<int:id>/', views.jogo_novo,name='jogo_update'), # get and post req. for update operation

    #marcacao
    path('marcacao/', views.marcacao_list),
    path('marcacao/novo/', views.marcacao_novo, name='marcacao_novo'),
    #path('marcacao/<int:id>/', views.marcacao_novo,name='marcacao_update'), # get and post req. for update operation

    #modalidade
    path('modalidade/', views.modalidade_list),
    path('modalidade/novo/', views.modalidade_novo, name='modalidade_novo'),
    #path('modalidade/<int:id>/', views.modalidade_novo,name='modalidade_update'), # get and post req. for update operation

    #pontuacao
    path('pontuacao/', views.pontuacao_list),
    path('pontuacao/novo/', views.pontuacao_novo, name='pontuacao_novo'),
    #path('pontuacao/<int:id>/', views.pontuacao_novo,name='pontuacao_update'), # get and post req. for update operation

    #resultado
    path('resultado/', views.resultado_list),
    path('resultado/novo/', views.resultado_novo, name='resultado_novo'),
    #path('resultado/<int:id>/', views.resultado_novo,name='resultado_update'), # get and post req. for update operation

    #substituicao
    path('substituicao/', views.substituicao_list),
    path('substituicao/novo/', views.substituicao_novo, name='substituicao_novo'),
    #path('substituicao/<int:id>/', views.substituicao_novo,name='substituicao_update'), # get and post req. for update operation

    #tipo_acao
    path('tipo_acao/', views.tipo_acao_list),
    path('tipo_acao/novo/', views.tipo_acao_novo, name='tipo_acao_novo'),
    #path('tipo_acao/<int:id>/', views.tipo_acao_novo,name='tipo_acao_update'), # get and post req. for update operation

    #tipo_pontuacao
    path('tipo_pontuacao/', views.tipo_pontuacao_list),
    path('tipo_pontuacao/novo/', views.tipo_pontuacao_novo, name='tipo_pontuacao_novo'),
    #path('tipo_pontuacao/<int:id>/', views.tipo_pontuacao_novo,name='tipo_pontuacao_update'), # get and post req. for update operation
]