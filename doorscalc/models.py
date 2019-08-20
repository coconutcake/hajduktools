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
    
    

    title = models.CharField(verbose_name=u"Nazwa", max_length=200, blank=False, null=False)
    code = models.CharField(verbose_name=u"Kod", max_length=3, blank=False, null=False)
    multiplier = models.DecimalField(verbose_name=u"Mnożnik", max_digits=3, decimal_places=0, blank=False, null=False)
    discount = models.ForeignKey('Discount', verbose_name=u"Zniżka", on_delete=models.CASCADE)
    excluded = models.CharField(verbose_name=u"Wyłączony wymiar", max_length=50, default="", help_text="wymiar pomijany: width, height, depth", blank=True, null=False)
    formula = models.CharField(verbose_name=u"Pole powierzchni", max_length=200, help_text="example: int(w)*int(h)+2*(int(d)*int(h))", blank=False, null=False)
    ob_formula = models.CharField(verbose_name=u"Obwód uszczelki", max_length=50, blank=False, null=False)

    nosna = models.CharField(verbose_name=u"Skrzydło nośne", help_text="Wybierz szybe nośną", choices=szyby, max_length=50, blank=False, null=True)
    nosna_max = models.FloatField(verbose_name=u"Maks. powierzchnia skrzydła nośnego", default=0.48, help_text="Wybierz maksymalną powierzchnie szyby nośnej", max_length=50, blank=False, null=False)

    gasket = models.BooleanField(verbose_name=u"Uszczelka w zestawie", default=False)
    cover = models.ImageField(upload_to='images/', default="image.png")
    tooltip = models.CharField(verbose_name=u"Podpowiedź", help_text="Wpisz krótki opis pod myszką", default="", blank=True, null=False, max_length=50)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.code} | {self.title}'