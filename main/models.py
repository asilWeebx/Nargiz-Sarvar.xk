import qrcode
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from distutils.command.upload import upload
from django.core.files import File
from io import BytesIO
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

class Blog(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=150)
    info = models.TextField()

    def __str__(self):
        return self.name


class About(models.Model):
    info = models.TextField()

    def __str__(self):
        return self.info


class Hujjatlar(models.Model):
    file = models.FileField(upload_to='hujjatlar/')
    name = models.CharField(max_length=120)
    PDF = "PDF"
    TXT = "TXT"
    XLS = "XLS"
    DOC = "DOC"
    JPG = "JPG"
    the_file = (
        (PDF, "PDF"),
        (TXT, "TXT"),
        (XLS, "XLS"),
        (DOC, "DOC"),
        (JPG, "JPG"),
    )
    qr_code = models.ImageField(upload_to='qr_code',blank=True,null=True)
    file_type = models.CharField(max_length=10, choices=the_file, default='PDF')

    def save(self, *args, **kwargs):
        QRCode = qrcode.QRCode()
        QRCode.add_data(f"http://127.0.0.1:8000/media/hujjatlar/{self.file}")
        QRCode.make()
        QRimg = QRCode.make_image(
            image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),
            embeded_image_path="media/korxona.jpg"
        )
        fname = 'qr-code' + str(self.id) + '.png'
        buffer = BytesIO()
        QRimg.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        QRimg.close()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Karusel1(models.Model):
       name = models.CharField(max_length=150)
       info = models.TextField()
       img = models.ImageField(upload_to='images/')

       def __str__(self):
           return self.name


class KaruselLoop(models.Model):
       name = models.CharField(max_length=150)
       info = models.TextField()
       img = models.ImageField(upload_to='images/')

       def __str__(self):
           return self.name

class Send(models.Model):
    sending = models.ForeignKey(Contact,on_delete=models.CASCADE)
    message = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
