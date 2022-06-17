from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

class EscolaForm(ModelForm):
    class Meta:
        model = Escola
        fields = '__all__'

class CertificadoForm(ModelForm):
    class Meta:
        model = Certificado
        fields = '__all__'

class HabilitacaoForm(ModelForm):
    class Meta:
        model = Habilitacao
        fields = '__all__'

class InteresseForm(ModelForm):
    class Meta:
        model = Interesse
        fields = '__all__'

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class TfcForm(ModelForm):
    class Meta:
        model = Tfc
        fields = '__all__'

class TecnicaForm(ModelForm):
    class Meta:
        model = Tecnica
        fields = '__all__'