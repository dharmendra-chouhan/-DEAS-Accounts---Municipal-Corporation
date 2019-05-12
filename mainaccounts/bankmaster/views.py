from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector

from .forms import SearchForm
from .models import Bankmaster

class BankmasterCreate(CreateView):
    model = Bankmaster
    fields = ['bankcode', 'bankname','branch','bankaddress']
    success_url = reverse_lazy('bankmaster:bankmaster_search')

class BankmasterList(ListView):
    model = Bankmaster

class BankmasterView(DetailView):
    model = Bankmaster

class BankmasterUpdate(UpdateView):
    model = Bankmaster
    fields =['bankcode', 'bankname','branch','bankaddress']
    success_url = reverse_lazy('bankmaster:bankmaster_search')

class BankmasterDelete(DeleteView):
    model = Bankmaster
    success_url = reverse_lazy("bankmaster:bankmaster_search")


def bankmaster_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            if query=='All':
                results = Bankmaster.objects.annotate(search=SearchVector('bankname', 'branch'), )         
            else:
                results = Bankmaster.objects.annotate(search=SearchVector('bankname', 'branch'), ).filter(search=query)   
    return render(request,'bankmaster/bankmaster_list.html',{'form': form,
                                                    'query': query,
                                                    'results': results})