from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import *
from .models import *

def home_page_view(request):
    return render(request, 'portfolio/home.html')
def competencias_page_view(request):
    return render(request, 'portfolio/competencias.html')
def formacao_page_view(request):
    return render(request, 'portfolio/formacao.html')
def layout_page_view(request):
    return render(request, 'portfolio/layout.html')
def projetos_page_view(request):
    return render(request, 'portfolio/projetos.html', {
        'projetos': Projeto.objects.all()
    })
def about_page_view(request):
    context = {'cadeiras': Cadeira.objects.order_by('ano', 'semestre'),
               'escolas': Escola.objects.order_by('ano_inicio').reverse(),
               'certificados': Certificado.objects.order_by('ano_inicio').reverse(),
               'habilitacoes': Habilitacao.objects.order_by('ano').reverse(),
               'interesses': Interesse.objects.all(),
               'projetos': Projeto.objects.all()
               }
    return render(request, 'portfolio/about.html', context)
def contact_page_view(request):
    return render(request, 'portfolio/contact.html')
def blog_page_view(request):
    context = {'posts': Post.objects.order_by('hora').reverse() }
    return render(request, 'portfolio/blog.html', context)
def newPost_page_view(request):

    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}
    return render(request, 'portfolio/newPost.html', context)

def editar_post_page_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))


    return render(request, 'portfolio/editar.html', {'form': form, 'post_id': post_id})

def newCadeira_page_view(request):
    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:about'))
    return render(request, 'portfolio/newCadeira.html', {'form': form})

def newEscola_page_view(request):
    form = EscolaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:about'))
    return render(request, 'portfolio/newEscola.html', {'form': form})

def newCertificado_page_view(request):
    form = CertificadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:about'))
    return render(request, 'portfolio/newCertificado.html', {'form': form})

def newHabilitacao_page_view(request):
    form = HabilitacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:about'))
    return render(request, 'portfolio/newHabilitacao.html', {'form': form})

def newInteresse_page_view(request):
    form = InteresseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:about'))
    return render(request, 'portfolio/newInteresse.html', {'form': form})

def newProjeto_page_view(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))
    return render(request, 'portfolio/newProjeto.html', {'form': form})

def projeto_page_view(request, origem, projeto_id):
    projeto = Projeto.objects.get(pk=projeto_id)
    return render(request, 'portfolio/projeto.html', {
        'origem': origem,
        'projeto': projeto
    })

def login_page_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'portfolio/login.html', {
                'message': "Invalid credentials."
            })
    return render(request, "portfolio/login.html")

def logout_page_view(request):
    logout(request)
    return render(request, 'portfolio/home.html', {
        'message': "Logged Out"
    })


def resolution_path(instance, filename):
    return f'users/{instance.id}/'



