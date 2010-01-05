from piston.handler import BaseHandler
from data.models import AnnualStateEnergyConsumption

class EnergyConsumptionHandler(BaseHandler):
    
    allowed_methods = ('GET',)
    model = AnnualStateEnergyConsumption
    
    def read(self, request, id):
        record = AnnualStateEnergyConsumption.objects.get(id=id)
        return record