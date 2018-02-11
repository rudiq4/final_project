# Create your views here.
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from apps.user_profile.models import UserProfile


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'main_page/main_content.html'


def get_user_profile(request, user_id=None):
    user_profile = get_object_or_404(UserProfile, pk=user_id)

    if user_profile:
        res = "<h1 align='center'>{}</h1>".format(
            user_profile.user.get_full_name()
        )
        return HttpResponse(res)
    else:
        return HttpResponse("<h1 align='center'>Not found</h1>")


def get_users_by_gender(request, gender):
    user = UserProfile.objects.filter(sex=gender).last()
    res = "<h1 align='center'>{}</h1>".format(
        user.user.get_full_name()
    )
    return HttpResponse(res)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = "main_page/register.html"
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class UserPageView(DetailView):
    template_name = 'user_page.html'
    model = UserProfile


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['users'] = User.objects.all()

        return context

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form })
