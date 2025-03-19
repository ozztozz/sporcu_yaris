from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('login/', views.user_login, name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('password-change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
path('register/', views.register, name='register'),
path('', views.dashboard, name='dashboard'),
path('basvuru/<int:id>', views.dashboard, name='basvuru_detail'),

path('blog_list/', views.blog_list, name='account_blog_list'),
path('create_post/', views.blog_ekle, name='create_post'),
path('update_post/<slug:slug>/', views.blog_update, name='update_post'),

path('antrenor_list/', views.antrenor_list, name='antrenor_list'),
path('create_antrenor/', views.antrenor_ekle, name='create_antrenor'),
path('update_antrenor/<int:id>/', views.antrenor_update, name='update_antrenor'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)