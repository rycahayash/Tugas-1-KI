from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from profil.models import Profil
from lampiran.models import Lampiran
from postingan.models import Postingan

# custom_middleware.py
class MediaAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def has_permission_to_access_idcards(self, request):
        # image_path = 'id_cards/muthu_20231017001051_20231017001051.png'
        image_path = request.path.split('/media/')[1]

        profil = Profil.objects.get(gambar__contains=image_path)

        if profil.user_email_user == request.user:
            return True
        
    def has_permission_to_access_lampiran(self, request):
        dokumen_path = request.path.split('/media/')[1]

        try:
            lampiran = Lampiran.objects.get(dokumen_laporan__contains=dokumen_path)
            postingan = Postingan.objects.get(lampiran_id_lampiran=lampiran.id_lampiran)

            if postingan.user_email_user == request.user:
                return True, None
        except Lampiran.DoesNotExist or Postingan.DoesNotExist:
            pass

        return False, lampiran.id_lampiran


    def __call__(self, request):
        # Perform your logic here
        if request.path.startswith('/media/id_cards'):
            if request.user.is_authenticated:
                if not self.has_permission_to_access_idcards(request):
                    # Redirect to a custom HTML page for access forbidden
                    return HttpResponseRedirect(reverse('custom_access_denied_page'))
        # lampiran
        if request.path.startswith('/media/lampiran'):
            if request.user.is_authenticated:
                status, lampiran = self.has_permission_to_access_lampiran(request)
                if not status:
                    # Redirect to a custom HTML page for access forbidden
                    return HttpResponseRedirect(reverse('download_page', args=[lampiran]))

        response = self.get_response(request)
        return response
    
    