from django.urls import include, path
from perevalapi import views




urlpatterns = [
    path('records/', views.RecordViewSet.as_view({'post': 'submitData'})),
    # path('api-auth/', include('rest_framework.urls')),
]