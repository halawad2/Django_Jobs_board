
from django.urls import path
from . import views
urlpatterns = [
    path('', views.job_list, name='list'),
    path('<int:id >', views.job_detail, name='detail'),
]
