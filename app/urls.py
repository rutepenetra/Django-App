from django.urls import path, include
from . import views

urlpatterns = [
    #main
    path('', views.main_view),

    #acao
    path('acao/', views.acao_list),
    path('acao/novo/', views.acao_novo, name='acao_novo'),
    path('acao/edit/<int:id>/', views.acao_novo, name='acao_update'),
    path('acao/more/<int:n_acao>/', views.acao_more, name='acao_more'),
    path('acao/delete/<int:acao>', views.acao_delete, name='acao_delete'),

    #campeonato
    path('campeonato/', views.campeonato_list),
    path('campeonato/novo/', views.campeonato_novo, name='campeonato_novo'),
    path('campeonato/edit/<int:id>/', views.campeonato_novo,name='campeonato_update'),
	path('campeonato/more/<int:n_campeonato>/', views.campeonato_more, name='campeonato_more'),

    #convocatoria
    path('convocatoria/', views.convocatoria_list),
    path('convocatoria/novo/', views.convocatoria_novo, name='convocatoria_novo'),

    #epoca
    path('epoca/', views.epoca_list),
    path('epoca/novo/', views.epoca_novo, name='epoca_novo'),

    #equipa
    path('equipa/', views.equipa_list),
    path('equipa/novo/', views.equipa_novo, name='equipa_novo'),
    path('equipa/edit/<int:id>/', views.equipa_novo,name='equipa_update'),
	path('equipa/more/<int:n_equipa>/', views.equipa_more, name='equipa_more'),

    #faixa_etaria
    path('faixa_etaria/', views.faixa_etaria_list),
    path('faixa_etaria/novo/', views.faixa_etaria_novo, name='faixa_etaria_novo'),
    path('faixa_etaria/edit/<int:id>/', views.faixa_etaria_novo,name='faixa_etaria_update'),
    path('faixa_etaria/more/<int:n_faixa>/', views.faixa_etaria_more, name='faixa_etaria_more'),

    #jogador
    path('jogador/', views.jogador_list),
    path('jogador/novo/', views.jogador_novo, name='jogador_novo'),
    path('jogador/edit/<int:id>/', views.jogador_novo,name='jogador_update'),
    path('jogador/more/<int:n_jogador>/', views.jogador_more, name='jogador_more'),

    #jogo
    path('jogo/', views.jogo_list),
    path('jogo/novo/', views.jogo_novo, name='jogo_novo'),
    path('jogo/edit/<int:id>/', views.jogo_novo,name='jogo_update'),
    path('jogo/more/<int:n_jogo>/', views.jogo_more, name='jogo_more'),

    #marcacao
    path('marcacao/', views.marcacao_list),
    path('marcacao/novo/', views.marcacao_novo, name='marcacao_novo'),

    #modalidade
    path('modalidade/', views.modalidade_list),
    path('modalidade/novo/', views.modalidade_novo, name='modalidade_novo'),
    path('modalidade/edit/<int:id>/', views.modalidade_novo,name='modalidade_update'),
    path('modalidade/more/<int:n_modalidade>/', views.modalidade_more, name='modalidade_more'),

    #pontuacao
    path('pontuacao/', views.pontuacao_list),
    path('pontuacao/novo/', views.pontuacao_novo, name='pontuacao_novo'),

    #resultado
    path('resultado/', views.resultado_list),
    path('resultado/novo/', views.resultado_novo, name='resultado_novo'),

    #substituicao
    path('substituicao/', views.substituicao_list),
    path('substituicao/novo/', views.substituicao_novo, name='substituicao_novo'),
    path('substituicao/edit/<int:id>/', views.substituicao_novo,name='substituicao_update'),
    path('substituicao/more/<int:n_substituicao>/', views.substituicao_more, name='substituicao_more'),
    path('substituicao/delete/<int:substituicao>', views.substituicao_delete, name='substituicao_delete'),


    #tipo_acao
    path('tipo_acao/', views.tipo_acao_list),
    path('tipo_acao/novo/', views.tipo_acao_novo, name='tipo_acao_novo'),
    path('tipo_acao/edit/<int:id>/', views.tipo_acao_novo,name='tipo_acao_update'),
    path('tipo_acao/more/<int:n_tipo>/', views.tipo_acao_more, name='tipo_acao_more'),

    #tipo_pontuacao
    path('tipo_pontuacao/', views.tipo_pontuacao_list),
    path('tipo_pontuacao/novo/', views.tipo_pontuacao_novo, name='tipo_pontuacao_novo'),
    path('tipo_pontuacao/edit/<int:id>/', views.tipo_pontuacao_novo,name='tipo_pontuacao_update'),
    path('tipo_pontuacao/more/<int:n_tipo>/', views.tipo_pontuacao_more, name='tipo_pontuacao_more'),
]