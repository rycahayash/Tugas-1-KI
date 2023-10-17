from django.shortcuts import render, redirect
from postingan.models import Postingan
from lampiran.models import Lampiran
from postingan.forms import PostinganLampiranForm
from django.utils import timezone
from crypto import AES, DES, RC4, RC4_FILES

# Create your views here.
def postingan_list(request):
    postingan_list = Postingan.objects.all()
    context = {
        'postingan_list': postingan_list
    }
    return render(request, 'postingan/all_post.html', context)

def create_postingan(request):
    if request.method == 'POST':
        form = PostinganLampiranForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a Lampiran instance
            lampiran = Lampiran(
                jenis_lampiran=form.cleaned_data['jenis_lampiran'],
                metode_crypto=form.cleaned_data['metode_crypto'],
            )
            lampiran.save()

            # with open(lampiran.dokumen.url, 'rb') as image_file:
            #     file_content = image_file.read()
            uploaded_file = form.cleaned_data['dokumen_laporan']
            uploaded_file.open()  # Open the file
            file_content = uploaded_file.read()  # Read the content as bytes
            uploaded_file.close()  # Close the file

            # Encrypt the dokumen_laporan field based on the selected method
            key = str(lampiran.key_crypto)
            key = bytes.fromhex(key)
            pro = str(lampiran.pro_crypto)
            pro = bytes.fromhex(pro)

            if form.cleaned_data['metode_crypto'] == 'aes-cbc':
                encrypted_dokumen, _, _, _ = AES.aes_cbc_en(file_content, key, pro)
            elif form.cleaned_data['metode_crypto'] == 'aes-cfb':
                encrypted_dokumen, _, _, _ = AES.aes_cfb_en(file_content, key, pro)
            elif form.cleaned_data['metode_crypto'] == 'aes-ofb':
                encrypted_dokumen, _, _, _ = AES.aes_ofb_en(file_content, key, pro)
            elif form.cleaned_data['metode_crypto'] == 'aes-ctr':
                encrypted_dokumen, _, _, _ = AES.aes_ctr_en(file_content, key, pro)
            elif form.cleaned_data['metode_crypto'] == 'rc4-txt':
                encrypted_dokumen, _, _, _ = RC4.encrypt(file_content, key)
            elif form.cleaned_data['metode_crypto'] == 'rc4-img':
                encrypted_dokumen, _, _, _ = RC4_FILES.encrypt(file_content, key)
            elif form.cleaned_data['metode_crypto'] == 'des-cbc':
                encrypted_dokumen, _, _, _ = DES.des_cbc_en(file_content, key, pro)
            elif form.cleaned_data['metode_crypto'] == 'des-cfb':
                encrypted_dokumen, _, _, _ = DES.des_cfb_en(file_content, key, pro)
            elif form.cleaned_data['metode_crypto'] == 'des-ofb':
                encrypted_dokumen, _, _, _ = DES.des_ofb_en(file_content, key, pro)

            # Create a Postingan instance and link it to the Lampiran
            postingan = form.save(commit=False)
            postingan.dokumen_laporan = encrypted_dokumen
            postingan.waktu_upload = timezone.now()
            postingan.user_email_user = request.user
            postingan.lampiran_id_lampiran = lampiran  # Link to the Lampiran
            postingan.save()

            return redirect('my_posts')
    else:
        form = PostinganLampiranForm()

    return render(request, 'postingan/create.html', {'form': form})


def my_post(request):
    postingan_list = Postingan.objects.filter(user_email_user=request.user)
    
    context = {
        'postingan_list': postingan_list,
    }
    return render(request, 'postingan/my_post.html', context)
