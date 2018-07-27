from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from app.models import AppCase, AppCaseStep


@login_required
def app_case_manage(request):
    app_cases = AppCase.objects.all()
    user = request.session.get('user', '')
    return render(request, 'apptest/app_case_manage.html', {'appcases': app_cases, 'user': user})


@login_required
def app_case_step_manage(request):
    app_step_cases = AppCaseStep.objects.all()
    user = request.session.get('user', '')
    return render(request, 'apptest/app_case_step_manage.html', {'app_case_steps': app_step_cases, 'user': user})