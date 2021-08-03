from django.urls import path
from django.urls.base import reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)

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

auth_urlpatterns = [
    path("autenticacao/login", LoginView.as_view(), name="login"),
    path("autenticacao/logout", LogoutView.as_view(), name="logout"),
    path(
        "alterar_senha",
        PasswordChangeView.as_view(success_url=reverse_lazy("listar-servicos")),
        name="alterar-senha",
    ),
    path("resetar_senha", PasswordResetView.as_view(), name="resetar-senha"),
    path(
        "resetar_senha/sucesso",
        PasswordResetDoneView.as_view(),
        name="resetar-senha-sucesso",
    ),
    path(
        "resetar_senha/<str:uidb64>/<str:token>",
        PasswordResetConfirmView.as_view(),
        name="resetar-senha-confirmar",
    ),
    path(
        "resetar_senha/feito",
        PasswordResetDoneView.as_view(),
        name="resetar-senha-feito",
    ),
]

urlpatterns = servicos_urlpatterns + usuarios_urlpatterns + auth_urlpatterns
