from django.http import HttpRequest, HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render

from administracao.forms.usuario_forms import UsuarioForm


def cadastrar_usuario(request: HttpRequest) -> HttpResponse:
    form = UsuarioForm()

    if request.method == "POST":
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("listar-usuarios")

    context = {
        "form": form,
    }

    return render(request, "usuarios/form_usuario.html", context)


def listar_usuarios(request: HttpRequest) -> HttpResponse:
    usuarios = get_user_model().objects.filter(is_superuser=True).all()

    context = {
        "usuarios": usuarios,
    }

    return render(request, "usuarios/lista_usuarios.html", context)
