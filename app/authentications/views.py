from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group

from .forms import UserCreationForm


class SigninView(LoginView):
    def get_success_url(self):
        role = self.request.user.get_role_display()
        url = "/page/{}".format(role)
        return url


class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super(SignupView, self).form_valid(form)
        role = form.instance.get_role_display()
        group, created = Group.objects.get_or_create(name=role)
        group.user_set.add(self.object)
        return response  


class LogoutView(generic.RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/accounts/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)