from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def home_page(request):
    return render_to_response('home.html', dict())

