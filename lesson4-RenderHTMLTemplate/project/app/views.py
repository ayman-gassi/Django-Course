from django.shortcuts import render

# Create your views here.
def index(request):
    User = [{
        'name': 'John Doe',
        'email': '',
        'phone': '',
    } , {
        'name': 'Jane Doe',
        'email': '',
        'phone': '',
    }]
    context = {'users': User}
    return render(request, 'index.html' , context)
