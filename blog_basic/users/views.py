from django.shortcuts import render
from .models import VyasProfile


def profile(request):
    context = {
        'things': VyasProfile.objects.all()
    }

    return render(request, 'users/profile.html', context)



