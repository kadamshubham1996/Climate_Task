from datetime import datetime

from django.db import models



class Climate(models.Model):

      CLIMATE_TYPE = (("Max_Temp", "Max_Temp"),
                 ("Min_Temp", "Min_Temp"),
                 ("Mean_Temp", "Mean_Temp"),
                 ("Sunshine", "Sunshine"),
                 ("Rainfall", "Rainfall"),
                 ("Raindays", "Raindays"),
                 ("Days_of_Air_frost", "Days_of_Air_frost"))

      Region = models.CharField(max_length=50)
      Climate_type = models.CharField(max_length=124, choices=CLIMATE_TYPE,default=None)
      Year = models.CharField(max_length=50, null=True)
      Jan = models.CharField(max_length=50, null=True)
      Feb = models.CharField(max_length=50, null=True)
      Mar = models.CharField(max_length=50, null=True)
      Apr = models.CharField(max_length=50, null=True)
      May = models.CharField(max_length=50, null=True)
      Jun = models.CharField(max_length=50, null=True)
      Jul = models.CharField(max_length=50, null=True)
      Aug = models.CharField(max_length=50, null=True)
      Sep = models.CharField(max_length=50, null=True)
      Oct = models.CharField(max_length=50, null=True)
      Nov = models.CharField(max_length=50, null=True)
      Dec = models.CharField(max_length=50, null=True)
      Win = models.CharField(max_length=50, null=True)
      Spr = models.CharField(max_length=50, null=True)
      Sum = models.CharField(max_length=50, null=True)
      Aut = models.CharField(max_length=50, null=True)
      Ann = models.CharField(max_length=50, null=True)