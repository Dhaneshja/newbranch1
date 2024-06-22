from django.db import models

class product(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False)
    num_of_product = models.IntegerField()

    def _str_(self):
      return f'{self.category} - {self.num_of_products}'