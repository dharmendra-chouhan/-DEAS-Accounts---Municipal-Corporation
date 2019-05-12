from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.postgres.search import SearchVector
from django.forms import ModelForm

from django.contrib import messages

from .forms import SearchForm,Subledger_masterForm

from .models import Subledger_master
from lookup.models import Lookup,Lookupdet
from accountcode.models import Function_master,Object_master

# Create your views here.

class subledgermasterForm(ModelForm):
    class Meta:
        model = Subledger_master
        fields = ['function_id', 'object_id','lookupdet_bug','opening_bal','lookupdet_opening_drcr','opening_bal_date','subledger_code','subledger_desc','status','budget_provion_required']


def subledger_search(request,success=None):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            if query=='All':
                results = Subledger_master.objects.annotate(search=SearchVector('subledger_code', 'subledger_desc'), )         
            else:
                results = Subledger_master.objects.annotate(search=SearchVector('subledger_code', 'subledger_desc'), ).filter(search=query)   
    return render(request,'subledger/subledger_list.html',{'form': form,
                                                    'query': query,
                                                    'results': results})



def SubledgerCreate(request, template_name='subledger/subledger_master_form.html'):  
    form = subledgermasterForm(request.POST or None)
    lookup = Lookup.objects.filter(lookupcode = 'DRCR').values('id')
    lookupdet =Lookupdet.objects.filter(lookup_id=lookup[0]['id']).values()

    functionmaster=Function_master.objects.filter(lookup=3).values('id').values()
    objectmaster=Object_master.objects.filter(lookup=7).values('id').values()

    lookupbug = Lookup.objects.filter(lookupcode = 'BUG').values('id')
    lookupdetbug =Lookupdet.objects.filter(lookup_id=lookupbug[0]['id']).values()
    lookupstu = Lookup.objects.filter(lookupcode = 'STU').values('id')
    lookupdetstu =Lookupdet.objects.filter(lookup_id=lookupstu[0]['id']).values()

    lookupbrq = Lookup.objects.filter(lookupcode = 'BRQ').values('id')
    lookupdetbrq =Lookupdet.objects.filter(lookup_id=lookupbrq[0]['id']).values()
    success = False

    if form.is_valid():
        form.save()
        success = True
        return redirect('subledger:subledger_search')
    return render(request, template_name, {'form': form,'lookupdet':lookupdet,'functionmaster':functionmaster,
    'objectmaster':objectmaster,'lookupdetbug':lookupdetbug,'lookupdetstu':lookupdetstu,'lookupdetbrq':lookupdetbrq,'success':success})


def SubledgerUpdate(request, pk, template_name='subledger/subledger_master_edit.html'):
    post = get_object_or_404(Subledger_master, pk=pk)
    form = subledgermasterForm(request.POST or None, instance=post)
    lookup = Lookup.objects.filter(lookupcode = 'DRCR').values('id')
    lookupdet =Lookupdet.objects.filter(lookup_id=lookup[0]['id']).values()
    functionmaster=Function_master.objects.filter(lookup=3).values('id').values()
    objectmaster=Object_master.objects.filter(lookup=7).values('id').values()
    lookupbug = Lookup.objects.filter(lookupcode = 'BUG').values('id')
    lookupdetbug =Lookupdet.objects.filter(lookup_id=lookupbug[0]['id']).values()
    lookupstu = Lookup.objects.filter(lookupcode = 'STU').values('id')
    lookupdetstu =Lookupdet.objects.filter(lookup_id=lookupstu[0]['id']).values()
    lookupbrq = Lookup.objects.filter(lookupcode = 'BRQ').values('id')
    lookupdetbrq =Lookupdet.objects.filter(lookup_id=lookupbrq[0]['id']).values()
    if form.is_valid():
        form.save()
        return redirect('subledger:subledger_search',success)
    return render(request, template_name, {'form': form,'lookupdet':lookupdet,'functionmaster':functionmaster,
                    'objectmaster':objectmaster,'lookupdetbug':lookupdetbug,'lookupdetstu':lookupdetstu,'lookupdetbrq':lookupdetbrq})


def SubledgerDelete(request, pk, template_name='subledger/subledger_master_confirm_delete.html'):
    post = get_object_or_404(Subledger_master, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('subledger:subledger_search')
    return render(request, template_name, {'object': post})


def Subledger_master_delete(request, pk):
    post = get_object_or_404(Subledger_master, pk=pk)
    data = dict()
    context = {'post': post}
    data['html_form'] = render_to_string('subledger/partial_book_delete.html', context, request=request)
    return JsonResponse(data)