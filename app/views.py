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
    context = {'acao_list':AcaoDisciplinar.objects.all()}
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
    context = {'jogo_list':Jogo.objects.all()}
    return render( request, "jogo/jogo_list.html", context)


def jogo_novo(request):
    return



#marcacao
def marcacao_list(request):
    context = {'marcacao_list':Marcacao.objects.all()}
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
    context = {'resultado_list':ResultadoJogo.objects.all()}
    return render( request, "resultado/resultado_list.html", context)


def resultado_novo(request):
    return



#substituicao
def substituicao_list(request):
    context = {'substituicao_list':Substituicao.objects.all()}
    return render( request, "substituicao/substituicao_list.html", context)


def substituicao_novo(request):
    return


