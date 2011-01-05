from piston.handler import BaseHandler, AnonymousBaseHandler
from npp.data.models import *
from django.conf import settings
from piston.doc import generate_doc
from django.http import Http404

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
    
    def get_allowed_keys(self):
        return self.allowed_keys

    def read(self, request):
        bound = page_limits(request.GET)

        params = {}
        for key,val in request.GET.items():
            if key in self.allowed_keys:
                params[str(key)] = val
 
        records = self.model.objects.all()           
        
        # ADDED 01/05/2010 - allow a no_limit option for apps making large queries, 
        # else paginate normally
        if 'no_limit' in request.GET:
                no_limit = True
                records.filter(**params)
        else:
            records = records.filter(**params)[bound['lower']:bound['upper']]
            

        return records
        
class AlternativeFuelVehiclesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'fips_state')
        model = AlternativeFuelVehicles
        super(AlternativeFuelVehiclesHandler, self).__init__(allowed_keys, model)
        
class AnsiCountyStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'ansi_state', 'code', 'county', 'ansi_class')
        model = AnsiCountyState
        super(AnsiCountyStateHandler, self).__init__(allowed_keys, model)
        
class AtCodesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('code',)
        model = AtCodes
        super(AtCodesHandler, self).__init__(allowed_keys, model)
        
class AverageTeacherSalaryHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = AverageTeacherSalary
        super(AverageTeacherSalaryHandler, self).__init__(allowed_keys, model)
        
class BilingualEdSpendingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = BilingualEdSpending
        super(BilingualEdSpendingHandler, self).__init__(allowed_keys, model)
        
class BudgetCategorySubfunctionsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('subfunction',)
        model = BudgetCategorySubfunctions
        super(BudgetCategorySubfunctionsHandler, self).__init__(allowed_keys, model)
        
class CffrHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'state_code', 'county_code', 'place_code', 'state_postal', 'congressional_district', 'program_code', 'object_type', 'agency_code', 'funding_sign')
        model = Cffr
        super(CffrHandler, self).__init__(allowed_keys, model)
  
class CffrAgencyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'agency_code', 'agency_name')
        model = CffrAgency
        super(CffrAgencyHandler, self).__init__(allowed_keys, model)
        
class CffrGeoHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'state_code', 'county_code', 'place_code', 'place_name', 'state_gu', 'type_gu', 'county_gu', 'place_gu', 'split_gu', 'congress_district')
        model = CffrGeo
        super(CffrGeoHandler, self).__init__(allowed_keys, model)
        
class CffrObjectCodeHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'object_code', 'category')
        model = CffrObjectCode
        super(CffrObjectCodeHandler, self).__init__(allowed_keys, model)
        
class CffrProgramHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'program_id_code', 'program_name')
        model = CffrProgram
        super(CffrProgramHandler, self).__init__(allowed_keys, model)
        
class ChildrenPovertyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'age_range')
        model = ChildrenPoverty
        super(ChildrenPovertyHandler, self).__init__(allowed_keys, model)
        
class CountyPopulationEstimatesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'geo_id', 'geo_id2', 'sum_level', 'geo_name')
        model = CountyPopulationEstimates
        super(CountyPopulationEstimatesHandler, self).__init__(allowed_keys, model)
        
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
    
class DrugFreeSchoolSpendingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = DrugFreeSchoolSpending
        super(DrugFreeSchoolSpendingHandler, self).__init__(allowed_keys, model)
        
class EducationalAttainmentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state', 'gender', 'value_type', 'category')
        model = EducationalAttainment
        super(EducationalAttainmentHandler, self).__init__(allowed_keys, model)
        
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
        
class EnrolledStudentsDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state', )
        model = EnrolledStudentsDistrict
        super(EnrolledStudentsDistrictHandler, self).__init__(allowed_keys, model)
        
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

class EllStudentsDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = EllStudentsDistrict
        super(EllStudentsDistrictHandler, self).__init__(allowed_keys, model)
        
class ExpenditurePerPupilHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = ExpenditurePerPupil
        super(ExpenditurePerPupilHandler, self).__init__(allowed_keys, model)
        
class FamiliesPovertyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = FamiliesPoverty
        super(FamiliesPovertyHandler, self).__init__(allowed_keys, model)
        
class FcnaSpendingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = FcnaSpending
        super(FcnaSpendingHandler, self).__init__(allowed_keys, model)
        
class FederalImpactAidHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = FederalImpactAid
        super(FederalImpactAidHandler, self).__init__(allowed_keys, model)
        
class FipsCountyCongressDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state_code', 'county_code', 'district_code', 'congress')
        model = FipsCountyCongressDistrict
        super(FipsCountyCongressDistrictHandler, self).__init__(allowed_keys, model)
        
class FipsStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('code', 'state')
        model = FipsState
        super(FipsStateHandler, self).__init__(allowed_keys, model)

class FreeLunchEligibleHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = FreeLunchEligible
        super(FreeLunchEligibleHandler, self).__init__(allowed_keys, model)
        
class FreeReducedLunchEligibleHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = FreeReducedLunchEligible
        super(FreeReducedLunchEligibleHandler, self).__init__(allowed_keys, model)
        
class FreeReducedLunchEligibleCountyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'county_name', 'year')
        model = FreeReducedLunchEligibleCounty
        super(FreeReducedLunchEligibleCountyHandler, self).__init__(allowed_keys, model)
        
class HalfPintsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = HalfPints
        super(HalfPintsHandler, self).__init__(allowed_keys, model)
        
class HeadStartEnrollmentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = HeadStartEnrollment
        super(HeadStartEnrollmentHandler, self).__init__(allowed_keys, model)
                
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
        
class IndividualEducationProgramsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = IndividualEducationPrograms
        super(IndividualEducationProgramsHandler, self).__init__(allowed_keys, model)
        
class IrsGrossCollectionsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = IrsGrossCollections
        super(IrsGrossCollectionsHandler, self).__init__(allowed_keys, model)
        
class KidsHealthInsuranceHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = KidsHealthInsurance
        super(KidsHealthInsuranceHandler, self).__init__(allowed_keys, model)
        
class MathScienceSpendingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = MathScienceSpending
        super(MathScienceSpendingHandler, self).__init__(allowed_keys, model)

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
        
class MigrantStudentsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = MigrantStudents
        super(MigrantStudentsHandler, self).__init__(allowed_keys, model)
        
class MilitaryPersonnelHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = MilitaryPersonnel
        super(MilitaryPersonnelHandler, self).__init__(allowed_keys, model)
        
class MsnCodeHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('msn', 'description', 'unit')
        model = MsnCodes
        super(MsnCodeHandler, self).__init__(allowed_keys, model)
        
class NativeEdSpendingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = NativeEdSpending
        super(NativeEdSpendingHandler, self).__init__(allowed_keys, model)
        
class NewAidsCasesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = NewAidsCases
        super(NewAidsCasesHandler, self).__init__(allowed_keys, model)
        
class NcesSchoolDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'district_name', 'county_name', 'county_code', 'state_code', 'congress_code', 'district_code')
        model = NcesSchoolDistrict
        super(NcesSchoolDistrictHandler, self).__init__(allowed_keys, model)
        
class OtherFederalRevenueHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = OtherFederalRevenue
        super(OtherFederalRevenueHandler, self).__init__(allowed_keys, model)
        
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
        
class PopulationCongressionalDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'district', 'year')
        model = PopulationCongressionalDistrict
        super(PopulationCongressionalDistrictHandler, self).__init__(allowed_keys, model)
        
class PopulationFamiliesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = PopulationFamilies
        super(PopulationFamiliesHandler, self).__init__(allowed_keys, model)

class PupilTeacherDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = PupilTeacherDistrict
        super(PupilTeacherDistrictHandler, self).__init__(allowed_keys, model) 
               
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
        
class RetiredDisabledNilfHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = RetiredDisabledNilf
        super(RetiredDisabledNilfHandler, self).__init__(allowed_keys, model)
        
class SaipeSchoolHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'fips_state', 'ccd_district_id', 'district_name')
        model = SaipeSchool
        super(SaipeSchoolHandler, self).__init__(allowed_keys, model)
        
class SaipeCountyStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'fips_state', 'fips_county', 'state_county_name', 'state_postal_abbreviation')
        model = SaipeCountyState
        super(SaipeCountyStateHandler, self).__init__(allowed_keys, model)
        
class SchipEnrollmentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = SchipEnrollment
        super(SchipEnrollmentHandler, self).__init__(allowed_keys, model)

class SchoolBreakfastParticipationHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = SchoolBreakfastParticipation
        super(SchoolBreakfastParticipationHandler, self).__init__(allowed_keys, model)
        
class SchoolLunchParticipationHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = SchoolLunchParticipation
        super(SchoolLunchParticipationHandler, self).__init__(allowed_keys, model)
        
class ShelterPopulationHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = ShelterPopulation
        super(ShelterPopulationHandler, self).__init__(allowed_keys, model)
        
class SnapBenefitsRecipientsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state_fips', 'county_fips', 'name', 'year')
        model = SnapBenefitsRecipients
        super(SnapBenefitsRecipientsHandler, self).__init__(allowed_keys, model)
        
class SnapMonthlyBenefitsPersonHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = SnapMonthlyBenefitsPerson
        super(SnapMonthlyBenefitsPersonHandler, self).__init__(allowed_keys, model)
        
class SnapParticipationHouseholdsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = SnapParticipationHouseholds
        super(SnapParticipationHouseholdsHandler, self).__init__(allowed_keys, model)
        
class SnapParticipationPeopleHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = SnapParticipationPeople
        super(SnapParticipationPeopleHandler, self).__init__(allowed_keys, model)
        
class SpecialEdFundingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = SpecialEdFunding
        super(SpecialEdFundingHandler, self).__init__(allowed_keys, model)
        
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
        
class StateGdpHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = StateGdp
        super(StateGdpHandler, self).__init__(allowed_keys, model)

class StateGdpPre97Handler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = StateGdp
        super(StateGdpPre97Handler, self).__init__(allowed_keys, model)

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
        
class SubfunctionsCffrHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('subfunction_number', 'cfda_program_code', 'at_code_1', 'at_code_2',
            'at_code_3', 'at_code_4', 'at_code_5', 'at_code_6' ,'at_code_7', 'at_code_8')
        model = SubfunctionsCffr
        super(SubfunctionsCffrHandler, self).__init__(allowed_keys, model)
        
class SummerLunchParticipationHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = SummerLunchParticipation
        super(SummerLunchParticipationHandler, self).__init__(allowed_keys, model)
        
class TitleIFundingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = TitleIFunding
        super(TitleIFundingHandler, self).__init__(allowed_keys, model)
        
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
        
class VocationalEdSpendingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = VocationalEdSpending
        super(VocationalEdSpendingHandler, self).__init__(allowed_keys, model)
        
class WicBenefitsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('place', 'state', 'year', 'type')
        model = WicBenefits
        super(WicBenefitsHandler, self).__init__(allowed_keys, model)
        
class WicParticipantsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('place', 'state', 'year', 'type')
        model = WicParticipants
        super(WicParticipantsHandler, self).__init__(allowed_keys, model)
