from django.shortcuts import render

# Create your views here.
from bug.models import Bug


def bug_manage(request):
    username = request.session.get('user', '')
    bugs = Bug.objects.all()
    return render(request, 'bug/bug_manage.html', {'username':username, 'bugs':bugs})
