from django.urls import path

from administracao.views.usuario_views import (
    cadastrar_usuario,
    editar_usuario,
    listar_usuarios,
)
from administracao.views.servico_views import (
    cadastrar_servico,
    editar_servico,
    listar_servicos,
)

servicos_urlpatterns = [
    path("servicos/cadastrar", cadastrar_servico, name="cadastrar-servico"),
    path("servicos/listar", listar_servicos, name="listar-servicos"),
    path("servicos/editar/<int:pk>", editar_servico, name="editar-servico"),
]

usuarios_urlpatterns = [
    path("usuarios/cadastrar", cadastrar_usuario, name="cadastrar-usuario"),
    path("usuarios/listar", listar_usuarios, name="listar-usuarios"),
    path("usuarios/editar/<int:pk>", editar_usuario, name="editar-usuario"),
]

urlpatterns = servicos_urlpatterns + usuarios_urlpatterns
