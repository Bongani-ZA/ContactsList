from django.shortcuts import render, redirect
from .models import Contact

def home(request):
    contacts = Contact.objects.all()

    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ""
    return render(request, 'home.html', {'contacts': contacts, 'search_input': search_input})


def add_contact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name = request.POST['full_name'],
            relationship = request.POST['relationship'],
            email = request.POST['email'],
            phone_number = request.POST['phone_number'],
            address = request.POST['address']
        )
        new_contact.save()
        return redirect('home')
    return render(request, 'add.html')


def edit_contact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['full_name']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone_number']
        contact.address = request.POST['address']
        contact.save()
        return redirect('/contact-edited/' + str(contact.id))
    
    return render(request, 'edit.html', {'contact': contact})


def contact_edited(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contact-edited.html', {'contact': contact})


def delete_contact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method =='POST':
        contact.delete()
        return redirect('contact-deleted')
    
    return render(request, 'delete.html', {'contact': contact})


def contact_deleted(request):
    return render(request, 'contact-deleted.html')


def contact_profile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact': contact})

