from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Transaction
from . forms import DepositForm
from . constants import DEPOSIT,PARCHASED
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.core.mail import EmailMessage, EmailMultiAlternatives
from books.models import BooksDetails
from django.template.loader import render_to_string
# Create your views here.

def send_transaction_email(user, amount, subject, template):
        mail_subject = subject
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        to_email = user.email
        send_email = EmailMultiAlternatives(mail_subject, '', to=[to_email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()
     

class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name =  'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transactions/transaction_report.html')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'profile' : self.request.user.profile
        })
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title' : self.title
        })
        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'

    def get_initial(self):
        initial = {'transaction_type' : DEPOSIT}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount') # user je tk ta deposit krtece seta nelam
        profile = self.request.user.profile
        profile.amount += amount
        profile.save(
            update_fields = ['amount']
        ) 
        messages.success(self.request, f'{amount}$ was deposited to your account successfully ')

        # email send krteci jei user tk deposit krce
        send_transaction_email(self.request.user, amount, "deposit message", 'transactions/deposit_email.html')
        return super().form_valid(form)
    

class BuyBookView(TransactionCreateMixin,View):
    def get(self, request, book_id):
        book = get_object_or_404(BooksDetails, id=book_id)
 
        profile = request.user.profile
        user_balance = profile.amount
 
        if user_balance >= book.borrowing_price: 
            profile.amount -= book.borrowing_price
            profile.save() 
            Transaction.objects.create(
                profile=profile,
                book = book,
                amount = book.borrowing_price,
                balance_after_transactions = profile.amount,
                transaction_type = PARCHASED,
            ) 
            messages.success(request, f'You have successfully purchased "{book.title}". Tk: {book.borrowing_price}') 
            send_transaction_email(self.request.user, book.borrowing_price, "deposit message", 'transactions/deposit_email.html')
            return redirect('details', id=book_id) 
        else: 
            messages.error(request, 'The price of this book is {book.borrowing_price}, But you have {profile.amount}.')
            return redirect('details', id=book_id) 
        

class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = 'transactions/transaction_report.html'
    model = Transaction
    balance = 0
    context_object_name = 'report_list'

    def get_queryset(self):
        queryset = super().get_queryset().filter(   # user er sokol data ekhane store krlam
            profile = self.request.user.profile
        )

        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            start_date_str and end_date_str #ei duitake datetime input ee convert korlam
            datetime.strptime(' ' ,"%Y-%m-%d").date()  #eti akti built in funtion
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

            queryset = queryset.filter(timestamp__date__gte = start_date, timestamp__date__lte = end_date)

            self.balance =  Transaction.objects.filter(timestamp__date__gte = start_date, timestamp__date__lte = end_date).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.profile.amount
        
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'profile' : self.request.user.profile
        })
        return context