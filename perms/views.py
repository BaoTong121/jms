from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import DeleteView, ListView, UpdateView, CreateView, DetailView, View
from django.views.generic.edit import SingleObjectMixin
from django.urls import reverse_lazy
from users.mixins import LoginRequiredMixin
from .models import Perms
from .forms import PermsForm




class PermsListView(LoginRequiredMixin, ListView):
    model = Perms
    template_name = 'perms/list.html'
    form = PermsForm()


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PermsListView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

class PermsCreateView(LoginRequiredMixin, CreateView):
    model = Perms
    form_class = PermsForm
    success_url = reverse_lazy('perms/list.html')

    def get(self, request, *args, **kwargs):
        return HttpResponse("Method not support", status=405)
    def form_invalid(self, form):
        return HttpResponse(";".join(form.errors), status=400)



class PermDetailView(DetailView):
    model = Perms
    template_name = "perms/detail.html"


class PermDeleteView(SingleObjectMixin, View):
    model = Perms

    def post(self, request, *args, **kwargs):
        perm = self.get_object()
        perm.delete()
        return HttpResponse("删除成功")

