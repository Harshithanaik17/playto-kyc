from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from kyc.views import *

def home(request):
    return HttpResponse("KYC API Running 🚀")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/v1/kyc/', KYCView.as_view()),
    path('api/v1/state/<int:id>/', ChangeStateView.as_view()),
    path('api/v1/queue/', QueueView.as_view()),
]