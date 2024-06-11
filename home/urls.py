from django.urls import path
from . import views
from . import viewsTwo
from . import viewsThree
from . import viewsTwo


urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la vista index en views.py
    path('section14/', views.section14, name='section14'),  # Ruta para la vista section14 en viewsTwo.py
    path('section15/', viewsTwo.section15, name='section15'),
    path('section16/', viewsThree.section16, name='section16'),  # Ruta para la vista section16 en viewsThree.py
    # Otras rutas...
]
