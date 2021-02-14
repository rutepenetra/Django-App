# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcaoDisciplinar(models.Model):
    n_acao = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.ForeignKey('TipoAcao', models.DO_NOTHING, db_column='tipo')
    jogador = models.ForeignKey('Jogador', models.DO_NOTHING, db_column='jogador')
    jogo = models.ForeignKey('Jogo', models.DO_NOTHING, db_column='jogo')

    def __str__(self):
            return self.descricao
    class Meta:
        managed = False
        db_table = 'acao_disciplinar'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Campeonato(models.Model):
    n_campeonato = models.AutoField(primary_key=True)
    nome_campeonato = models.CharField(max_length=100)

    def __str__(self):
            return self.nome_campeonato
    class Meta:
        managed = False
        db_table = 'campeonato'


class Convocatoria(models.Model):
    n_jogo = models.OneToOneField('Jogo', models.DO_NOTHING, db_column='n_jogo', primary_key=True)
    n_equipa = models.ForeignKey('Equipa', models.DO_NOTHING, db_column='n_equipa')
    n_jogador = models.ForeignKey('Jogador', models.DO_NOTHING, db_column='n_jogador')
    posicao = models.CharField(max_length=50)
    suplente = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'convocatoria'
        unique_together = (('n_jogo', 'n_equipa', 'n_jogador'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Epoca(models.Model):
    n_campeonato = models.OneToOneField(Campeonato, models.DO_NOTHING, db_column='n_campeonato', primary_key=True)
    n_jogo = models.ForeignKey('Jogo', models.DO_NOTHING, db_column='n_jogo')
    ano = models.CharField(max_length=20)

    def __str__(self):
            return self.ano
    class Meta:
        managed = False
        db_table = 'epoca'
        unique_together = (('n_campeonato', 'n_jogo'),)


class Equipa(models.Model):
    n_equipa = models.AutoField(primary_key=True)
    nome_equipa = models.CharField(max_length=50)
    fundacao = models.IntegerField()
    origem = models.CharField(max_length=50)
    telefone = models.IntegerField()
    email = models.CharField(max_length=50)
    descricao_equipa = models.CharField(max_length=150, blank=True, null=True)
    treinador = models.CharField(max_length=50)
    modalidade = models.ForeignKey('Modalidade', models.DO_NOTHING, db_column='modalidade', blank=True, null=True)
    faixa_etaria = models.ForeignKey('FaixaEtaria', models.DO_NOTHING, db_column='faixa_etaria', blank=True, null=True)

    def __str__(self):
            return self.nome_equipa
    class Meta:
        managed = False
        db_table = 'equipa'


class FaixaEtaria(models.Model):
    n_faixa = models.AutoField(primary_key=True)
    designacao = models.CharField(max_length=25)

    def __str__(self):
            return self.designacao
    class Meta:
        managed = False
        db_table = 'faixa_etaria'


class Jogador(models.Model):
    n_jogador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    data_nasc = models.DateField()
    nif = models.IntegerField()
    telefone = models.IntegerField()
    email = models.CharField(max_length=50)
    morada = models.CharField(max_length=100)

    def __str__(self):
            return self.nome
    class Meta:
        managed = False
        db_table = 'jogador'


class Jogo(models.Model):
    n_jogo = models.AutoField(primary_key=True)
    dia = models.DateField()
    hora = models.TimeField()
    localizacao = models.CharField(max_length=50)


    class Meta:
        managed = False
        db_table = 'jogo'


class Marcacao(models.Model):
    n_marcacao = models.AutoField(primary_key=True)
    n_jogo = models.ForeignKey(Jogo, models.DO_NOTHING, db_column='n_jogo')
    n_jogador = models.ForeignKey(Jogador, models.DO_NOTHING, db_column='n_jogador')
    minuto = models.CharField(max_length=6)
    descricao = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marcacao'


class Modalidade(models.Model):
    n_modalidade = models.AutoField(primary_key=True)
    nome_modalidade = models.CharField(max_length=50)
    tipo_pontuacao = models.ForeignKey('TipoPontuacao', models.DO_NOTHING, db_column='tipo_pontuacao')

    def __str__(self):
            return self.nome_modalidade

    class Meta:
        managed = False
        db_table = 'modalidade'


class Pontuacao(models.Model):
    n_equipa = models.OneToOneField(Equipa, models.DO_NOTHING, db_column='n_equipa', primary_key=True)
    n_campeonato = models.ForeignKey(Campeonato, models.DO_NOTHING, db_column='n_campeonato')
    pontuacao_total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pontuacao'
        unique_together = (('n_equipa', 'n_campeonato'),)


class ResultadoJogo(models.Model):
    n_jogo = models.OneToOneField(Jogo, models.DO_NOTHING, db_column='n_jogo', primary_key=True)
    equipa_a = models.ForeignKey(Equipa, models.DO_NOTHING, related_name='equipa_a', db_column='equipa_a')
    equipa_b = models.ForeignKey(Equipa, models.DO_NOTHING, related_name='equipa_b', db_column='equipa_b')
    pontuacao_a = models.IntegerField()
    pontuacao_b = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'resultado_jogo'
        unique_together = (('n_jogo', 'equipa_a', 'equipa_b'),)


class Substituicao(models.Model):
    n_substituicao = models.AutoField(primary_key=True)
    jogo = models.ForeignKey(Jogo, models.DO_NOTHING, db_column='jogo')
    jogador_entra = models.ForeignKey(Jogador, models.DO_NOTHING, related_name='jogador_entra', db_column='jogador_entra')
    jogador_sai = models.ForeignKey(Jogador, models.DO_NOTHING, related_name='jogador_sai', db_column='jogador_sai')

    class Meta:
        managed = False
        db_table = 'substituicao'


class TipoAcao(models.Model):
    n_tipo_acao = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    modalidade = models.ForeignKey(Modalidade, models.DO_NOTHING, db_column='modalidade')

    def __str__(self):
            return self.descricao

    class Meta:
        managed = False
        db_table = 'tipo_acao'


class TipoPontuacao(models.Model):
    n_tipo_pontuacao = models.AutoField(primary_key=True)
    descricao_tipo_pontuacao = models.CharField(max_length=100)
    vitoria = models.IntegerField()
    derrota = models.IntegerField()
    empate = models.IntegerField()

    def __str__(self):
            return self.descricao_tipo_pontuacao
    class Meta:
        managed = False
        db_table = 'tipo_pontuacao'
