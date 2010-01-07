from piston.handler import BaseHandler, AnonymousBaseHandler
from data.models import AnnualStateEnergyConsumption

class EnergyConsumptionHandler(BaseHandler):
    
    allowed_methods = ('GET',)
    model = AnnualStateEnergyConsumption
    anonymous = 'AnonymousEnergyConsumptionHandler'
    
    def read(self, request, id=None):
        if id != None:
            record = AnnualStateEnergyConsumption.objects.get(id=id)
            return record
        else:
            records = AnnualStateEnergyConsumption.objects.all()[:10]
            return records
            
class AnonymousEnergyConsumptionHandler(AnonymousBaseHandler):
    fields = ('id')