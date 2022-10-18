from django.shortcuts import render
from .forms import ContactForm, Contact


def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form

    }
    return render(request, 'contact.html', context)


