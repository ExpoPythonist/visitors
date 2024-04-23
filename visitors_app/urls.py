from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.home, name="home-page"),
                  path('login', views.login_page, name='login-page'),
                  path('register', views.userregister, name='register-page'),
                  path('save_register', views.save_register, name='register-user'),
                  path('user_login', views.login_user, name='login-user'),
                  path('home', views.home, name='home-page'),
                  path('logout', views.logout_user, name='logout'),
                  path('profile', views.profile, name='profile-page'),
                  path('update_password', views.update_password, name='update-password'),
                  path('update_profile', views.update_profile, name='update-profile'),
                  path('departments', views.departments, name='department-page'),
                  path('manage_department', views.manage_department, name='manage-department'),
                  path('manage_department/<int:pk>', views.manage_department, name='manage-department-pk'),
                  path('save_department', views.save_department, name='save-department'),
                  path('delete_department/<int:pk>', views.delete_department, name='delete-department'),
                  path('users', views.users, name='user-page'),
                  path('manage_user', views.manage_user, name='manage-user'),
                  path('manage_user/<int:pk>', views.manage_user, name='manage-user-pk'),
                  path('save_user', views.save_user, name='save-user'),
                  path('delete_user/<int:pk>', views.delete_user, name='delete-user'),
                  path('visitors', views.visitors, name='visitor-page'),
                  path('manage_visitor', views.manage_visitor, name='manage-visitor'),
                  path('view_visitor/<int:pk>', views.view_visitor, name='view-visitor-pk'),
                  path('manage_visitor/<int:pk>', views.manage_visitor, name='manage-visitor-pk'),
                  path('save_visitor', views.save_visitor, name='save-visitor'),
                  path('delete_visitor/<int:pk>', views.delete_visitor, name='delete-visitor'),
                  path('report', views.report, name='report-page'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
