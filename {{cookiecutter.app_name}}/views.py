from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import {{ cookiecutter.model_name }}Form
from .models import {{ cookiecutter.model_name }}


class {{ cookiecutter.model_name }}CRUDView(object):
    model = {{ cookiecutter.model_name }}
    queryset = {{ cookiecutter.model_name }}.objects.all()
    form_class = {{ cookiecutter.model_name }}Form
    paginate_by = 20
    action = None

    def form_valid(self, form):
        self.object = form.save()
        if self.action:
            messages.info(self.request, '{{ cookiecutter.model_name }} {0}.'.format(self.action))
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('{{ cookiecutter.model_name|lower }}:list')


class {{ cookiecutter.model_name }}List({{ cookiecutter.model_name }}CRUDView, ListView):
    pass


class {{ cookiecutter.model_name }}Create({{ cookiecutter.model_name }}CRUDView, CreateView):
    action = "created"


class {{ cookiecutter.model_name }}Detail({{ cookiecutter.model_name }}CRUDView, DetailView):
    pass


class {{ cookiecutter.model_name }}Update({{ cookiecutter.model_name }}CRUDView, UpdateView):
    action = "updated"


class {{ cookiecutter.model_name }}Delete({{ cookiecutter.model_name }}CRUDView, DeleteView):
    action = "deleted"
