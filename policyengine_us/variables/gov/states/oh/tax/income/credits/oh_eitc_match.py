from policyengine_us.model_api import *


class oh_wftc(Variable):
    value_type = float
    entity = TaxUnit
    label = "Ohio Working Families Tax Credit"
    unit = USD
    definition_period = YEAR
    reference = ""
    defined_for = StateCode.OH

    def formula_2023(tax_unit, period, parameters):
        federal_eitc = tax_unit("earned_income_tax_credit", period)
        rate = parameters(
            period
        ).gov.states.oh.tax.income.credits.eitc_match
        return federal_eitc * rate
