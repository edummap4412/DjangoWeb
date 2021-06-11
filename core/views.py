from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContatoForm
from .models import ProdutosModel
from django.urls import reverse_lazy
from django.contrib import messages



class IndexView(TemplateView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['produto'] = ProdutosModel.objects.all()

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso')
        return super(IndexView,self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.success(self.request, 'Email enviado com sucesso')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)



class LeiamaisView(TemplateView):

    template_name = 'leiamais.html'
