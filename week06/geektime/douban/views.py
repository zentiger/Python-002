from django.shortcuts import render
from .models import T1

def movies_short(request):
    # shorts = T1.objects.all()
    shorts = T1.objects.filter(n_star__gt=3)

    return render(request, 'index.html', locals())

# Create your views here.
