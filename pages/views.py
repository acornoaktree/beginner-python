from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse(request.build_absolute_uri())

# Create your views here.
