from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("idea/<int:idea_id>/", views.idea, name="idea")
]
