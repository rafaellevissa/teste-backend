from django.db import models

class Briefing(models.Model):
    name = models.CharField(max_length=255)
    retailer = models.ForeignKey('retailer.Retailer', on_delete=models.CASCADE)
    responsible = models.CharField(max_length=255)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    release_date = models.DateField()
    available = models.IntegerField()

    def __str__(self):
        return self.name
    