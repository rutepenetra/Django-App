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
    context = {'acao_list':AcaoDisciplinar.objects.all()}
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
        if id == 0:
            form = AcaoForm(request.POST)
        else:
            acao = AcaoDisciplinar.objects.get(pk = id)
            form = AcaoForm(request.POST, instance = acao)
        if form.is_valid():
            form.save()
        return redirect('/acao/')

def acao_more(request, n_acao):
	try:
		acao = AcaoDisciplinar.objects.get(pk = n_acao)
	except AcaoDisciplinar.DoesNotExist:
		raise Http404('Acao Disciplinar não existe')
	return render(request, 'acao/acao_more.html', context={'acao':acao})

def acao_delete(request, acao):
    acao = AcaoDisciplinar.objects.get(pk = acao)
    acao.delete()
    return redirect('/acao/')

#campeonato
def campeonato_list(request):
    context = {'campeonato_list':Campeonato.objects.all()}
    return render( request, "campeonato/campeonato_list.html", context)


def campeonato_novo(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = CampeonatoForm()
        else:
            campeonato = Campeonato.objects.get(pk=id)
            form = CampeonatoForm(instance = campeonato)
        return render(request, "campeonato/campeonato_novo.html", {'form': form})
    else:
        if id == 0:
            form = CampeonatoForm(request.POST)
        else:
            campeonato = Campeonato.objects.get (pk = id)
            form = CampeonatoForm(request.POST, instance = campeonato)
        if form.is_valid():
            form.save()
        return redirect('/campeonato/')

def campeonato_more(request, n_campeonato):
	try:
		campeonato = Campeonato.objects.get(pk = n_campeonato)
	except Campeonato.DoesNotExist:
		raise Http404('Campeonato não existe')
	return render(request, 'campeonato/campeonato_more.html', context={'campeonato':campeonato})


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
            convocatoria = Convocatoria.objects.get(pk = id)
            form = ConvocatoriaForm(instance = convocatoria)
        return render(request, "convocatoria/convocatoria_novo.html", {'form': form})
     else:
        if id == 0:
            form = ConvocatoriaForm(request.POST)
        else:
            convocatoria = Convocatoria.objects.get(pk = id)
            form = ConvocatoriaForm(request.POST, instance = convocatoria)
        if form.is_valid():
            form.save()
        return redirect('/convocatoria/')

#epoca
def epoca_list(request):
	context = {'epoca_list':Epoca.objects.raw('SELECT epoca.n_campeonato,  '
                                                      'ano, nome_campeonato, count(ano)  '
                                                      ' FROM epoca inner join campeonato '
                                                       'on epoca.n_campeonato = campeonato.n_campeonato '
                                                       'group by epoca.n_campeonato, nome_campeonato, ano   '
                                                       'order by epoca.ano asc')}
	return render( request, "epoca/epoca_list.html", context)


def epoca_novo(request, id = 0):
     if request.method == "GET":
        if id == 0:
            form = EpocaForm()
        else:
            epoca = Epoca.objects.get(pk = id)
            form = EpocaForm(instance = epoca)
        return render(request, "epoca/epoca_novo.html", {'form': form})
     else:
        if id == 0:
            form = EpocaForm(request.POST)
        else:
            epoca = Epoca.objects.get(pk = id)
            form = EpocaForm(request.POST, instance = epoca)
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
            equipa = Equipa.objects.get(pk = id)
            form = EquipaForm(instance = equipa)
        return render(request, "equipa/equipa_novo.html", {'form': form})
    else:
        if id == 0:
            form = EquipaForm(request.POST)
        else:
            equipa = Equipa.objects.get(pk = id)
            form = EquipaForm(request.POST, instance = equipa)
        if form.is_valid():
            form.save()
        return redirect('/equipa/')

def equipa_more(request, n_equipa):
	try:
		equipa = Equipa.objects.get(pk = n_equipa)
	except Equipa.DoesNotExist:
		raise Http404('Equipa não existe')
	return render(request, 'equipa/equipa_more.html', context={'equipa':equipa})


#faixa_etaria
def faixa_etaria_list(request):
	context = {'faixa_etaria_list':FaixaEtaria.objects.all()}
	return render( request, "faixa_etaria/faixa_etaria_list.html", context)

def faixa_etaria_novo(request, id = 0):
     if request.method == "GET":
        if id == 0:
            form = FaixaEtariaForm()
        else:
            faixa_etaria = FaixaEtaria.objects.get(pk = id)
            form = FaixaEtariaForm(instance = faixa_etaria)
        return render(request, "faixa_etaria/faixa_etaria_novo.html", {'form': form})
     else:
        if id == 0:
            form = FaixaEtariaForm(request.POST)
        else:
            faixa_etaria = FaixaEtaria.objects.get(pk = id)
            form = FaixaEtariaForm(request.POST, instance = faixa_etaria)
        if form.is_valid():
            form.save()
        return redirect('/faixa_etaria/')

def faixa_etaria_more(request, n_faixa):
	try:
		faixa_etaria = FaixaEtaria.objects.get(pk = n_faixa)
	except FaixaEtaria.DoesNotExist:
		raise Http404('Faixa Etária não existe')
	return render(request, 'faixa_etaria/faixa_etaria_more.html', context={'faixa_etaria':faixa_etaria})


#jogador
def jogador_list(request):
    context = {'jogador_list':Jogador.objects.all()}

    return render( request, "jogador/jogador_list.html", context)

def jogador_novo(request, id = 0):
	if request.method == "GET":
		if id == 0:
			form = JogadorForm()
		else:
			jogador = Jogador.objects.get(pk = id)
			form = JogadorForm(instance = jogador)
		return render(request, "jogador/jogador_novo.html", {'form': form})
	else:
		if id == 0:
			form = JogadorForm(request.POST)
		else:
			jogador = Jogador.objects.get(pk = id)
			form = JogadorForm(request.POST, instance = jogador)
		if form.is_valid():
			form.save()
		return redirect('/jogador/')

def jogador_more(request, n_jogador):
	try:
		jogador = Jogador.objects.get(pk = n_jogador)
	except Jogador.DoesNotExist:
		raise Http404('Jogador não existe')
	return render(request, 'jogador/jogador_more.html', context={'jogador':jogador})


#jogo
def jogo_list(request):
    context = {'jogo_list':Jogo.objects.all()}
    return render( request, "jogo/jogo_list.html", context)


def jogo_novo(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = JogoForm()
        else:
            jogo = Jogo.objects.get(pk = id)
            form = JogoForm(instance = jogo)
        return render(request, "jogo/jogo_novo.html", {'form': form})
    else:
        if id == 0:
            form = JogoForm(request.POST)
        else:
            jogo = Jogo.objects.get(pk = id)
            form = JogoForm(request.POST, instance = jogo)
        if form.is_valid():
        	form.save()
        return redirect('/jogo/')

def jogo_more(request, n_jogo):
	try:
		jogo = Jogo.objects.get(pk = n_jogo)
	except Jogo.DoesNotExist:
		raise Http404('Jogo não existe')
	return render(request, 'jogo/jogo_more.html', context={'jogo':jogo})


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
            marcacao = Marcacao.objects.get(pk = id)
            form = MarcacaoForm(instance = marcacao)
        return render(request, "marcacao/marcacao_novo.html", {'form': form})
    else:
        if id == 0:
            form = MarcacaoForm(request.POST)
        else:
            marcacao = Marcacao.objects.get(pk = id)
            form = MarcacaoForm(request.POST, instance = marcacao)
        if form.is_valid():
            form.save()
        return redirect('/marcacao/')

#modalidade
def modalidade_list(request):
	context = {'modalidade_list':Modalidade.objects.all()}
	return render( request, "modalidade/modalidade_list.html", context)

def modalidade_novo(request, id = 0):
     if request.method == "GET":
        if id == 0:
            form = ModalidadeForm()
        else:
            modalidade = Modalidade.objects.get(pk = id)
            form = ModalidadeForm(instance = modalidade)
        return render(request, "modalidade/modalidade_novo.html", {'form': form})
     else:
        if id == 0:
            form = ModalidadeForm(request.POST)
        else:
            modalidade = Modalidade.objects.get(pk=id)
            form = ModalidadeForm(request.POST, instance = modalidade)
        if form.is_valid():
            form.save()
        return redirect('/modalidade/')

def modalidade_more(request, n_modalidade):
	try:
		modalidade = Modalidade.objects.get(pk = n_modalidade)
	except Modalidade.DoesNotExist:
		raise Http404('Modalidade não existe')
	return render(request, 'modalidade/modalidade_more.html', context={'modalidade':modalidade})


#pontuacao
def pontuacao_list(request):
    context = {'pontuacao_list':Pontuacao.objects.all()}
    return render( request, "pontuacao/pontuacao_list.html", context)


def pontuacao_novo(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = PontuacaoForm()
        else:
            pontuacao = Pontuacao.objects.get(pk = id)
            form = PontuacaoForm(instance = pontuacao)
        return render(request, "pontuacao/pontuacao_novo.html", {'form': form})
    else:
        if id == 0:
            form = Pontuacao(request.POST)
        else:
            pontuacao = Pontuacao.objects.get(pk = id)
            form = PontuacaoForm(request.POST, instance = pontuacao)
        if form.is_valid():
            form.save()
        return redirect('/pontuacao/')

#resultado
def resultado_list(request):
    context = {'resultado_list':ResultadoJogo.objects.all()}
    return render( request, "resultado/resultado_list.html", context)


def resultado_novo(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = ResultadoForm()
        else:
            resultado = ResultadoJogo.objects.get(pk = id)
            form = ResultadoForm(instance = resultado)
        return render(request, "resultado/resultado_novo.html", {'form': form})
    else:
        if id == 0:
            form = ResultadoForm(request.POST)
        else:
            resultado = ResultadoJogo.objects.get(pk = id)
            form = ResultadoForm(request.POST, instance = resultado)
        if form.is_valid():
            form.save()
        return redirect('/resultado/')


#substituicao
def substituicao_list(request):
    context = {'substituicao_list':Substituicao.objects.all()}
    return render( request, "substituicao/substituicao_list.html", context)


def substituicao_novo(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = SubstituicaoForm()
        else:
            substituicao = Substituicao.objects.get(pk = id)
            form = SubstituicaoForm(instance = substituicao)
        return render(request, "substituicao/substituicao_novo.html", {'form': form})
    else:
        if id == 0:
            form = SubstituicaoForm(request.POST)
        else:
            substituicao = Substituicao.objects.get(pk = id)
            form = SubstituicaoForm(request.POST, instance = substituicao)
        if form.is_valid():
            form.save()
        return redirect('/substituicao/')

def substituicao_more(request, n_substituicao):
	try:
		substituicao = Substituicao.objects.get(pk = n_substituicao)
	except Substituicao.DoesNotExist:
		raise Http404('Substituicao não existe')
	return render(request, 'substituicao/substituicao_more.html', context={'substituicao':substituicao})

def substituicao_delete(request, substituicao):
    substituicao = Substituicao.objects.get(pk = substituicao)
    substituicao.delete()
    return redirect('/substituicao/')

#tipo_acao
def tipo_acao_list(request):
    context = {'tipo_acao_list':TipoAcao.objects.all()}
    return render( request, "tipo_acao/tipo_acao_list.html", context)


def tipo_acao_novo(request, id = 0):
     if request.method == "GET":
        if id == 0:
            form = TipoAcaoForm()
        else:
            tipo_acao = TipoAcao.objects.get(pk = id)
            form = TipoAcaoForm(instance = tipo_acao)
        return render(request, "tipo_acao/tipo_acao_novo.html", {'form': form})
     else:
        if id == 0:
            form = TipoAcaoForm(request.POST)
        else:
            tipo_acao = TipoAcao.objects.get(pk = id)
            form = TipoAcaoForm(request.POST, instance = tipo_acao)
        if form.is_valid():
            form.save()
        return redirect('/tipo_acao/')

def tipo_acao_more(request, n_tipo):
	try:
		tipo_acao = TipoAcao.objects.get(pk = n_tipo)
	except TipoAcao.DoesNotExist:
		raise Http404('Tipo de Ação não existe')
	return render(request, 'tipo_acao/tipo_acao_more.html', context={'tipo_acao':tipo_acao})


 #tipo_pontucao
def tipo_pontuacao_list(request):
    context = {'tipo_pontuacao_list':TipoPontuacao.objects.all()}
    return render( request, "tipo_pontuacao/tipo_pontuacao_list.html", context)


def tipo_pontuacao_novo(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = TipoPontuacaoForm()
        else:
            tipo_pontuacao = TipoPontuacao.objects.get(pk = id)
            form = TipoPontuacaoForm(instance = tipo_pontuacao)
        return render(request, "tipo_pontuacao/tipo_pontuacao_novo.html", {'form': form})
    else:
        if id == 0:
            form = TipoPontuacaoForm(request.POST)
        else:
            tipo_pontuacao = TipoPontuacao.objects.get(pk = id)
            form = TipoPontuacaoForm(request.POST, instance = tipo_pontuacao)
        if form.is_valid():
            form.save()
        return redirect('/tipo_pontuacao/')

def tipo_pontuacao_more(request, n_tipo):
	try:
		tipo_pontuacao = TipoPontuacao.objects.get(pk = n_tipo)
	except TipoPontuacao.DoesNotExist:
		raise Http404('Tipo de Pontuação não existe')
	return render(request, 'tipo_pontuacao/tipo_pontuacao_more.html', context={'tipo_pontuacao':tipo_pontuacao})
