from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .models import Insta
# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        
        context = {
            'user': username,
            
                   }
        Insta.objects.create(username=username)
        return render(request, 'login/authenticated.html')
    return render(request, 'login/index.html')
