from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from api.models import ApiTestCase, ApiStep, Api


@login_required
def api_test_manage(request):
    api_tests = ApiTestCase.objects.all()
    username = request.session.get('user', '')
    return render(request, 'apitest/apitest_manage.html', {'apitests': api_tests, 'user': username})


@login_required
def api_step_manage(request):
    api_steps = ApiStep.objects.all()
    username = request.session.get('user', '')
    return render(request, 'apitest/apitest_manage.html', {'apisteps': api_steps, 'user': username})


def api_manage(request):
    apis = Api.objects.all()
    username = request.session.get('user', '')
    return render(request, 'apitest/api_manage.html', {'apis': apis, 'user': username})
