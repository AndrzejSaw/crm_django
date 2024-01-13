from django.contrib import admin
from django.urls import path
from blog import views  # Импортируйте views из вашего приложения blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Добавьте эту строку для главной страницы
]

