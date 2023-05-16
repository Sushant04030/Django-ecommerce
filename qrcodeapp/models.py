from django.db import models

# Create your models here.

class qrimage(models.Model):
    qr_img_name     = models.CharField(max_length=200, default= 'new')
    qr_img    = models.ImageField(upload_to="static/images/qrcodes/")

    def __str__(self):
        return self.qr_img_name
