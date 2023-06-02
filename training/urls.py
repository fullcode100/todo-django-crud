from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('todo/', include("my_todo.urls")),
    # path('admin/', admin.site.urls),
]
