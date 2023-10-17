from django.shortcuts import render, get_object_or_404, redirect
from .models import Profil
from .forms import ProfilEditForm, ProfilCreateForm
from django.http import HttpResponse, HttpResponseForbidden

def view_profil_image(request, user_id):
    # Check if the user requesting the image is the owner of the profile
    if request.user.is_authenticated and request.user.id == user_id:
        profil = get_object_or_404(Profil, user_email_user_id=user_id)
        if profil.gambar:
            with open(profil.gambar.path, 'rb') as image_file:
                response = HttpResponse(image_file.read(), content_type='image/jpeg')
            return response
    return HttpResponseForbidden("You do not have permission to view this image.")

def edit_profil(request):
    # Get the Profil instance for the currently logged-in user
    profil, created = Profil.objects.get_or_create(user_email_user=request.user)

    if request.method == 'POST':
        # Bind the form with POST data
        form = ProfilEditForm(request.POST, request.FILES, instance=profil)  # Note the use of request.FILES
        if form.is_valid():
            # Handle the uploaded image
            if 'gambar' in request.FILES:
                form.instance.gambar.name = profil.unique_filename(request.FILES['gambar'].name)
            # Save the changes
            form.save()
            return redirect('edit_profil')  # Redirect back to the edit form
    else:
        # Display the form with the existing data
        form = ProfilEditForm(instance=profil)

    return render(request, 'profil/edit.html', {'form': form})

def create_profil(request):
    try:
        profil = Profil.objects.get(user_email_user=request.user)
        return redirect('edit_profil')  # Redirect to the edit view if the profile already exists
    except Profil.DoesNotExist:
        if request.method == 'POST':
            form = ProfilCreateForm(request.POST, request.FILES)  # Include request.FILES for file uploads
            if form.is_valid():
                profil = form.save(commit=False)
                profil.user_email_user = request.user
                profil.save()
                return redirect('edit_profil')  # Redirect to the edit view after creating the profile
        else:
            form = ProfilCreateForm()

        return render(request, 'profil/create.html', {'form': form})

