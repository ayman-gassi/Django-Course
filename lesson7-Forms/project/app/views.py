from django.shortcuts import redirect, render
from .forms import ContactForm

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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contactSuccess(request):
    return render(request, 'contact_success.html')