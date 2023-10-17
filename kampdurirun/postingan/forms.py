from django import forms
from .models import Postingan
from lampiran.models import Lampiran

class PostinganLampiranForm(forms.ModelForm):
    # Fields for Lampiran model
    jenis_lampiran = forms.ChoiceField(
        label='Jenis Lampiran',
        choices=Lampiran.JENIS_LAMPIRAN_CHOICES,
        required=True
    )
    dokumen_laporan = forms.FileField(
        label='Dokumen Lampiran',
        required=False
    )
    metode_crypto = forms.ChoiceField(
        label='Metode Enkripsi',
        choices=Lampiran.METODE_CRYPTO_CHOICES,
        required=False
    )
    
    user_email_user = forms.CharField(
        widget=forms.HiddenInput(),  # This field will be hidden in the form
        required=False  # Since it's hidden, it can be optional
    )

    class Meta:
        model = Postingan
        fields = ['judul', 'deskripsi']
