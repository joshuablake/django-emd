from django.db import models

class HistoricalPrice(models.Model):
    region = models.ForeignKey('static.Region')
    date = models.DateField()
    type = models.ForeignKey('static.Type')
    price_low = models.DecimalField(max_digits=15, decimal_places=2)
    price_average = models.DecimalField(max_digits=15, decimal_places=2)
    price_high = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.BigIntegerField()

    class Meta:
        unique_together = ('region', 'date', 'type')
        db_table = 'items_history'
        managed = False
