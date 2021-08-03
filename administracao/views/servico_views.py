from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required

from administracao.forms.servico_forms import ServicoForm
from administracao.models import Servico


@login_required
def cadastrar_servico(request: HttpRequest) -> HttpResponse:
    form = ServicoForm()

    if request.method == "POST":
        form = ServicoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("listar-servicos")

    context = {
        "form": form,
    }

    return render(request, "servicos/form_servico.html", context)


@login_required
def listar_servicos(request: HttpRequest) -> HttpResponse:
    servicos = Servico.objects.all()

    context = {
        "servicos": servicos,
    }

    return render(request, "servicos/listar_servicos.html", context)


@login_required
def editar_servico(request: HttpRequest, pk: int) -> HttpResponse:
    servico = get_object_or_404(Servico, pk=pk)

    form = ServicoForm(request.POST or None, instance=servico)

    if form.is_valid():
        form.save()

        return redirect("listar-servicos")

    context = {
        "form": form,
    }

    return render(request, "servicos/form_servico.html", context)
