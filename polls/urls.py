from django.urls import path

# Para chamar a view, precisamos mapeá-la para uma URL - e para isso precisamos de um URLconf.
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]