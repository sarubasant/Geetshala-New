from django.urls import path
# from songs import views
from .views import song_list,songsDetail


urlpatterns = [
    path('', song_list, name='song_list'),
    path('<int:id>/',songsDetail),
]

