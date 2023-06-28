from django.db import models

# Create your models here.
class Buku(models.Model):
    id_buku = models.AutoField(primary_key=True)
    cover_buku = models.CharField(max_length=500)
    judul_buku = models.CharField(max_length=255)
    stok = models.CharField(max_length=20)

    def __str__(self):
        return self.judul_buku