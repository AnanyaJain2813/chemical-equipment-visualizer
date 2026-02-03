from django.db import models


class EquipmentDataset(models.Model):
    total = models.IntegerField()
    avg_flowrate = models.FloatField()
    avg_pressure = models.FloatField()
    avg_temperature = models.FloatField()
    type_distribution = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dataset {self.id} - {self.created_at}"
