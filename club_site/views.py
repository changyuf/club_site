from django.shortcuts import render
from club_admin.models import Activity
from django.http import HttpResponse

# Create your views here.


def home(request):
    next_3_activities = Activity.objects.order_by("-start_time")[:5]
    context = {'activities': next_3_activities}
    return render(request, 'club_site/home.html', context)

