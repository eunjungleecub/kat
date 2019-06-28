from django.urls import path
from promotion.views import MainView, InfoView

urlpatterns = [

    path('info/', InfoView.as_view(), name='info'),
# main.html defined in katharsis/urls.py
    
    
]
