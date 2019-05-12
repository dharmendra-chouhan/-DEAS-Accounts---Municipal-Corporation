from django.http import HttpResponse
from django.views.generic.base import TemplateView
 
# def index(request):
#     return HttpResponse('This page shows a list of most recent posts.')
#     return render_to_response('index.html')

class HomeView(TemplateView):
    template_name = 'index.html'