from piston.handler import BaseHandler, AnonymousBaseHandler
from data.models import AnnualStateEnergyConsumption, AnnualStateEnergyExpenditures
from django.conf import settings

def page_limits(request_get):    
    if 'page' in request_get:
        page = int(request_get['page'])
    else:
        page = 1 

    lower_row = (page*settings.SEARCH_PAGINATE_BY) - settings.SEARCH_PAGINATE_BY
    upper_row = lower_row + settings.SEARCH_PAGINATE_BY
    
    return {'lower_row':lower_row, 'upper_row':upper_row}
    
class EnergyConsumptionHandler(BaseHandler):
    allowed_methods = ('GET',)
    allowed_keys = ('id','msn','year','value', 'state')
    model = AnnualStateEnergyConsumption
    #anonymous = 'AnonymousEnergyConsumptionHandler'
    
    def read(self, request, id=None):
        bounds = page_limits(request.GET)

        params = {}
        for key,val in request.GET.items():
            if key in self.allowed_keys:
                params[str(key)] = val
 
        records = model.objects.all()           
        records = records.filter(**params)[bounds['lower_row']:bounds['upper_row']]
        return records
            
#class AnonymousEnergyConsumptionHandler(AnonymousBaseHandler):
    #fields = ('id')
    
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
    
