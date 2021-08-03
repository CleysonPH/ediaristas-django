from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from administracao.forms.usuario_forms import UsuarioForm


def cadastrar_usuario(request: HttpRequest) -> HttpResponse:
    form = UsuarioForm()

    if request.method == "POST":
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()

    context = {
        "form": form,
    }

    return render(request, "usuarios/form_usuario.html", context)
