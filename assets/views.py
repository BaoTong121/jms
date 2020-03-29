from django.shortcuts import render
from django.shortcuts import get_object_or_404, HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, View
from django.urls import reverse_lazy

from .forms import AssetsFrom
from .models import Assets
from users.mixins import LoginRequiredMixin

class AssetsListView(LoginRequiredMixin, ListView):
    model = Assets
    context_object_name = 'assets'
    template_name = 'assets/list.html'

class AssetsCreateView(LoginRequiredMixin, CreateView):
    model = Assets
    form_class = AssetsFrom
    template_name = "assets/add.html"
    success_url = reverse_lazy("assets:list")

class AssetsDetailView(LoginRequiredMixin, DetailView):
    model = Assets
    template_name = "assets/detail.html"

class AssetsUpdateView(LoginRequiredMixin, UpdateView):
    model = Assets
    form_class = AssetsFrom
    template_name = "assets/update.html"
    success_url = reverse_lazy("assets:list")


class AssetsDelView(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        print(args, kwargs)
        asset_id = self.kwargs.get("pk", 0)
        print(asset_id)
        asset = get_object_or_404(Assets, id=asset_id)
        asset.delete()
        return HttpResponse("删除成功")

# Create your views here.
