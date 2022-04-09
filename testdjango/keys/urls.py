from django.urls import path, include
from keys import views
from .views import helloAPI, Random_Recommand_Theme, Show_Theme, Show_Er

app_name = 'keys'

urlpatterns = [
    path("api/hello/", helloAPI),
    path("api/home/<int:id>/",Random_Recommand_Theme),
    path("api/th/<int:id>/", Show_Theme),
    path("api/er/<int:id>/", Show_Er),
    path("thimg/<int:id>", views.image, name='image'),
]