from django.urls import path
from django.urls.resolvers import URLPattern

from .views import todo_list, todo_details, todo_create, todo_update, todo_delete

app_name = 'todos'

urlpatterns = [
    path('', todo_list),
    path('create/', todo_create),
    path('<id>/', todo_details),
    path('<id>/update/', todo_update),
    path('<id>/delete/', todo_delete),
]
