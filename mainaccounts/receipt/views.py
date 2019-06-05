from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import Receipt
from .forms import ReceiptdetFormSet


class ReceiptList(ListView):
    model = Receipt


class ReceiptCreate(CreateView):
    model = Receipt
    fields = ['receipt_no', 'receipt_date']


class ReceiptdetCreate(CreateView):
    model = Receipt
    fields = ['receipt_no', 'receipt_date']
    success_url = reverse_lazy('receipt-list')

    def get_context_data(self, **kwargs):
        data = super(ReceiptdetCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['receiptdet'] = ReceiptdetFormSet(self.request.POST)
        else:
            data['receiptdet'] = ReceiptdetFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        Receiptdet = context['receiptdet']
        with transaction.atomic():
            self.object = form.save()

            if Receiptdet.is_valid():
                Receiptdet.instance = self.object
                Receiptdet.save()
        return super(ReceiptdetCreate, self).form_valid(form)


class ReceiptUpdate(UpdateView):
    model = Receipt
    success_url = '/'
    fields = ['receipt_no', 'receipt_date']


class ReceiptdetUpdate(UpdateView):
    model = Receipt
    fields = ['receipt_no', 'receipt_date']
    success_url = reverse_lazy('receipt-list')

    def get_context_data(self, **kwargs):
        data = super(ReceiptdetUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['Receiptdet'] = ReceiptdetFormSet(self.request.POST, instance=self.object)
        else:
            data['Receiptdet'] = ReceiptdetFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        Receiptdet = context['Receiptdet']
        with transaction.atomic():
            self.object = form.save()

            if Receiptdet.is_valid():
                Receiptdet.instance = self.object
                Receiptdet.save()
        return super(ReceiptdetUpdate, self).form_valid(form)


class ReceiptDelete(DeleteView):
    model = Receipt
    success_url = reverse_lazy('receipt-list')
