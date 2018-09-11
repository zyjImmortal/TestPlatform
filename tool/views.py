from django.shortcuts import render

# Create your views here.
from product.models import Env, Version
from api.models import Api


def tool_index(request):
    envs = Env.objects.all()
    version = Version.objects.first()
    return render(request, 'tool/home.html', {'envs': envs, 'version': version, 'nav_active': 'tool'})
