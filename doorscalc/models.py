from django.db import models
from django.utils import timezone

# Create your models here.

class Discount(models.Model):
    title = models.CharField(max_length=99, blank=False, null=False)
    discount = models.DecimalField(max_digits=3, decimal_places=0, help_text="Wpisz zniżkę w %", blank=False, null=False)
    def __str__(self):
        return f'{self.title} | -{self.discount}%'
class Door(models.Model):
    C = 'int(w)*int(h)+int(h)*int(d)'
    F = 'int(w)*int(h)'
    szyby = [
        (C, 'Tylko frontowa w narożnych i trójstronnych'),
        (F, 'Cała'),
    ]
    
    

    title = models.CharField(max_length=200, blank=False, null=False)
    code = models.CharField(max_length=3, blank=False, null=False)
    multiplier = models.DecimalField(max_digits=3, decimal_places=0, blank=False, null=False)
    discount = models.ForeignKey("Discount", on_delete=models.CASCADE)
    excluded = models.CharField(max_length=50, default="", help_text="wymiar pomijany: width, height, depth", blank=True, null=False)
    formula = models.CharField(max_length=200, help_text="example: int(w)*int(h)+2*(int(d)*int(h))", blank=False, null=False)
    ob_formula = models.CharField(max_length=50, blank=False, null=False)

    nosna = models.CharField(help_text="Wybierz szybe nośną", choices=szyby, max_length=50, blank=False, null=True)
    nosna_max = models.FloatField(default=0.48, help_text="Wybierz maksymalną powierzchnie szyby nośnej", max_length=50, blank=False, null=False)

    gasket = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='images/', default="image.png")
    tooltip = models.CharField(help_text="Wpisz krótki opis pod myszką", default="", blank=False, null=False, max_length=50)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.code} | {self.title}'