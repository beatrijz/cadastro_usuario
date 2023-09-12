
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsável, nome de referência
    #facebook.com
    #usuarios.com
    path ('',views.home, name = 'home'),
    path ('usuarios/', views.usuarios, name='listagem_usuarios')
    #facebook.com/devaprender
    #path ('devaprender/')
]
