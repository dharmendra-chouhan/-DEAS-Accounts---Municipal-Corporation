from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector
from django.template.loader import render_to_string
from .forms import SearchForm
from django.http import JsonResponse



from .models import Vendor

class VendorCreate(CreateView):
    model = Vendor
    fields = ['vname', 'vcontact','vemail','vaddress']
    success_url = reverse_lazy('vendor:vendor_search')

class VendorList(ListView):
    model = Vendor

class VendorView(DetailView):
    model = Vendor

class VendorUpdate(UpdateView):
    model = Vendor
    fields = ['vname', 'vcontact','vemail','vaddress']
    success_url = reverse_lazy('vendor:vendor_search')

class VendorDelete(DeleteView):
    model = Vendor
    success_url = reverse_lazy("vendor:vendor_search")


def vendor_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            if query=='All':
                results = Vendor.objects.annotate(search=SearchVector('vname', 'vaddress'), )         
            else:
                results = Vendor.objects.annotate(search=SearchVector('vname', 'vaddress'), ).filter(search=query)   
    return render(request,'vendor/vendor_list.html',{'form': form,
                                                    'query': query,
                                                    'results': results})


def vendor_delete(request, pk):
    print("dharmendra")
    vendor = get_object_or_404(Vendor, pk=pk)
    data = dict()
    context = {'vendor': vendor}
    data['html_form'] = render_to_string('vendor/partial_book_delete.html', context, request=request)
    return JsonResponse({"key": "value"})