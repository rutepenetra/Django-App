from django import forms
from .models import Jogador
from .models import Jogo
from .models import Equipa
from .models import Marcacao
from .models import Epoca
from .models import Convocatoria
from .models import ResultadoJogo
from .models import Pontuacao
from .models import AcaoDisciplinar
from .models import TipoAcao
from .models import TipoPontuacao
from .models import Substituicao
from .models import FaixaEtaria
from .models import Modalidade
from .models import Campeonato




#JOGADOR
class JogadorForm(forms.ModelForm):

    class Meta:
        model = Jogador
        fields = ('nome','data_nasc','nif','telefone', 'email', 'morada')
        labels = {
            'nome':'Nome Completo',
            'data_nasc':'Data Nascimento',
            'nif':'Nº de Contribuinte',
            'telefone':'Telefone',
            'email':'Email',
            'morada':'Morada'
        }

#EQUPA
class EquipaForm(forms.ModelForm):

    class Meta:
        model = Equipa
        fields = ('nome_equipa','fundacao','origem','telefone', 'email', 'descricao_equipa', 'treinador', 'modalidade', 'faixa_etaria')
        labels = {
            'nome':'Nome Equipa',
            'fundacao':'Ano de Fundação',
            'origem':'Origem da Equipa',
            'telefone':'Telefone',
            'email':'Email',
            'descricao_equipa':'Descrição da Equipa',
            'treinador':'Treinador',
            'modalidade':'Modalidade',
            'faixa_etaria':'Faixa Etária'
        }

#JOGO
class JogoForm(forms.ModelForm):

        class Meta:
            model = Jogo
            fields = ('dia', 'hora', 'localizacao')
            labels = {
                'dia':'Dia do Jogo',
                'hora':'Hora do Jogo',
                'localizacao':'Localização do Jogo'
            }

#MARCACAO
class MarcacaoForm(forms.ModelForm):

    class Meta:
        model = Marcacao
        fields = ('n_jogo', 'n_jogador', 'minuto', 'descricao')
        labels = {
            'n_jogo':'Jogo',
            'n_jogador':'Jogador',
            'minuto':'Minuto da Marcação',
            'descricao':'Descrição da Marcação'
        }
#EPOCA
class EpocaForm(forms.ModelForm):

    class Meta:
        model = Epoca
        fields = ('n_campeonato', 'n_jogo', 'ano')
        labels = {
            'n_campeonato':'Campeonato',
            'n_jogo':'Jogo',
            'ano':'Ano'
        }
#CONVOCATORIA
class ConvocatoriaForm(forms.ModelForm):

    class Meta:
        model = Convocatoria
        fields = ('n_jogo', 'n_equipa', 'n_jogador', 'posicao', 'suplente')
        labels = {
            'n_jogo':'Jogo',
            'n_equipa':'Equipa',
            'n_jogador':'Jogador',
            'posicao':'Posição',
            'suplente':'Suplente'
        }
#RESULTADO
class ResultadoForm(forms.ModelForm):

    class Meta:
        model = ResultadoJogo
        fields = ('n_jogo', 'equipa_a', 'equipa_b', 'pontuacao_a', 'pontuacao_b')
        labels = {
            'n_jogo':'Jogo',
            'equipa_a':'Equipa A',
            'equipa_b':'Equipa B',
            'pontuacao_a':'Pontuação da Equipa A',
            'pontuacao_b':'Pontuação da Equipa B'
        }
#PONTUACAO
class PontuacaoForm(forms.ModelForm):

    class Meta:
        model = Pontuacao
        fields = ('n_equipa', 'n_campeonato', 'pontuacao_total')
        labels = {
            'n_equipa':'Equipa',
            'n_campeonato':'Campeonato',
            'pontuacao_total':'Pontuação Total'
        }
#ACAO
class AcaoForm(forms.ModelForm):

    class Meta:
        model = AcaoDisciplinar
        fields = ('descricao', 'tipo', 'jogador', 'jogo')
        labels = {
            'descricao':'Descrição da Ação',
            'tipo':'Tipo de Ação',
            'jogador':'Jogador',
            'jogo':'Jogo'
        }

#TIPO ACAO
class TipoAcaoForm(forms.ModelForm):

    class Meta:
        model = TipoAcao
        fields = ('descricao', 'modalidade')
        labels = {
            'descricao':'Descrição da Ação',
            'modalidade':'Modalidade'
        }



#SUBSTITUICAO
class SubstituicaoForm(forms.ModelForm):

    class Meta:
        model = Substituicao
        fields = ('jogo', 'jogador_entra', 'jogador_sai')
        labels = {
            'jogo':'Jogo',
            'jogador_entra':'Jogador Que Entra',
            'jogador_sai':'Jogador Que Sai'
        }
#CAMPEONATO
class CampeonatoForm(forms.ModelForm):

    class Meta:
        model = Campeonato
        fields = ('nome_campeonato',)
        labels = {
            'nome_campeonato':'Nome Campeonato'
        }
#MODALIDADE
class ModalidadeForm(forms.ModelForm):

    class Meta:
        model = Modalidade
        fields = ('nome_modalidade', 'tipo_pontuacao')
        labels = {
            'nome_modalidade':'Nome Modalidade',
            'tipo_pontuacao':'Tipo de Pontuação'
        }
#TIPO PONTUACAO
class TipoPontuacaoForm(forms.ModelForm):

    class Meta:
        model = TipoPontuacao
        fields = ('descricao_tipo_pontuacao','vitoria','derrota','empate')
        labels = {
          'descricao_tipo_pontuacao':'Descrição',
          'vitoria':'Pontos Em Caso de Vitória',
          'derrota':'Pontos Em Caso de Derrota',
          'empate':'Pontos Em Caso de Empate'
        }
#FAIXA ETARIA
class FaixaEtariaForm(forms.ModelForm):

    class Meta:
        model = FaixaEtaria
        fields = ('designacao',)
        labels = {
            'designacao':'Designação'
        }

