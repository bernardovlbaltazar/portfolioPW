from django.db import models

# Create your models here.

def projeto_path(instance,filename):
    return f'projeto/{instance.id}'

def tfcs_path(instance,filename):
    return f'tfcs/{instance.id}'

class Post(models.Model):
    autor = models.CharField(max_length=30)
    data = models.DateField(auto_now_add=True)
    hora = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField(max_length=200)

    def __str__(self):
        return self.titulo[:15]


class Pessoa(models.Model):
    nome = models.CharField(max_length=20)
    linkedin = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)

    def __str__(self):
        return self.nome


class Professor(models.Model):

    nome = models.CharField(max_length=20)
    linkedin = models.URLField(blank=True)
    lusofona = models.URLField(blank=True)

    def __str__(self):
        return self.nome

class Linguagem(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class Cadeira(models.Model):
    RANKING = {
        (1, '1 estrela'),
        (2, '2 estrelas'),
        (3, '3 estrelas'),
        (4, '4 estrelas'),
        (5, '5 estrelas'),
    }
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ranking = models.IntegerField(choices=RANKING)
    descricao = models.TextField()
    linguagens = models.ManyToManyField(Linguagem, blank=True)
    docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
    docente_praticas = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='praticas')

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=20)
    cadeira = models.ForeignKey(Cadeira, on_delete=models.CASCADE, related_name='cadeira')
    descricao = models.TextField(max_length=500)
    extensao = models.CharField(max_length=10, blank=True)
    imagem = models.ImageField(blank=True, upload_to=tfcs_path)
    ano_realizado = models.IntegerField(default=0)
    participantes = models.ManyToManyField(Pessoa, related_name="participacao")
    github = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    tech_usado = models.ManyToManyField(Tecnologia, related_name="tecnologia")

    def __str__(self):
        return self.titulo




class Escola(models.Model):
    nome = models.CharField(max_length=50)
    ano_inicio = models.IntegerField()
    ano_fim = models.IntegerField()

    def __str__(self):
        return self.nome

class Certificado(models.Model):
    titulo = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=50)
    ano_inicio = models.IntegerField()
    ano_fim = models.IntegerField(blank=True)

    def __str__(self):
        return self.titulo

class Habilitacao(models.Model):
    titulo = models.CharField(max_length=50)
    ano = models.IntegerField()

    def __str__(self):
        return self.titulo

class Interesse(models.Model):
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class Tecnica(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=50)
    mail = models.EmailField(blank=True)
    pontuacao = models.IntegerField()

    def __str__(self):
        return self.nome + ' | ' + str(self.pontuacao)

class Tfc(models.Model):
    autores = models.ManyToManyField(Pessoa, related_name='tfcAutores')
    orientadores = models.ManyToManyField(Professor, related_name='tfcOrientadores')
    ano = models.IntegerField()
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    imagem = models.ImageField(blank=True, upload_to=projeto_path)
    relatorio = models.FileField(blank=True)
    link_github = models.CharField(max_length=150, blank=True)
    link_video = models.CharField(max_length=150,blank=True)

    def __str__(self):
        return self.titulo