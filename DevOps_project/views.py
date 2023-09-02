# userapp/views.py

from django.http import JsonResponse

from DevOps_project.utils import VisitCounter
from .models import Person


def get_people(request):
    users = Person.objects.all()
    user_data = [
        {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        for user in users
    ]
    return JsonResponse(user_data, safe=False)


def get_visit_count(request):
    
    counter = VisitCounter()
    counter.increment()
    count = counter.get_count()
    return JsonResponse({'visit_count': count})