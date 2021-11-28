from django.urls import path

from . import views

app_name = "ideas"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("<int:idea_id>", views.idea, name="idea")
]
