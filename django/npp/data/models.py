from django.db import models

class AnnualStateEnergyConsumption(models.Model):
    state = models.CharField(max_length=2)
    msn = models.CharField(max_length=5)
    year = models.IntegerField()
    value = models.FloatField(null=True)
    
class AnnualStateEnergyExpenditures(models.Model):
    state = models.CharField(max_length=2)
    msn = models.CharField(max_length=5)
    year = models.IntegerField()
    value = models.FloatField(null=True)
    
class StateEnergyProductionEstimates(models.Model):
    state = models.CharField(max_length=2)
    msn = models.CharField(max_length=5)
    year = models.IntegerField()
    value = models.FloatField(null=True)
    
class MSNCodes(models.Model):
    msn = models.CharField(max_length=5)
    description = models.TextField()
    unit = models.CharField(max_length=255)
    
class StatePostalCodes(models.Model):
    code = models.CharField(max_length=2)
    state = models.CharField(max_length=32)
    
class FIPSState(models.Model):
    state = models.CharField(max_length=2)
    code = models.CharField(max_length=64)