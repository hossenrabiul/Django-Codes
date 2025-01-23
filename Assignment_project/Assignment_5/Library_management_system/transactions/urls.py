from django.contrib import admin
from django.urls import path, include
from . views import DepositMoneyView, BuyBookView, TransactionReportView
urlpatterns = [
    
    path('accounts/', DepositMoneyView.as_view(), name = 'deposit_money'),
    path('buyBook/<int:book_id>/', BuyBookView.as_view(), name = 'buy_now'),
    path('report/', TransactionReportView.as_view(), name = 'report'),
    # path('books/', include('books.urls')),
    # path('categories/', include('categories.urls')),
    # path('reviews/', include('review.urls')),
    # path('transactions/', include('transactions.urls')),
 
]