from django.contrib import admin
from django.urls import path
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/hello/', views.print_hello),
    path('api/v1/Movie/', views.Movie_list_view),
    path('api/v1/Movie/<int:id>/', views.Movie_item_view),
    path('api/v1/Movie/Reviews/',views.Reviews_list_view)
]
