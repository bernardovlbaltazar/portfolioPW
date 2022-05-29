from django.urls import path
from . import views

app_name = "portfolio"

name = 'home'
urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about', views.about_page_view, name='about'),
    path('competencias', views.competencias_page_view, name='competencias'),
    path('formacao', views.formacao_page_view, name='formacao'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('contact', views.contact_page_view, name='contact'),
    path('blog', views.blog_page_view, name='blog'),
    path('newpost', views.newPost_page_view, name='newpost'),
    path('editar/<int:post_id>', views.editar_post_page_view, name='editar'),
    path('newcadeira', views.newCadeira_page_view, name='newcadeira'),
    path('newescola', views.newEscola_page_view, name='newescola'),
    path('newcertificado', views.newCertificado_page_view, name='newcertificado'),
    path('newhabilitacao', views.newHabilitacao_page_view, name='newhabilitacao'),
    path('newinteresse', views.newInteresse_page_view, name='newinteresse'),
    path('newprojeto', views.newProjeto_page_view, name='newprojeto'),
    path('<str:origem>/projetos/<int:projeto_id>', views.projeto_page_view, name='projeto'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),

]
