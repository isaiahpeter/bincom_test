from django.urls import path
from .views import GetPollResultView,ResultSumTotalView,UploadPostResult


urlpatterns = [
    path('',GetPollResultView.as_view(),name='poll_result'),
    path('result',ResultSumTotalView.as_view(),name='result'),
    path('add_result',UploadPostResult.as_view(),name='add_result'),
    ]