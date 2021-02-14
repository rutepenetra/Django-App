from django.shortcuts import render, redirect
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
from .forms import EquipaForm
from .forms import JogoForm
from .forms import MarcacaoForm
from .forms import EpocaForm
from .forms import ConvocatoriaForm
from .forms import ResultadoForm
from .forms import PontuacaoForm
from .forms import AcaoForm
from .forms import TipoAcaoForm
from .forms import SubstituicaoForm
from .forms import CampeonatoForm
from .forms import ModalidadeForm
from .forms import TipoPontuacaoForm
from .forms import FaixaEtariaForm


#main
def main_view(request):
    return render( request, "main/base2.html")

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


def acao_novo(request, id = 0):
     if request.method == "GET":
        if id==0:
            form = AcaoForm()
        else:
            acao = AcaoDisciplinar.objects.get(pk=id)
            form = AcaoForm(instance = acao)
        return render(request, "acao/acao_novo.html", {'form': form})
     else:
         form = AcaoForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/acao/')

#campeonato
def campeonato_list(request):
    context = {'campeonato_list':Campeonato.objects.raw('SELECT CAMPEONATO.N_CAMPEONATO, CAMPEONATO.NOME_CAMPEONATO, EPOCA.ANO, COUNT(EPOCA.N_JOGO) '
                                                           'FROM CAMPEONATO INNER JOIN EPOCA '
                                                            'ON CAMPEONATO.N_CAMPEONATO = EPOCA.N_CAMPEONATO '
                                                           'GROUP BY CAMPEONATO.N_CAMPEONATO, CAMPEONATO.NOME_CAMPEONATO, EPOCA.ANO ')}
    return render( request, "campeonato/campeonato_list.html", context)


def campeonato_novo(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = CampeonatoForm()
        else:
            campeonato = CampeonatoForm.objects.get(pk=id)
            form = CampeonatoForm(instance = campeonato)
        return render(request, "campeonato/campeonato_novo.html", {'form': form})
    else:
        form = CampeonatoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/campeonato/')

#convocatoria
def convocatoria_list(request):
	context = {'convocatoria_list':Convocatoria.objects.raw('SELECT convocatoria.n_jogo,  '
                                                              'CASE WHEN equipa_a <> 0 '
                                                                       'THEN (Select nome_equipa from equipa where n_equipa = equipa_a) '
                                                              'END equipa_1,  '
                                                          ' CASE WHEN equipa_b <> 0 '
                                                                     'THEN (Select nome_equipa from equipa where n_equipa = equipa_b) '
                                                                    'END equipa_2, nome_equipa, count(convocatoria.n_jogador) '
                                                      ' FROM convocatoria inner join equipa '
                                                       'on convocatoria.n_equipa = equipa.n_equipa inner join resultado_jogo '
                                                       'on convocatoria.n_jogo = resultado_jogo.n_jogo '
                                                       'group by convocatoria.n_equipa, convocatoria.n_jogo, resultado_jogo.equipa_a, resultado_jogo.equipa_b, equipa.nome_equipa '
                                                       'order by convocatoria.n_jogo asc')}
	return render( request, "convocatoria/convocatoria_list.html", context)


def convocatoria_novo(request, id = 0):
     if request.method == "GET":
        if id == 0:
            form = ConvocatoriaForm()
        else:
            convocatoria = ConvocatoriaForm.objects.get(pk = id)
            form = ConvocatoriaForm(instance = convocatoria)
        return render(request, "convocatoria/convocatoria_novo.html", {'form': form})
     else:
         form = ConvocatoriaForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/convocatoria/')

#epoca
def epoca_list(request):
	context = {'epoca_list':Epoca.objects.raw('SELECT epoca.n_campeonato,  '
                                                      'ano, nome_campeonato, count(ano)  '
                                                      ' FROM epoca inner join campeonato '
                                                       'on epoca.n_campeonato = campeonato.n_campeonato '
                                                       'group by epoca.n_campeonato, nome_campeonato, ano '
                                                       'order by epoca.ano asc')}
	return render( request, "epoca/epoca_list.html", context)


def epoca_novo(request, id = 0):
     if request.method == "GET":
        if id == 0:
            form = EpocaForm()
        else:
            epoca = EpocaForm.objects.get(pk = id)
            form = EpocaForm(instance = epoca)
        return render(request, "epoca/epoca_novo.html", {'form': form})
     else:
         form = EpocaForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/epoca/')

#equipa
def equipa_list(request):
    context = {'equipa_list':Equipa.objects.all()}
    return render( request, "equipa/equipa_list.html", context)


def equipa_novo(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = EquipaForm()
        else:
            equipa = EquipaForm.objects.get(pk = id)
            form = EquipaForm(instance = equipa)
        return render(request, "equipa/equipa_novo.html", {'form': form})
    else:
         form = EquipaForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/equipa/')

#faixa_etaria
def faixa_etaria_list(request):
	context = {'faixa_etaria_list':FaixaEtaria.objects.raw('SELECT n_faixa,  '
                                                      'designacao, count(*)  '
                                                      ' FROM faixa_etaria inner join equipa '
                                                       'on faixa_etaria.n_faixa = equipa.faixa_etaria '
                                                       'group by faixa_etaria.n_faixa, designacao '
                                                       )}
	return render( request, "faixa_etaria/faixa_etaria_list.html", context)

def faixa_etaria_novo(request, id = 0):
     if request.method == "GET":
        if id == 0:
            form = FaixaEtariaForm()
        else:
            faixa_etaria = FaixaEtariaForm.objects.get(pk = id)
            form = FaixaEtariaForm(instance = faixa_etaria)
        return render(request, "faixa_etaria/faixa_etaria_novo.html", {'form': form})
     else:
         form = FaixaEtariaForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/faixa_etaria/')

#jogador
def jogador_list(request):
    context = {'jogador_list':Jogador.objects.raw('SELECT Jogador.n_jogador, nome, nome_equipa, nome_modalidade FROM Jogador INNER JOIN Convocatoria '
    'ON Jogador.n_jogador = Convocatoria.n_jogador INNER JOIN Equipa '
    'ON Convocatoria.n_equipa = Equipa.n_equipa INNER JOIN Modalidade '
    'ON Equipa.modalidade = Modalidade.n_modalidade '
    'GROUP BY Jogador.n_jogador, nome, nome_equipa, nome_modalidade, Equipa.n_equipa '
    'ORDER BY Equipa.n_equipa')}

    return render( request, "jogador/jogador_list.html", context)

def jogador_novo(request, id = 0):
	if request.method == "GET":
		if id == 0:
			form = JogadorForm()
		else:
			jogador = JogadorForm.objects.get(pk = id)
			form = JogadorForm(instance = jogador)
		return render(request, "jogador/jogador_novo.html", {'form': form})
	else:
	    form = JogadorForm(request.POST)
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


def jogo_novo(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = JogoForm()
        else:
            jogo = JogoForm.objects.get(pk = id)
            form = JogoForm(instance = jogo)
        return render(request, "jogo/jogo_novo.html", {'form': form})
    else:
         form = JogoForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/jogo/')



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


def marcacao_novo(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = MarcacaoForm()
        else:
            marcacao = MarcacaoForm.objects.get(pk = id)
            form = MarcacaoForm(instance = marcacao)
        return render(request, "marcacao/marcacao_novo.html", {'form': form})
    else:
         form = MarcacaoForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/marcacao/')

#modalidade
def modalidade_list(request):
	context = {'modalidade_list':Modalidade.objects.raw('SELECT n_modalidade,  '
                                                      'nome_modalidade, count(*)  '
                                                      ' FROM modalidade inner join equipa '
                                                       'on modalidade.n_modalidade = equipa.modalidade '
                                                       'group by n_modalidade, nome_modalidade '
                                                       )}
	return render( request, "modalidade/modalidade_list.html", context)

def modalidade_novo(request, id = 0):
     if request.method == "GET":
        if id == 0:
            form = ModalidadeForm()
        else:
            modalidade = ModalidadeForm.objects.get(pk = id)
            form = ModalidadeForm(instance = modalidade)
        return render(request, "modalidade/modalidade_novo.html", {'form': form})
     else:
         form = ModalidadeForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/modalidade/')

#pontuacao
def pontuacao_list(request):
    context = {'pontuacao_list':Pontuacao.objects.all()}
    return render( request, "pontuacao/pontuacao_list.html", context)


def pontuacao_novo(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = PontuacaoForm()
        else:
            pontuacao = PontuacaoForm.objects.get(pk = id)
            form = PontuacaoForm(instance = pontuacao)
        return render(request, "pontuacao/pontuacao_novo.html", {'form': form})
    else:
         form = Pontuacao(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/pontuacao/')

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


def resultado_novo(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = ResultadoForm()
        else:
            resultado = ResultadoForm.objects.get(pk = id)
            form = ResultadoForm(instance = resultado)
        return render(request, "resultado/resultado_novo.html", {'form': form})
    else:
         form = ResultadoForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/resultado/')


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


def substituicao_novo(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = SubstituicaoForm()
        else:
            substituicao = SubstituicaoForm.objects.get(pk = id)
            form = SubstituicaoForm(instance = substituicao)
        return render(request, "substituicao/substituicao_novo.html", {'form': form})
    else:
         form = SubstituicaoForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/substituicao/')

#tipo_acao
def tipo_acao_list(request):
    context = {'tipo_acao_list':TipoAcao.objects.raw('SELECT n_tipo_acao, descricao, nome_modalidade '
                                                    'FROM tipo_acao INNER JOIN modalidade '
                                                    'on tipo_acao.modalidade = modalidade.n_modalidade ')}
    return render( request, "tipo_acao/tipo_acao_list.html", context)


def tipo_acao_novo(request, id = 0):
     if request.method == "GET":
        if id == 0:
            form = TipoAcaoForm()
        else:
            tipo_acao = TipoAcaoForm.objects.get(pk = id)
            form = TipoAcaoForm(instance = tipo_acao)
        return render(request, "tipo_acao/tipo_acao_novo.html", {'form': form})
     else:
         form = TipoAcaoForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/tipo_acao/')

 #tipo_pontucao
def tipo_pontuacao_list(request):
    context = {'tipo_pontuacao_list':TipoPontuacao.objects.raw('SELECT n_tipo_pontuacao, vitoria, derrota, empate, nome_modalidade '
                                                                'FROM tipo_pontuacao INNER JOIN modalidade '
                                                                'on tipo_pontuacao.n_tipo_pontuacao = modalidade.tipo_pontuacao '
                                                                )}
    return render( request, "tipo_pontuacao/tipo_pontuacao_list.html", context)


def tipo_pontuacao_novo(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = AcaoForm()
        else:
            tipo_pontuacao = TipoPontuacaoForm.objects.get(pk = id)
            form = TipoPontuacaoForm(instance = tipo_pontuacao)
        return render(request, "tipo_pontuacao/tipo_pontucao_novo.html", {'form': form})
    else:
      form = AcaoForm(request.POST)
      if form.is_valid():
          form.save()
      return redirect('/tipo_pontuacao/')

