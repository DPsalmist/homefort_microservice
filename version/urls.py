from django.urls import path
from .views import AppVersionList, AppVersionCreate, AppVersionDetail

urlpatterns = [
	path('', AppVersionList.as_view(), name='app-list'),
	path('create/', AppVersionCreate.as_view(), name='app-create'),
	path('update/<str:pk>/', AppVersionDetail.as_view(), name='app-detail'),
]