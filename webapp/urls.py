from django.urls import path

from webapp.views import calculation, index_view

urlpatterns = [
    path('', index_view),
    path('subtract/', calculation),
    path('multiply/', calculation),
    path('divide/', calculation),
    path('add/', calculation),
]
