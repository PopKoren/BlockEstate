from django.urls import include, path
from api import admin, views   # Change this line
from django.contrib import admin


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
    path('user/', views.user_info, name='user-info'),
    path('user/update/', views.user_update, name='user-update'),
    path('user/change-password/', views.change_password, name='change-password'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), 
]