from piston.handler import BaseHandler, AnonymousBaseHandler
from data.models import AnnualStateEnergyConsumption, AnnualStateEnergyExpenditures

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
    
class EnergyExpendituresHandler(BaseHandler):
    
    allowed_methods = ('GET',)
    model = AnnualStateEnergyExpenditures
    
    def read(self, request, id=None):
        if id != None:
            record = AnnualStateEnergyExpenditures.objects.get(id=id)
            return record
        else:
            records = AnnualStateEnergyExpenditures.objects.all()[:10]
            return records
    
