from lampiran.models import Lampiran
from django.http import HttpResponse
from .forms import DocumentPasswordForm  
from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from lampiran.models import Lampiran
from crypto import AES, DES, RC4, RC4_FILES

# Create your views here.
def custom_access_denied_page(request):
    context = {}

    return render(request, 'access_denied.html', context)

def custom_decryption(encrypted_content, metode_encryption, key, pro):
    if metode_encryption == 'aes-cbc':
        decrypted_content,_,_,_ = AES.aes_cbc_de(encrypted_content, key, pro)
    elif metode_encryption == 'aes-cfb':
        decrypted_content,_,_,_ = AES.aes_cfb_de(encrypted_content, key, pro)
    elif metode_encryption == 'aes-ofb':
        decrypted_content,_,_,_ = AES.aes_ofb_de(encrypted_content, key, pro)
    elif metode_encryption == 'aes-ctr':
        decrypted_content,_,_,_ = AES.aes_ctr_de(encrypted_content, key, pro)
    elif metode_encryption == 'rc4-txt':
        decrypted_content,_,_,_ = RC4.decrypt(encrypted_content, key)
    elif metode_encryption == 'rc4-img':
        decrypted_content,_,_,_ = RC4_FILES.decrypt_image(encrypted_content, key)
    elif metode_encryption == 'des-cbc':
        decrypted_content,_,_,_ = DES.des_cbc_de(encrypted_content, key, pro)
    elif metode_encryption == 'des-cfb':
        decrypted_content,_,_,_ = DES.des_cfb_de(encrypted_content, key, pro)
    elif metode_encryption == 'des-ofb':
        decrypted_content,_,_,_ = DES.des_ofb_de(encrypted_content, key, pro)

    return decrypted_content

def download_page(request, id_dokumen):
    lampiran = get_object_or_404(Lampiran, id_lampiran=id_dokumen)

    # Check if the form has been submitted
    if request.method == 'POST':
        form = DocumentPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password_is_correct(password, id_dokumen):
                # Handle password submission here
                metode_encryption = lampiran.metode_crypto  # Get the encryption method from the Lampiran object
                # Perform custom decryption based on the encryption method
                decrypted_content,_,_,_ = custom_decryption(lampiran.dokumen_laporan, metode_encryption, lampiran.key_crypto, lampiran.pro_crypto)

                if decrypted_content is not None:
                    # Custom decryption successful, allow access and initiate download
                    response = FileResponse(decrypted_content, as_attachment=True)
                    response['Content-Disposition'] = f'attachment; filename="{lampiran.dokumen_laporan.name}"'
                    return response
                else:
                    # Custom decryption failed, display an error message
                    form.add_error('password', 'Decryption failed. Please check your password or decryption logic.')
    else:
        # If it's a GET request, display the form
        form = DocumentPasswordForm()

    context = {
        'form': form,
        'id_dokumen': id_dokumen,
    }
    return render(request, 'lampiran/download_page.html', context)

# Implement your password validation logic
def password_is_correct(password, id_dokumen):
    # key = Lampiran.objects.filter(id_lampiran = id_dokumen).values('key').first()
    # key = key['key']

    # if password == str(key):
    #     return True

    # return False 
    return True

def download_file(post_id):
    pass