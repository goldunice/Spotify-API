from django.db import models


class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=255)
    tugilgan_yil = models.DateField(blank=True, null=True)
    davlat = models.CharField(max_length=255)

    def __str__(self):
        return self.ism


class Albom(models.Model):
    nom = models.CharField(max_length=255)
    sana = models.DateField(blank=True, null=True)
    rasm = models.FileField(blank=True, null=True, upload_to='rasmlar')
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Qoshiq(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=255)
    davomiylik = models.DurationField(blank=True, null=True)
    fayl = models.FileField(null=True, upload_to='musiqalar')
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
