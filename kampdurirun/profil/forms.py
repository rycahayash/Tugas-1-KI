from django import forms
from profil.models import Profil

class ProfilEditForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = [
            'informasi_kesehatan',
            'tinggi_badan',
            'berat_badan',
            'golongan_darah',
            'catatan_kejahatan',
            'nama_user',
            'jenis_kelamin',
            'kewarganegaraan',
            'agama',
            'is_kawin',
            'gambar',
        ]
        
class ProfilCreateForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = [
            'informasi_kesehatan',
            'tinggi_badan',
            'berat_badan',
            'golongan_darah',
            'catatan_kejahatan',
            'nama_user',
            'jenis_kelamin',
            'kewarganegaraan',
            'agama',
            'is_kawin',
            'gambar',
        ]
