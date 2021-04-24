from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from . import forms


def contact_form(request):

    if request.method == 'POST':
        form = forms.EmailingForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            subject = form.cleaned_data["Subject"]
            email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")
            message = f"{name} said, {message}"

            # connection=get_connection('django.core.mail.backends.console.EmailBackend'))
            send_mail(subject, message, from_email=email,
                      recipient_list=[settings.EMAIL_HOST_USER])
            return redirect('success/')
    else:
        form = forms.EmailingForm()

    return render(request, "base.html", dict(form=form))


def sucessful_page(request):
    return render(request, "successpage.html")
