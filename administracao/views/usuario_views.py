from django.http import HttpRequest, HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from administracao.forms.usuario_forms import CadastroUsuarioForm, EditarUsuarioForm


@login_required
def cadastrar_usuario(request: HttpRequest) -> HttpResponse:
    form = CadastroUsuarioForm()

    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("listar-usuarios")

    context = {
        "form": form,
    }

    return render(request, "usuarios/form_usuario.html", context)


@login_required
def listar_usuarios(request: HttpRequest) -> HttpResponse:
    usuarios = get_user_model().objects.filter(is_superuser=True).all()

    context = {
        "usuarios": usuarios,
    }

    return render(request, "usuarios/lista_usuarios.html", context)


@login_required
def editar_usuario(request: HttpRequest, pk: int) -> HttpResponse:
    usuario = get_object_or_404(get_user_model(), pk=pk)

    form = EditarUsuarioForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()

        return redirect("listar-usuarios")

    context = {
        "form": form,
    }

    return render(request, "usuarios/form_usuario.html", context)
