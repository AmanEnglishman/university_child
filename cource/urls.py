from django.urls import path

from .views import ClassesListView

urlpatterns = [
    path('', ClassesListView.as_view(), name='classes_list'),
]
