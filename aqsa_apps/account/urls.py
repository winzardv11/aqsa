# Author of Aqsa: Yulay Musin
from django.conf.urls import url, include
from . import views_before_login as before
from . import views_after_login as after


before_login_urlpatterns = [
    # Before login successfully. Templates in the "templates/registration". The urls without namespace.
    url(r'^signup$', before.signup, name='signup'),
    url(r'^', include('django.contrib.auth.urls')),
    # account/login/					[name='login']
    # account/logout/					[name='logout']
    # account/password_change/			[name='password_change']  # not available because admin URI not turned on
    # account/password_change/done/		[name='password_change_done']  # not available because admin URI not turned on
    # account/password_reset/			[name='password_reset']
    # account/password_reset/done/		[name='password_reset_done']
    # account/reset/<uidb64>/<token>/	[name='password_reset_confirm']
    # account/reset/done/				[name='password_reset_complete']
]
after_login_urlpatterns = [
    # After login successfully. Templates in the "templates/account". The urls with 'account' namespace.
    url(r'^change_password$', after.change_password, name='change_password'),
    url(r'^update_account$', after.update_account, name='update_account'),
    url(r'^delete_account/$', after.DeleteAccount.as_view(), name='delete_account'),
    url(r'^account_deleted$', after.AccountDeleted.as_view(), name='account_deleted'),
]
