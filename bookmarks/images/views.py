from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.shortcuts import get_object_or_404

@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            
            new_image.user = request.user
            new_image.save()
            messages.success(request,'Image added successfully.')
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
        
    return render(request,
                  'images/image/create.html',
                  {
                      'section' : 'images',
                      'form' : form
                  })
        
        
# view for the the detail of the image
def image_view(request,id,slug):
    image = get_object_or_404(Image,id=id,slug=slug)
    return render(
        request,
        'images/image/detail.html',
        {
            'section' : 'images',
            'image' : image
        }
    )
