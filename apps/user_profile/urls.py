from django.conf.urls import url

from apps.user_profile.views import (
    get_users_by_gender,
    UserProfileDetailView,
    RegisterFormView,
    UserPageView,
    change_password)
from final_project.views import MainPageView

urlpatterns = [
    url(r'^/', UserProfileDetailView.as_view()),
    url(r'^register/$', RegisterFormView.as_view()),
    url(r'^(?P<gender>[a-zA-Z]+)$', get_users_by_gender),
    url(r'^register/$', RegisterFormView.as_view(), name="register"),
    url(r'^$', MainPageView.as_view(), name="main"),
    #url(r'^register_child$', child_form),
    url(r'^profile_page/(?P<pk>[0-9]+)$', UserPageView.as_view(), name='user-page'),
    url(r'^change_password$', change_password, name='change_password'),


]