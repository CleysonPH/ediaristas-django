from django.urls import path

from .views import cadastrar_servico, editar_servico, listar_servicos


urlpatterns = [
    path("servicos/cadastrar", cadastrar_servico, name="cadastrar-servico"),
    path("servicos/listar", listar_servicos, name="listar-servicos"),
    path("servicos/editar/<int:pk>", editar_servico, name="editar-servico"),
]
