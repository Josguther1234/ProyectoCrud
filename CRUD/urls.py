from django.urls import path
from views import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index = name='index'),
]
