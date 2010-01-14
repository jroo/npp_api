from piston.handler import BaseHandler, AnonymousBaseHandler
from npp.data.models import AnnualStateEnergyConsumption, AnnualStateEnergyExpenditures, StateEnergyProductionEstimates, MSNCodes, StatePostalCodes, FIPSState
from npp.data.models import ANSICountyState, FIPSCountyCongressDistrict, NCESSchoolDistrict
from django.conf import settings

def page_limits(request_get):    
    page = 1
    if 'page' in request_get:
        page = int(request_get['page'])

    lower_row = (page*settings.SEARCH_PAGINATE_BY) - settings.SEARCH_PAGINATE_BY
    upper_row = lower_row + settings.SEARCH_PAGINATE_BY
    
    return {'lower':lower_row, 'upper':upper_row}
    

class GenericHandler(BaseHandler):
    def __init__(self, allowed_keys, model):
        self.model = model
        self.allowed_keys = allowed_keys

    allowed_methods = ('GET',)

    def read(self, request):
        bound = page_limits(request.GET)

        params = {}
        for key,val in request.GET.items():
            if key in self.allowed_keys:
                params[str(key)] = val
 
        records = self.model.objects.all()           
        records = records.filter(**params)[bound['lower']:bound['upper']]
        return records
        
class ANSICountyStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'ansi_state', 'code', 'county', 'ansi_class')
        model = ANSICountyState
        super(ANSICountyStateHandler, self).__init__(allowed_keys, model)
    
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
        
class EnergyProductionEstimatesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'msn', 'year', 'value', 'state')
        model = StateEnergyProductionEstimates
        super(EnergyProductionEstimatesHandler, self).__init__(allowed_keys, model)
        
class FIPSCountyCongressDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state_code', 'county_code', 'district_code', 'congress')
        model = FIPSCountyCongressDistrict
        super(FIPSCountyCongressDistrictHandler, self).__init__(allowed_keys, model)
        
class MSNCodeHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('msn', 'description', 'unit')
        model = MSNCodes
        super(MSNCodeHandler, self).__init__(allowed_keys, model)
        
class NCESSchoolDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'district_name', 'county_name', 'county_code', 'state_code', 'congress_code', 'district_code')
        model = NCESSchoolDistrict
        exclude = ('id')
        super(NCESSchoolDistrictHandler, self).__init__(allowed_keys, model)
        
class StatePostalCodesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('code', 'state')
        model = StatePostalCodes
        super(StatePostalCodesHandler, self).__init__(allowed_keys, model)
        
class FIPSStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('code', 'state')
        model = FIPSState
        super(FIPSStateHandler, self).__init__(allowed_keys, model)
