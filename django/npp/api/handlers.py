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
    

class GenericHandler(BaseHandler):
    def __init__(self, allowed_keys, model):
        self.model = model
        self.allowed_keys = allowed_keys 
    allowed_methods = ('GET',)
    
    def read(self, request):
        bounds = page_limits(request.GET)

        params = {}
        for key,val in request.GET.items():
            if key in self.allowed_keys:
                params[str(key)] = val
 
        records = self.model.objects.all()           
        records = records.filter(**params)[bounds['lower_row']:bounds['upper_row']]
        return records
    
class EnergyConsumptionHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'msn', 'year', 'value', 'state')
        model = AnnualStateEnergyConsumption
        super(EnergyConsumptionHandler, self).__init__(allowed_keys, model)

class EnergyExpendituresHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'msn', 'year', 'value', 'state')
        model = AnnualStateEnergyConsumption
        super(EnergyExpendituresHandler, self).__init__(allowed_keys, model)
