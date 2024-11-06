from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse
from .models import Contact, ContactMe
from .forms import ContactForm, ProfileEditForm
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.views import View
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'phonebook/home.html', {})


@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user= request.user).order_by('name')
    paginator = Paginator(contacts, 8)
    
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    
    context = {'contacts' : contacts, 'page_obj': page_pbj}
    return render(request, 'phonebook/contact_list.html', context)


# Save the new contact
@login_required
def new_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect(reverse('contact-list'))
        
    else:
        form = ContactForm()
        
    context = {'forms': form }
    return render(request, 'phonebook/add_contact.html', context=context)


# Edit the conatct information
@login_required
def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user = request.user)
    
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact-detail', pk = contact.pk)
    else:
        form = ContactForm(instance = contact)
            
    context = {'form': form, 'contact': contact}
    
    return render(request, 'phonebook/update_contact.html', context)


# After clicking the it will show all the datails related to it
@login_required
def contact_detail(request, pk):
    person = get_object_or_404(Contact, pk=pk, user=request.user)
    
    
    context = {'person' : person}
    print(person.name, person.job, person.email)
    return render(request, 'phonebook/contact_details.html', context)




# Delete the contact
@login_required
def delete_contact(request, pk):
    entry = get_object_or_404(Contact, pk=pk, user = request.user)
    print(f'This contact {entry} has been deleted')
    entry.delete()
    return redirect(reverse('contact-list'))



# Profile Page
@login_required
def profile(request):
    # contact = get_object_or_404(Contact, pk=pk, user= request.user)
    context = {'context': request.user}
    return render(request, 'phonebook/profile.html', context)


# Edit the profile section
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance = request.user)
        
    return render(request, 'phonebook/edit_profile.html', {'form': form})
        



# Views to take the Contact me html
class ContactView(View):
    def get(self, request):
        return render(request, 'phonebook/contact_me.html')
    
    def post(self, request):
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
            
        # Checks if fields are empty
        if not name or not email or not message:
            message.error(request, _("All fields are required."))
            return render(request, "phonebook/contact_me.html")
        
        # Validate email    
        try:
             validate_email(email)
        except ValidationError:
            messages.error(request, ("Invalid email address"))
            return render(request, "phonebook/contact_me.html")
            
        # Sending email
        try:
            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=f"from {email}: {message} ",
                from_email=email,
                recipient_list= ['akshatraj2607@gmail.com'],
                fail_silently=False
            )
                
            messages.success(request, _("Your message has been sent successfully!"))
            return redirect('contact')
        except Exception as e:
            messages.error(request, _("An error occured while sending your message. Please try again."))
            return render(request, "phonebook/contact_me.html")
            

# Contact Us
class ContactUs(View):
    def get(self, request):
        return render(request, 'phonebook/contact_me.html')

    def post(self, request):
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
            
        # Checks if fields are empty
        if not name or not email or not message:
            messages.error(request, _("All fields are required."))
            return render(request, "phonebook/contact_me.html")
        
        # Validate email    
        try:
             validate_email(email)
        except ValidationError:
            messages.error(request, ("Invalid email address"))
            return render(request, "phonebook/contact_me.html")
        
        
        # Save the Data
        
        try:
            # Save to the database
            new_message = ContactMe(name = name,email =  email, message = message)
            new_message.save()
            messages.success(request, ("Message sent succussfully!"))
            return redirect('contact')
        except Exception as e:
            messages.error(request, f"An Error occured while sending your message : {str(e)}")
            return redirect('contact')
        
        
# About me section
def about_me(request):
    return render(request, 'phonebook/about_me.html')