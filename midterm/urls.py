from django.urls import path
from midterm import views

# Declare a namespace for this APP
app_name = 'midterm'

urlpatterns = [
    # For home
    path('', views.home, name='home'),
    # For Ajax
    path('api_get_cate_topword/', views.api_get_cate_topword),
]
