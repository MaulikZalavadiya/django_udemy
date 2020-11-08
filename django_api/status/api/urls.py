# from django.conf.urls import path
from django.urls import path
from .views import (
    StatusAPIView,
    # StatusCreateAPIView,
    # StatusDetailAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView,
)

urlpatterns =[
    path('',StatusAPIView.as_view()),  
    # path('create/',StatusCreateAPIView.as_view()),
    # path('<pk>/',StatusDetailAPIView.as_view()),
    # path('<int:pk>/update/',StatusUpdateAPIView.as_view()),
    # path('<int:pk>/delete/',StatusDeleteAPIView.as_view()),

] 


#/api/status -> list
#/api/status/create -> Create
#/api/status/12/ -> Details
#/api/status/12/Update/ -> update
#/api/status/12/delete/ -> Delete