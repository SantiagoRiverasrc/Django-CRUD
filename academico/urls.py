from django.urls import path
from .views import gestor_cursos,registercurse,eliminarcurse, edicioncurse, editarcurso

urlpatterns = [
    path('', gestor_cursos),
    path('registrarcurso/', registercurse),
    path('edicioncurso/<codigo>', edicioncurse),
    path('editarcurso/', editarcurso),
    path('eliminarcurso/<codigo>', eliminarcurse)
]
