from django.shortcuts import render
from .models import AcaoDisciplinar
from .models import Campeonato
from .models import Convocatoria
from .models import Epoca
from .models import Equipa
from .models import FaixaEtaria
from .models import Jogador
from .models import Jogo
from .models import Marcacao
from .models import Modalidade
from .models import Pontuacao
from .models import ResultadoJogo
from .models import Substituicao
from .models import TipoAcao
from .models import TipoPontuacao


from .forms import JogadorForm


#acao
def acao_list(request):
    context = {'acao_list':AcaoDisciplinar.objects.raw('SELECT n_acao,  '
                                                               'CASE WHEN equipa_a <> 0 '
                                                                        'THEN (Select nome_equipa from equipa where n_equipa = equipa_a) '
                                                               'END equipa_1,  '
                                                        	  ' CASE WHEN equipa_b <> 0 '
                                                                      'THEN (Select nome_equipa from equipa where n_equipa = equipa_b) '
                                                        				'END equipa_2, nome, tipo_acao.descricao '
                                                       ' FROM acao_disciplinar inner join jogador '
                                                        'on acao_disciplinar.jogador = jogador.n_jogador inner join resultado_jogo '
                                                        'on acao_disciplinar.jogo = resultado_jogo.n_jogo inner join tipo_acao '
                                                        'on acao_disciplinar.tipo = tipo_acao.n_tipo_acao')}
    return render( request, "acao/acao_list.html", context)


def acao_novo(request):
    return


#campeonato
def campeonato_list(request):
    context = {'campeonato_list':Campeonato.objects.raw('SELECT CAMPEONATO.N_CAMPEONATO, CAMPEONATO.NOME_CAMPEONATO, EPOCA.ANO, COUNT(EPOCA.N_JOGO) '
                                                           'FROM CAMPEONATO INNER JOIN EPOCA '
                                                            'ON CAMPEONATO.N_CAMPEONATO = EPOCA.N_CAMPEONATO '
                                                           'GROUP BY CAMPEONATO.N_CAMPEONATO, CAMPEONATO.NOME_CAMPEONATO, EPOCA.ANO ')}
    return render( request, "campeonato/campeonato_list.html", context)


def campeonato_novo(request):
    return


#equipa
def equipa_list(request):
    context = {'equipa_list':Equipa.objects.all()}
    return render( request, "equipa/equipa_list.html", context)


def equipa_novo(request):
    return


#jogador
def jogador_list(request):
    context = {'jogador_list':Jogador.objects.raw('SELECT Jogador.n_jogador, nome, nome_equipa, nome_modalidade FROM Jogador INNER JOIN Convocatoria '
    'ON Jogador.n_jogador = Convocatoria.n_jogador INNER JOIN Equipa '
    'ON Convocatoria.n_equipa = Equipa.n_equipa INNER JOIN Modalidade '
    'ON Equipa.modalidade = Modalidade.n_modalidade '
    'GROUP BY Jogador.n_jogador, nome, nome_equipa, nome_modalidade, Equipa.n_equipa '
    'ORDER BY Equipa.n_equipa')}

    return render( request, "jogador/jogador_list.html", context)

def jogador_novo(request, id=0):
        if request.method == "GET":
            if id == 0:
                form = JogadorForm()
            else:
                jogador = Jogador.objects.get(pk=id)
                form = JogadorForm(instance=jogador)
            return render(request, "jogador/jogador_novo.html", {'form': form})
        else:
            if id == 0:
                form = JogadorForm(request.POST)
            else:
                jogador = Jogador.objects.get(pk=id)
                form = JogadorForm(request.POST,instance= jogador)
            if form.is_valid():
                form.save()
            return redirect('/jogador/')

#jogo
def jogo_list(request):
    context = {'jogo_list':Jogo.objects.raw('SELECT jogo.n_jogo, '
                                               'CASE WHEN equipa_a <> 0 '
                                               ' THEN (Select nome_equipa from equipa where n_equipa = equipa_a) '
                                               'END equipa_a, '
                                               'CASE WHEN equipa_b <> 0 '
                                                ' THEN (Select nome_equipa from equipa where n_equipa = equipa_b) '
                                                'END equipa_b, dia, hora, localizacao '
                                            'FROM jogo inner join resultado_jogo  '
                                            'on jogo.n_jogo = resultado_jogo.n_jogo')}
    return render( request, "jogo/jogo_list.html", context)


def jogo_novo(request):
    return



#marcacao
def marcacao_list(request):
    context = {'marcacao_list':Marcacao.objects.raw('SELECT n_marcacao, '
                                                          ' CASE  WHEN equipa_a <> 0 '
                                                                   ' THEN (Select nome_equipa from equipa where n_equipa = equipa_a) '
                                                           'END equipa_a, '
                                                    	 '  CASE	WHEN equipa_b <> 0 '
                                                                  'THEN (Select nome_equipa from equipa where n_equipa = equipa_b) '
                                                    				'END equipa_b, nome, minuto '
                                                    'FROM marcacao inner join resultado_jogo  '
                                                    	'on marcacao.n_jogo = resultado_jogo.n_jogo inner join jogador '
                                                    	'on marcacao.n_jogador = jogador.n_jogador')}
    return render( request, "marcacao/marcacao_list.html", context)


def marcacao_novo(request):
    return



#pontuacao
def pontuacao_list(request):
    context = {'pontuacao_list':Pontuacao.objects.all()}
    return render( request, "pontuacao/pontuacao_list.html", context)


def pontuacao_novo(request):
    return



#resultado
def resultado_list(request):
    context = {'resultado_list':ResultadoJogo.objects.raw('SELECT n_jogo, '
                                                            ' CASE  WHEN equipa_a <> 0 '
                                                                     ' THEN (Select nome_equipa from equipa where n_equipa = equipa_a) '
                                                             'END equipa_1, '
                                                         '  CASE	WHEN equipa_b <> 0 '
                                                                    'THEN (Select nome_equipa from equipa where n_equipa = equipa_b) '
                                                                    'END equipa_2, pontuacao_a, pontuacao_b '
                                                      'FROM resultado_jogo ')}
    return render( request, "resultado/resultado_list.html", context)


def resultado_novo(request):
    return



#substituicao
def substituicao_list(request):
    context = {'substituicao_list':Substituicao.objects.raw('SELECT n_substituicao, jogo, '
                                                            ' CASE  WHEN equipa_a <> 0 '
                                                                     ' THEN (Select nome_equipa from equipa where n_equipa = equipa_a) '
                                                             'END equipa_1, '
                                                            '  CASE	WHEN equipa_b <> 0 '
                                                                    'THEN (Select nome_equipa from equipa where n_equipa = equipa_b) '
                                                                    'END equipa_2, pontuacao_a, pontuacao_b '
                                                                'FROM substituicao INNER JOIN Resultado_jogo '
                                                                'on substituicao.jogo = resultado_jogo.n_jogo inner join jogador '
                                                                ' on substituicao.jogador_entra = jogador.n_jogador')}
    return render( request, "substituicao/substituicao_list.html", context)


def substituicao_novo(request):
    return

