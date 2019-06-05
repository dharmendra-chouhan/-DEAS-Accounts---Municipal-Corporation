from django.forms import ModelForm, inlineformset_factory

from .models import Receipt, Receiptdet


class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        exclude = ()


class ReceiptdetForm(ModelForm):
    class Meta:
        model = Receiptdet
        exclude = ()


ReceiptdetFormSet = inlineformset_factory(Receipt, Receiptdet,
                                            form=ReceiptdetForm, extra=1)
