# from qrcode import image, make
# from django.shortcuts import render
# from .models import *
# import time

# def qr_gen(request):
#     image1 = None
#     if request.method == 'POST':
#         data1 = request.POST['data']
#         img = make(data1)
#         img_name = 'qr' + "-" + data1 + '.png'
        
#         image1 = qrimage.objects.create(data = img_name,image = img)
#         image1.save()

#     context = {
#         'image1' : image1,
#     }
#     return render(request, 'qrimage.html',context)


# qrcodeapp/views.py

# from django.shortcuts import render
# from django.conf import settings
# from qrcode import *
# import time

# def qr_gen(request):
#     if request.method == 'POST':
#         data = request.POST['data']
#         img = make(data)
#         img_name = 'qr' + str(time.time()) + '.png'
#         img.save(settings.STATIC_ROOT + 's/' + 'qrcodes' + '/' + img_name)
#         return render(request, 'qrimage.html', {'img_name': img_name})
#     return render(request, 'qrimage.html')



from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time
from .models import *

def qr_gen(request):
    if request.method == 'POST':
        data = request.POST['data']
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save(settings.STATIC_ROOT + 's/' + 'qrcodes' + '/' + img_name)
        print(img)
        image1 = qrimage.objects.create(
            qr_img_name = img_name,
            qr_img = img_name
        )
        image1.save()

        return render(request, 'qrimage.html', {'img_name': img_name})
    return render(request, 'qrimage.html')