from django.conf.urls import url
from .views import signup
from django.contrib.auth import views as auth_views
from .views import success_page,UserProfileUpdate,profile
app_name ='accounts'
urlpatterns = [

    url(r'^signup/$',signup , name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^password/change/$',
        auth_views.PasswordChangeView.as_view(), {"post_change_redirect":"account:password_change_done"},
        name='password_change'),
    url(r'^password/change/done/$',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),
    url(r'^password/reset/$',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    url(r'^password/reset/done/$',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    url(r'^password/reset/\
            (?P<uidb64>[0-9A-Za-z_\-]+)/\
            (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    url(r'^password/reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
    url(r'^userprofile/update/(?P<pk>\w+)/$',
        UserProfileUpdate,
        name='user_profile_update'),
    url(r'^profile/success/$',
        success_page,
        name='success_page'),
    url(r'^profile/$',
        profile,
        name='profile_page'),
]