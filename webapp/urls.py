from django.urls import path

from webapp.views import calculation

urlpatterns = [
    path('subtract/', calculation),
    path('multiply/', calculation),
    path('divide/', calculation),
    path('add/', calculation),
]
