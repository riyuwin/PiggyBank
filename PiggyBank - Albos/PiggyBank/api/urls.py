from django.urls import path
from .views import AccountList, AccountDetail, WithdrawList, WithdrawDetail, DepositList, DepositDetail

urlpatterns = [
    path('account/', AccountList.as_view()),
    path('account/<int:pk>/', AccountDetail.as_view()),
    path('withdraw/', WithdrawList.as_view()),
    path('withdraw/<int:pk>/', WithdrawDetail.as_view()),
    path('deposit/', DepositList.as_view()),
    path('deposit/<int:pk>/', DepositDetail.as_view()),
]