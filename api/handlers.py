from piston.handler import BaseHandler, AnonymousBaseHandler
from npp.data.models import *
from django.conf import settings
from piston.doc import generate_doc

def page_limits(request_get):    
    page = 1
    if 'page' in request_get:
        page = int(request_get['page'])

    lower_row = (page*settings.SEARCH_PAGINATE_BY) - settings.SEARCH_PAGINATE_BY
    upper_row = lower_row + settings.SEARCH_PAGINATE_BY
    
    return {'lower':lower_row, 'upper':upper_row}
    
class GenericHandler(BaseHandler):
    def __init__(self, allowed_keys, model, fields=None):
        self.model = model
        self.allowed_keys = allowed_keys
        self.fields = fields

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
        
class AlternativeFuelVehiclesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'fips_state')
        model = AlternativeFuelVehicles
        super(AlternativeFuelVehiclesHandler, self).__init__(allowed_keys, model)
        
class ANSICountyStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'ansi_state', 'code', 'county', 'ansi_class')
        model = ANSICountyState
        super(ANSICountyStateHandler, self).__init__(allowed_keys, model)
        
class ATCodesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('code')
        model = ATCodes
        super(ATCodesHandler, self).__init__(allowed_keys, model)
        
class AverageTeacherSalaryHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = AverageTeacherSalary
        super(AverageTeacherSalaryHandler, self).__init__(allowed_keys, model)
        
class BudgetCategorySubfunctionsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('subfunction')
        model = BudgetCategorySubfunctions
        super(BudgetCategorySubfunctionsHandler, self).__init__(allowed_keys, model)
        
class CFFRHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'state_code', 'county_code', 'place_code', 'state_postal', 'congressional_district', 'program_code', 'object_type', 'agency_code', 'funding_sign')
        model = CFFR
        super(CFFRHandler, self).__init__(allowed_keys, model)
        
class CFFRAgencyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'agency_code', 'agency_name')
        model = CFFRAgency
        super(CFFRAgencyHandler, self).__init__(allowed_keys, model)
        
class CFFRGeoHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'state_code', 'county_code', 'place_code', 'place_name', 'state_gu', 'type_gu', 'county_gu', 'place_gu', 'split_gu', 'congress_district')
        model = CFFRGeo
        super(CFFRGeoHandler, self).__init__(allowed_keys, model)
        
class CFFRObjectCodeHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'object_code', 'category')
        model = CFFRObjectCode
        super(CFFRObjectCodeHandler, self).__init__(allowed_keys, model)
        
class CFFRProgramHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'program_id_code', 'program_name')
        model = CFFRProgram
        super(CFFRProgramHandler, self).__init__(allowed_keys, model)
        
class CountyUnemploymentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state_fips', 'county_fips', 'year')
        model = CountyUnemployment
        super(CountyUnemploymentHandler, self).__init__(allowed_keys, model)
        
class DiplomaRecipientTotalHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'key')
        model = DiplomaRecipientTotal
        super(DiplomaRecipientTotalHandler, self).__init__(allowed_keys, model)
        
class DropoutsRaceHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'key')
        model = DropoutsRace
        super(DropoutsRaceHandler, self).__init__(allowed_keys, model)
        
class EmploymentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = Employment
        super(EmploymentHandler, self).__init__(allowed_keys, model)
    
class EnergyConsumptionHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'msn', 'year', 'value', 'state')
        model = AnnualStateEnergyConsumption
        super(EnergyConsumptionHandler, self).__init__(allowed_keys, model)

class EnergyExpendituresHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'msn', 'year', 'value', 'state')
        model = AnnualStateEnergyExpenditures
        super(EnergyExpendituresHandler, self).__init__(allowed_keys, model)
        
class EnrollmentRaceHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'key')
        model = EnrollmentRace
        super(EnrollmentRaceHandler, self).__init__(allowed_keys, model)
        
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
        
class FIPSStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('code', 'state')
        model = FIPSState
        super(FIPSStateHandler, self).__init__(allowed_keys, model)
        
class HealthInsuranceHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = HealthInsurance
        super(HealthInsuranceHandler, self).__init__(allowed_keys, model)

class HighSchoolDropoutsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = HighSchoolDropouts
        super(HighSchoolDropoutsHandler, self).__init__(allowed_keys, model)
        
class HighSchoolOtherHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'key')
        model = HighSchoolOther
        super(HighSchoolOtherHandler, self).__init__(allowed_keys, model)
                
class HousingUnitsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = HousingUnits
        super(HousingUnitsHandler, self).__init__(allowed_keys, model)
        
class IRSGrossCollectionsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = IRSGrossCollections
        super(IRSGrossCollectionsHandler, self).__init__(allowed_keys, model)
        
class KidsHealthInsuranceHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = KidsHealthInsurance
        super(KidsHealthInsuranceHandler, self).__init__(allowed_keys, model)

class MedicaidParticipationHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = MedicaidParticipation
        super(MedicaidParticipationHandler, self).__init__(allowed_keys, model)
        
class MedicareEnrollmentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = MedicareEnrollment
        super(MedicareEnrollmentHandler, self).__init__(allowed_keys, model)

class MedianHouseholdIncome4MemberHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = MedianHouseholdIncome4Member
        super(MedianHouseholdIncome4MemberHandler, self).__init__(allowed_keys, model)
        
class MilitaryPersonnelHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = MilitaryPersonnel
        super(MilitaryPersonnelHandler, self).__init__(allowed_keys, model)
        
class MSNCodeHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('msn', 'description', 'unit')
        model = MSNCodes
        super(MSNCodeHandler, self).__init__(allowed_keys, model)
        
class NewAIDSCasesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = NewAIDSCases
        super(NewAIDSCasesHandler, self).__init__(allowed_keys, model)
        
class NCESSchoolDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'district_name', 'county_name', 'county_code', 'state_code', 'congress_code', 'district_code')
        model = NCESSchoolDistrict
        super(NCESSchoolDistrictHandler, self).__init__(allowed_keys, model)
        
class OwnersRentersHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = OwnersRenters
        super(OwnersRentersHandler, self).__init__(allowed_keys, model)
        
class PeopleInPovertyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = PeopleInPoverty
        super(PeopleInPovertyHandler, self).__init__(allowed_keys, model)
        
class PopulationFamiliesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = PopulationFamilies
        super(PopulationFamiliesHandler, self).__init__(allowed_keys, model) 
               
class PresidentsBudgetHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('budget_type', 'source_category_code', 'source_subcategory_code', 'agency_code', 'bureau_code', 'account_code', 'treasury_agency_code', 'subfunction_code', 'grant_non_grant')
        model = PresidentsBudget
        fields = ('budget_type', 'source_category_code', 'source_category_name',
            'source_subcategory_code', 'source_subcategory_name', 'agency_code',
            'agency_name', 'bureau_code', 'bureau_name', 'account_code',
            'account_name', 'treasury_agency_code', 'subfunction_code',
            'subfunction_title', 'bea_category', 'grant_non_grant',
            'on_off_budget', ('years', ('year', 'value',),),)
        super(PresidentsBudgetHandler, self).__init__(allowed_keys, model, fields)
        
class RacePopulation1980sHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('fips_state', 'year', 'race_code', 'sex')
        model = RacePopulation1980s
        super(RacePopulation1980sHandler, self).__init__(allowed_keys, model)
        
class RacePopulation1990sHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('area', 'year')
        model = RacePopulation1990s
        super(RacePopulation1990sHandler, self).__init__(allowed_keys, model)
        
class SCHIPEnrollmentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = SCHIPEnrollment
        super(SCHIPEnrollmentHandler, self).__init__(allowed_keys, model)
        
class StateCompletionRateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'key')
        model = StateCompletionRate
        super(StateCompletionRateHandler, self).__init__(allowed_keys, model)
        
class StateEmissionsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'producer_type', 'energy_source')
        model = StateEmissions
        super(StateEmissionsHandler, self).__init__(allowed_keys, model)
        
class StateGDPHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = StateGDP
        super(StateGDPHandler, self).__init__(allowed_keys, model)

class StateGDPPre97Handler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = StateGDP
        super(StateGDPPre97Handler, self).__init__(allowed_keys, model)

class StateLaborForceParticipationHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = StateLaborForceParticipation
        super(StateLaborForceParticipationHandler, self).__init__(allowed_keys, model)
        
class StateMedianIncomeHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'start_year', 'end_year')
        model = StateMedianIncome
        super(StateMedianIncomeHandler, self).__init__(allowed_keys, model)
        
class StatePopulationEstimatesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = StatePopulationEstimates
        super(StatePopulationEstimatesHandler, self).__init__(allowed_keys, model)
        
class StatePostalCodesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('code', 'state')
        model = StatePostalCodes
        super(StatePostalCodesHandler, self).__init__(allowed_keys, model)
        
class StateRenewableEnergyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state')
        model = StateRenewableEnergy
        super(StateRenewableEnergyHandler, self).__init__(allowed_keys, model)
        
class StateUnemploymentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state')
        model = StateUnemployment
        super(StateUnemploymentHandler, self).__init__(allowed_keys, model)
        
class SubfunctionsCFFRHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('subfunction_number', 'cfda_program_code', 'at_code_1', 'at_code_2',
            'at_code_3', 'at_code_4', 'at_code_5', 'at_code_6' ,'at_code_7', 'at_code_8')
        model = SubfunctionsCFFR
        super(SubfunctionsCFFRHandler, self).__init__(allowed_keys, model)
        
class SAIPESchoolHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'fips_state', 'ccd_district_id', 'district_name')
        model = SAIPESchool
        super(SAIPESchoolHandler, self).__init__(allowed_keys, model)
        
class SAIPECountyStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'fips_state', 'fips_county', 'state_county_name', 'state_postal_abbreviation')
        model = SAIPECountyState
        super(SAIPECountyStateHandler, self).__init__(allowed_keys, model)
        
class ShelterPopulationHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = ShelterPopulation
        super(ShelterPopulationHandler, self).__init__(allowed_keys, model)
        
class TeacherPupilRatioHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = TeacherPupilRatio
        super(TeacherPupilRatioHandler, self).__init__(allowed_keys, model)
        
class TotalStudentsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = TotalStudents
        super(TotalStudentsHandler, self).__init__(allowed_keys, model)
        
class VehicleRegistrationsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = VehicleRegistrations
        super(VehicleRegistrationsHandler, self).__init__(allowed_keys, model)
