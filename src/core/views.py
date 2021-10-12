from django.core.mail import send_mail
from django.shortcuts import render, reverse
from django.views import generic
from .forms import ContactForm 
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.models import Order

class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name= 'profile.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({
            "orders": Order.objects.filter(user=self.request.user, ordered=True)
        })
        return context
    


class HomeView(generic.TemplateView):
    template_name = 'index.html'

class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        messages.info(
            self.request, "Hemos recibido tu mensaje")
        name = form.cleaned_data.get('name')  #limpiando los campos
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        
        full_message = f"""
            Mensaje recibido de {name},{email}
            __________________________________


            {message}
            """  #mostrando este mensaje en consola al hacer el post request
        send_mail(
            subject="Mensaje recibido por Contact Form",
            message=full_message,
            from_email=[settings.DEFAULT_FROM_EMAIL],
            recipient_list=[settings.NOTIFY_EMAIL]
        ) #subject muestra el mensaje a la persona, y los datos son enviados a un recipiente

        return super(ContactView, self).form_valid(form)