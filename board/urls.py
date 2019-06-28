from django.urls import path
from board.views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('posts/', ListView.as_view(), name='posts_list'),
    path('<int:pk>/', DetailView.as_view(), name='detail_post'),
    path('create/', CreateView.as_view(), name='create_post'),
    path('update/', UpdateView.as_view(), name='update_post'),
    path('deleate/', DeleteView.as_view(), name='delete_post'),    
]
