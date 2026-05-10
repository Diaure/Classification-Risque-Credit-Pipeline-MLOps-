
from pydantic import BaseModel
from typing import Optional

class ClientFeatures(BaseModel):
    SK_ID_CURR: Optional[int] = None
    NAME_CONTRACT_TYPE: Optional[str] = None
    CODE_GENDER: Optional[str] = None
    FLAG_OWN_CAR: Optional[str] = None
    FLAG_OWN_REALTY: Optional[str] = None
    CNT_CHILDREN: Optional[int] = None
    AMT_INCOME_TOTAL: Optional[float] = None
    AMT_GOODS_PRICE: Optional[float] = None
    NAME_TYPE_SUITE: Optional[str] = None
    NAME_INCOME_TYPE: Optional[str] = None
    NAME_EDUCATION_TYPE: Optional[str] = None
    NAME_FAMILY_STATUS: Optional[str] = None
    NAME_HOUSING_TYPE: Optional[str] = None
    REGION_POPULATION_RELATIVE: Optional[float] = None
    DAYS_BIRTH: Optional[int] = None
    DAYS_EMPLOYED: Optional[int] = None
    DAYS_REGISTRATION: Optional[float] = None
    DAYS_ID_PUBLISH: Optional[int] = None
    OWN_CAR_AGE: Optional[float] = None
    FLAG_MOBIL: Optional[bool] = None
    FLAG_EMP_PHONE: Optional[bool] = None
    FLAG_WORK_PHONE: Optional[bool] = None
    FLAG_CONT_MOBILE: Optional[bool] = None
    FLAG_PHONE: Optional[bool] = None
    FLAG_EMAIL: Optional[bool] = None
    OCCUPATION_TYPE: Optional[str] = None
    REGION_RATING_CLIENT_W_CITY: Optional[int] = None
    WEEKDAY_APPR_PROCESS_START: Optional[str] = None
    HOUR_APPR_PROCESS_START: Optional[int] = None
    REG_REGION_NOT_LIVE_REGION: Optional[bool] = None
    REG_REGION_NOT_WORK_REGION: Optional[bool] = None
    LIVE_REGION_NOT_WORK_REGION: Optional[bool] = None
    REG_CITY_NOT_LIVE_CITY: Optional[bool] = None
    REG_CITY_NOT_WORK_CITY: Optional[bool] = None
    LIVE_CITY_NOT_WORK_CITY: Optional[bool] = None
    ORGANIZATION_TYPE: Optional[str] = None
    EXT_SOURCE_1: Optional[float] = None
    EXT_SOURCE_2: Optional[float] = None
    EXT_SOURCE_3: Optional[float] = None
    BASEMENTAREA_AVG: Optional[float] = None
    ELEVATORS_AVG: Optional[float] = None
    ENTRANCES_AVG: Optional[float] = None
    FLOORSMAX_AVG: Optional[float] = None
    NONLIVINGAPARTMENTS_AVG: Optional[float] = None
    NONLIVINGAREA_AVG: Optional[float] = None
    YEARS_BEGINEXPLUATATION_MEDI: Optional[float] = None
    YEARS_BUILD_MEDI: Optional[float] = None
    COMMONAREA_MEDI: Optional[float] = None
    LANDAREA_MEDI: Optional[float] = None
    FONDKAPREMONT_MODE: Optional[str] = None
    HOUSETYPE_MODE: Optional[str] = None
    WALLSMATERIAL_MODE: Optional[str] = None
    EMERGENCYSTATE_MODE: Optional[str] = None
    OBS_30_CNT_SOCIAL_CIRCLE: Optional[float] = None
    DEF_30_CNT_SOCIAL_CIRCLE: Optional[float] = None
    DAYS_LAST_PHONE_CHANGE: Optional[float] = None
    FLAG_DOCUMENT_2: Optional[bool] = None
    FLAG_DOCUMENT_3: Optional[bool] = None
    FLAG_DOCUMENT_4: Optional[bool] = None
    FLAG_DOCUMENT_5: Optional[bool] = None
    FLAG_DOCUMENT_6: Optional[bool] = None
    FLAG_DOCUMENT_7: Optional[bool] = None
    FLAG_DOCUMENT_8: Optional[bool] = None
    FLAG_DOCUMENT_9: Optional[bool] = None
    FLAG_DOCUMENT_10: Optional[bool] = None
    FLAG_DOCUMENT_11: Optional[bool] = None
    FLAG_DOCUMENT_12: Optional[bool] = None
    FLAG_DOCUMENT_13: Optional[bool] = None
    FLAG_DOCUMENT_14: Optional[bool] = None
    FLAG_DOCUMENT_15: Optional[bool] = None
    FLAG_DOCUMENT_16: Optional[bool] = None
    FLAG_DOCUMENT_17: Optional[bool] = None
    FLAG_DOCUMENT_18: Optional[bool] = None
    FLAG_DOCUMENT_19: Optional[bool] = None
    FLAG_DOCUMENT_20: Optional[bool] = None
    FLAG_DOCUMENT_21: Optional[bool] = None
    AMT_REQ_CREDIT_BUREAU_HOUR: Optional[float] = None
    AMT_REQ_CREDIT_BUREAU_DAY: Optional[float] = None
    AMT_REQ_CREDIT_BUREAU_WEEK: Optional[float] = None
    AMT_REQ_CREDIT_BUREAU_MON: Optional[float] = None
    AMT_REQ_CREDIT_BUREAU_QRT: Optional[float] = None
    BUREAU_SK_ID_BUREAU_max: Optional[float] = None
    BUREAU_DAYS_CREDIT_mean: Optional[float] = None
    BUREAU_DAYS_CREDIT_max: Optional[float] = None
    BUREAU_DAYS_CREDIT_min: Optional[float] = None
    BUREAU_CREDIT_DAY_OVERDUE_mean: Optional[float] = None
    BUREAU_CREDIT_DAY_OVERDUE_sum: Optional[float] = None
    BUREAU_DAYS_CREDIT_ENDDATE_mean: Optional[float] = None
    BUREAU_DAYS_CREDIT_ENDDATE_max: Optional[float] = None
    BUREAU_DAYS_CREDIT_ENDDATE_min: Optional[float] = None
    BUREAU_DAYS_CREDIT_ENDDATE_sum: Optional[float] = None
    BUREAU_DAYS_ENDDATE_FACT_max: Optional[float] = None
    BUREAU_DAYS_ENDDATE_FACT_sum: Optional[float] = None
    BUREAU_AMT_CREDIT_MAX_OVERDUE_max: Optional[float] = None
    BUREAU_CNT_CREDIT_PROLONG_max: Optional[float] = None
    BUREAU_CNT_CREDIT_PROLONG_sum: Optional[float] = None
    BUREAU_AMT_CREDIT_SUM_mean: Optional[float] = None
    BUREAU_AMT_CREDIT_SUM_min: Optional[float] = None
    BUREAU_AMT_CREDIT_SUM_sum: Optional[float] = None
    BUREAU_AMT_CREDIT_SUM_DEBT_max: Optional[float] = None
    BUREAU_AMT_CREDIT_SUM_DEBT_sum: Optional[float] = None
    BUREAU_AMT_CREDIT_SUM_LIMIT_mean: Optional[float] = None
    BUREAU_AMT_CREDIT_SUM_LIMIT_sum: Optional[float] = None
    BUREAU_AMT_CREDIT_SUM_OVERDUE_max: Optional[float] = None
    BUREAU_AMT_CREDIT_SUM_OVERDUE_sum: Optional[float] = None
    BUREAU_AMT_ANNUITY_mean: Optional[float] = None
    BUREAU_AMT_ANNUITY_min: Optional[float] = None
    BUREAU_MONTHS_BALANCE_max: Optional[float] = None
    BUREAU_CREDIT_ACTIVE_NUNIQUE: Optional[float] = None
    BUREAU_CREDIT_CURRENCY_NUNIQUE: Optional[float] = None
    BUREAU_CREDIT_TYPE_NUNIQUE: Optional[float] = None
    BUREAU_STATUS_NUNIQUE: Optional[float] = None
    BUREAU_CREDIT_ACTIVE_Bad_debt: Optional[float] = None
    BUREAU_CREDIT_ACTIVE_Sold: Optional[float] = None
    BUREAU_CREDIT_CURRENCY_currency_2: Optional[float] = None
    BUREAU_CREDIT_CURRENCY_currency_3: Optional[float] = None
    BUREAU_CREDIT_CURRENCY_currency_4: Optional[float] = None
    BUREAU_CREDIT_TYPE_Another_type_of_loan: Optional[float] = None
    BUREAU_CREDIT_TYPE_Car_loan: Optional[float] = None
    BUREAU_CREDIT_TYPE_Cash_loan__non_earmarked_: Optional[float] = None
    BUREAU_CREDIT_TYPE_Interbank_credit: Optional[bool] = None
    BUREAU_CREDIT_TYPE_Loan_for_business_development: Optional[float] = None
    BUREAU_CREDIT_TYPE_Loan_for_purchase_of_shares__margin_lending_: Optional[bool] = None
    BUREAU_CREDIT_TYPE_Loan_for_the_purchase_of_equipment: Optional[float] = None
    BUREAU_CREDIT_TYPE_Loan_for_working_capital_replenishment: Optional[float] = None
    BUREAU_CREDIT_TYPE_Microloan: Optional[float] = None
    BUREAU_CREDIT_TYPE_Mobile_operator_loan: Optional[bool] = None
    BUREAU_CREDIT_TYPE_Mortgage: Optional[float] = None
    BUREAU_CREDIT_TYPE_Real_estate_loan: Optional[float] = None
    BUREAU_CREDIT_TYPE_Unknown_type_of_loan: Optional[float] = None
    BUREAU_STATUS_1: Optional[float] = None
    BUREAU_STATUS_2: Optional[float] = None
    BUREAU_STATUS_4: Optional[float] = None
    BUREAU_STATUS_5: Optional[float] = None
    PREV_AMT_ANNUITY_mean: Optional[float] = None
    PREV_AMT_ANNUITY_min: Optional[float] = None
    PREV_AMT_APPLICATION_min: Optional[float] = None
    PREV_AMT_DOWN_PAYMENT_sum: Optional[float] = None
    PREV_HOUR_APPR_PROCESS_START_mean: Optional[float] = None
    PREV_NFLAG_LAST_APPL_IN_DAY_max: Optional[bool] = None
    PREV_NFLAG_LAST_APPL_IN_DAY_min: Optional[bool] = None
    PREV_RATE_DOWN_PAYMENT_max: Optional[float] = None
    PREV_RATE_DOWN_PAYMENT_sum: Optional[float] = None
    PREV_RATE_INTEREST_PRIMARY_max: Optional[float] = None
    PREV_RATE_INTEREST_PRIMARY_sum: Optional[float] = None
    PREV_RATE_INTEREST_PRIVILEGED_max: Optional[float] = None
    PREV_SELLERPLACE_AREA_sum: Optional[float] = None
    PREV_CNT_PAYMENT_max: Optional[float] = None
    PREV_CNT_PAYMENT_min: Optional[float] = None
    PREV_DAYS_FIRST_DRAWING_mean: Optional[float] = None
    PREV_DAYS_FIRST_DRAWING_max: Optional[float] = None
    PREV_DAYS_FIRST_DRAWING_sum: Optional[float] = None
    PREV_DAYS_FIRST_DUE_min: Optional[float] = None
    PREV_DAYS_LAST_DUE_mean: Optional[float] = None
    PREV_DAYS_LAST_DUE_min: Optional[float] = None
    PREV_DAYS_TERMINATION_mean: Optional[float] = None
    PREV_NFLAG_INSURED_ON_APPROVAL_sum: Optional[float] = None
    PREV_NAME_PAYMENT_TYPE_NUNIQUE: Optional[float] = None
    PREV_CODE_REJECT_REASON_NUNIQUE: Optional[float] = None
    PREV_NAME_TYPE_SUITE_NUNIQUE: Optional[float] = None
    PREV_NAME_CLIENT_TYPE_NUNIQUE: Optional[float] = None
    PREV_NAME_PRODUCT_TYPE_NUNIQUE: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_NUNIQUE: Optional[float] = None
    PREV_NAME_CONTRACT_TYPE_XNA: Optional[float] = None
    PREV_WEEKDAY_APPR_PROCESS_START_FRIDAY: Optional[float] = None
    PREV_WEEKDAY_APPR_PROCESS_START_MONDAY: Optional[float] = None
    PREV_WEEKDAY_APPR_PROCESS_START_SATURDAY: Optional[float] = None
    PREV_WEEKDAY_APPR_PROCESS_START_SUNDAY: Optional[float] = None
    PREV_WEEKDAY_APPR_PROCESS_START_THURSDAY: Optional[float] = None
    PREV_WEEKDAY_APPR_PROCESS_START_TUESDAY: Optional[float] = None
    PREV_WEEKDAY_APPR_PROCESS_START_WEDNESDAY: Optional[float] = None
    PREV_FLAG_LAST_APPL_PER_CONTRACT_N: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Building_a_house_or_an_annex: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Business_development: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_garage: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_holiday_home___land: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_home: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_new_car: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_used_car: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Car_repairs: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Education: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Everyday_expenses: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Furniture: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Gasification___water_supply: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Hobby: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Journey: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Medicine: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Money_for_a_third_person: Optional[bool] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Other: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Payments_on_other_loans: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Purchase_of_electronic_equipment: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Refusal_to_name_the_goal: Optional[bool] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Repairs: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Urgent_needs: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Wedding___gift___holiday: Optional[float] = None
    PREV_NAME_CONTRACT_STATUS_Refused: Optional[float] = None
    PREV_NAME_CONTRACT_STATUS_Unused_offer: Optional[float] = None
    PREV_NAME_PAYMENT_TYPE_Cashless_from_the_account_of_the_employer: Optional[float] = None
    PREV_NAME_PAYMENT_TYPE_Non_cash_from_your_account: Optional[float] = None
    PREV_CODE_REJECT_REASON_LIMIT: Optional[float] = None
    PREV_CODE_REJECT_REASON_SCO: Optional[float] = None
    PREV_CODE_REJECT_REASON_SCOFR: Optional[float] = None
    PREV_CODE_REJECT_REASON_SYSTEM: Optional[float] = None
    PREV_CODE_REJECT_REASON_VERIF: Optional[float] = None
    PREV_CODE_REJECT_REASON_XNA: Optional[float] = None
    PREV_NAME_TYPE_SUITE_Children: Optional[float] = None
    PREV_NAME_TYPE_SUITE_Family: Optional[float] = None
    PREV_NAME_TYPE_SUITE_Group_of_people: Optional[float] = None
    PREV_NAME_TYPE_SUITE_Other_A: Optional[float] = None
    PREV_NAME_TYPE_SUITE_Other_B: Optional[float] = None
    PREV_NAME_TYPE_SUITE_Spouse__partner: Optional[float] = None
    PREV_NAME_CLIENT_TYPE_New: Optional[float] = None
    PREV_NAME_CLIENT_TYPE_Refreshed: Optional[float] = None
    PREV_NAME_CLIENT_TYPE_XNA: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Additional_Service: Optional[bool] = None
    PREV_NAME_GOODS_CATEGORY_Animals: Optional[bool] = None
    PREV_NAME_GOODS_CATEGORY_Audio_Video: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Auto_Accessories: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Clothing_and_Accessories: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Computers: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Consumer_Electronics: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Direct_Sales: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Education: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Fitness: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Gardening: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Homewares: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Insurance: Optional[bool] = None
    PREV_NAME_GOODS_CATEGORY_Jewelry: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Medical_Supplies: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Medicine: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Office_Appliances: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Other: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Photo___Cinema_Equipment: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Sport_and_Leisure: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Tourism: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Vehicles: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Weapon: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_XNA: Optional[float] = None
    PREV_NAME_PORTFOLIO_POS: Optional[float] = None
    PREV_NAME_PRODUCT_TYPE_walk_in: Optional[float] = None
    PREV_CHANNEL_TYPE_AP___Cash_loan_: Optional[float] = None
    PREV_CHANNEL_TYPE_Car_dealer: Optional[float] = None
    PREV_CHANNEL_TYPE_Channel_of_corporate_sales: Optional[float] = None
    PREV_CHANNEL_TYPE_Contact_center: Optional[float] = None
    PREV_CHANNEL_TYPE_Regional___Local: Optional[float] = None
    PREV_CHANNEL_TYPE_Stone: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_Auto_technology: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_Connectivity: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_Construction: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_Industry: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_Jewelry: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_MLM_partners: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_Tourism: Optional[float] = None
    PREV_NAME_YIELD_GROUP_XNA: Optional[float] = None
    PREV_NAME_YIELD_GROUP_low_action: Optional[float] = None
    PREV_NAME_YIELD_GROUP_low_normal: Optional[float] = None
    PREV_PRODUCT_COMBINATION_Card_Street: Optional[float] = None
    PREV_PRODUCT_COMBINATION_Cash_Street__high: Optional[float] = None
    PREV_PRODUCT_COMBINATION_Cash_Street__low: Optional[float] = None
    PREV_PRODUCT_COMBINATION_Cash_Street__middle: Optional[float] = None
    PREV_PRODUCT_COMBINATION_Cash_X_Sell__high: Optional[float] = None
    PREV_PRODUCT_COMBINATION_Cash_X_Sell__middle: Optional[float] = None
    PREV_PRODUCT_COMBINATION_POS_industry_with_interest: Optional[float] = None
    PREV_PRODUCT_COMBINATION_POS_industry_without_interest: Optional[float] = None
    PREV_PRODUCT_COMBINATION_POS_mobile_without_interest: Optional[float] = None
    PREV_PRODUCT_COMBINATION_POS_other_with_interest: Optional[float] = None
    PREV_PRODUCT_COMBINATION_POS_others_without_interest: Optional[float] = None
    INST_PAY_NUM_INSTALMENT_VERSION_mean: Optional[float] = None
    INST_PAY_DAYS_ENTRY_PAYMENT_mean: Optional[float] = None
    INST_PAY_DAYS_ENTRY_PAYMENT_min: Optional[float] = None
    INST_PAY_AMT_PAYMENT_mean: Optional[float] = None
    INST_PAY_AMT_PAYMENT_min: Optional[float] = None
    INST_PAY_AMT_PAYMENT_sum: Optional[float] = None
    INST_PAY_PAYMENT_DELAY_mean: Optional[float] = None
    INST_PAY_PAYMENT_DELAY_max: Optional[float] = None
    INST_PAY_PAYMENT_DELAY_min: Optional[float] = None
    INST_PAY_PAYMENT_DELAY_sum: Optional[float] = None
    INST_PAY_PAYMENT_RATIO_mean: Optional[float] = None
    INST_PAY_PAYMENT_RATIO_min: Optional[float] = None
    CC_MONTHS_BALANCE_mean: Optional[float] = None
    CC_MONTHS_BALANCE_max: Optional[float] = None
    CC_AMT_BALANCE_mean: Optional[float] = None
    CC_AMT_CREDIT_LIMIT_ACTUAL_max: Optional[float] = None
    CC_AMT_CREDIT_LIMIT_ACTUAL_sum: Optional[float] = None
    CC_AMT_DRAWINGS_ATM_CURRENT_mean: Optional[float] = None
    CC_AMT_DRAWINGS_ATM_CURRENT_sum: Optional[float] = None
    CC_AMT_DRAWINGS_CURRENT_mean: Optional[float] = None
    CC_AMT_DRAWINGS_CURRENT_max: Optional[float] = None
    CC_AMT_DRAWINGS_CURRENT_min: Optional[float] = None
    CC_AMT_DRAWINGS_POS_CURRENT_min: Optional[float] = None
    CC_AMT_INST_MIN_REGULARITY_min: Optional[float] = None
    CC_AMT_PAYMENT_CURRENT_min: Optional[float] = None
    CC_AMT_PAYMENT_TOTAL_CURRENT_max: Optional[float] = None
    CC_CNT_DRAWINGS_ATM_CURRENT_mean: Optional[float] = None
    CC_CNT_DRAWINGS_ATM_CURRENT_min: Optional[float] = None
    CC_CNT_DRAWINGS_ATM_CURRENT_sum: Optional[float] = None
    CC_CNT_DRAWINGS_CURRENT_max: Optional[float] = None
    CC_CNT_DRAWINGS_CURRENT_min: Optional[float] = None
    CC_CNT_DRAWINGS_OTHER_CURRENT_mean: Optional[float] = None
    CC_CNT_DRAWINGS_OTHER_CURRENT_min: Optional[bool] = None
    CC_SK_DPD_max: Optional[float] = None
    CC_SK_DPD_DEF_max: Optional[float] = None
    CC_UTILIZATION_mean: Optional[float] = None
    CC_UTILIZATION_max: Optional[float] = None
    CC_UTILIZATION_min: Optional[float] = None
    CC_PAYMENT_RATIO_max: Optional[float] = None
    CC_PAYMENT_RATIO_min: Optional[float] = None
    CC_NAME_CONTRACT_STATUS_NUNIQUE: Optional[float] = None
    CC_NAME_CONTRACT_STATUS_Approved: Optional[bool] = None
    CC_NAME_CONTRACT_STATUS_Completed: Optional[float] = None
    CC_NAME_CONTRACT_STATUS_Refused: Optional[bool] = None
    CC_NAME_CONTRACT_STATUS_Sent_proposal: Optional[bool] = None
    CC_NAME_CONTRACT_STATUS_Signed: Optional[float] = None
    POS_CNT_INSTALMENT_min: Optional[float] = None
    POS_CNT_INSTALMENT_FUTURE_min: Optional[float] = None
    POS_SK_DPD_mean: Optional[float] = None
    POS_SK_DPD_min: Optional[float] = None
    POS_SK_DPD_DEF_max: Optional[float] = None
    POS_SK_DPD_DEF_min: Optional[bool] = None
    POS_NAME_CONTRACT_STATUS_NUNIQUE: Optional[float] = None
    POS_NAME_CONTRACT_STATUS_Amortized_debt: Optional[float] = None
    POS_NAME_CONTRACT_STATUS_Approved: Optional[float] = None
    POS_NAME_CONTRACT_STATUS_Canceled: Optional[bool] = None
    POS_NAME_CONTRACT_STATUS_Completed: Optional[float] = None
    POS_NAME_CONTRACT_STATUS_Returned_to_the_store: Optional[float] = None
    POS_NAME_CONTRACT_STATUS_Signed: Optional[float] = None
    POS_NAME_CONTRACT_STATUS_XNA: Optional[bool] = None

    # --- Configuration du modèle ---
    model_config = {
        "json_schema_extra": {
            "example": {
                "SK_ID_CURR": 412612,
                "NAME_CONTRACT_TYPE": "Cash loans",
                "CODE_GENDER": "F",
                "FLAG_OWN_CAR": "N",
                "FLAG_OWN_REALTY": "Y",
                "CNT_CHILDREN": 0,
                "AMT_INCOME_TOTAL": 135000.0,
                "AMT_GOODS_PRICE": 729000.0,
                "NAME_TYPE_SUITE": "Unaccompanied",
                "NAME_INCOME_TYPE": "Pensioner",
                "NAME_EDUCATION_TYPE": "Secondary / secondary special",
                "NAME_FAMILY_STATUS": "Single / not married",
                "NAME_HOUSING_TYPE": "House / apartment",
                "REGION_POPULATION_RELATIVE": 0.026392,
                "DAYS_BIRTH": -23259,
                "DAYS_EMPLOYED": 365243,
                "DAYS_REGISTRATION": -5382.0,
                "DAYS_ID_PUBLISH": -4284,
                "OWN_CAR_AGE": None,
                "FLAG_MOBIL": True,
                "FLAG_EMP_PHONE": False,
                "FLAG_WORK_PHONE": False,
                "FLAG_CONT_MOBILE": True,
                "FLAG_PHONE": True,
                "FLAG_EMAIL": False,
                "OCCUPATION_TYPE": None,
                "REGION_RATING_CLIENT_W_CITY": 2,
                "WEEKDAY_APPR_PROCESS_START": "THURSDAY",
                "HOUR_APPR_PROCESS_START": 11,
                "REG_REGION_NOT_LIVE_REGION": False,
                "REG_REGION_NOT_WORK_REGION": False,
                "LIVE_REGION_NOT_WORK_REGION": False,
                "REG_CITY_NOT_LIVE_CITY": False,
                "REG_CITY_NOT_WORK_CITY": False,
                "LIVE_CITY_NOT_WORK_CITY": False,
                "ORGANIZATION_TYPE": "XNA",
                "EXT_SOURCE_1": None,
                "EXT_SOURCE_2": 0.7416015408659962,
                "EXT_SOURCE_3": 0.6832688314232291,
                "BASEMENTAREA_AVG": 0.1747,
                "ELEVATORS_AVG": 0.0,
                "ENTRANCES_AVG": 0.4828,
                "FLOORSMAX_AVG": 0.1667,
                "NONLIVINGAPARTMENTS_AVG": None,
                "NONLIVINGAREA_AVG": 0.2384,
                "YEARS_BEGINEXPLUATATION_MEDI": 0.9796,
                "YEARS_BUILD_MEDI": None,
                "COMMONAREA_MEDI": None,
                "LANDAREA_MEDI": 0.1482,
                "FONDKAPREMONT_MODE": None,
                "HOUSETYPE_MODE": "block of flats",
                "WALLSMATERIAL_MODE": "Panel",
                "EMERGENCYSTATE_MODE": "No",
                "OBS_30_CNT_SOCIAL_CIRCLE": 2.0,
                "DEF_30_CNT_SOCIAL_CIRCLE": 0.0,
                "DAYS_LAST_PHONE_CHANGE": -1506.0,
                "FLAG_DOCUMENT_2": False,
                "FLAG_DOCUMENT_3": True,
                "FLAG_DOCUMENT_4": False,
                "FLAG_DOCUMENT_5": False,
                "FLAG_DOCUMENT_6": False,
                "FLAG_DOCUMENT_7": False,
                "FLAG_DOCUMENT_8": False,
                "FLAG_DOCUMENT_9": False,
                "FLAG_DOCUMENT_10": False,
                "FLAG_DOCUMENT_11": False,
                "FLAG_DOCUMENT_12": False,
                "FLAG_DOCUMENT_13": False,
                "FLAG_DOCUMENT_14": False,
                "FLAG_DOCUMENT_15": False,
                "FLAG_DOCUMENT_16": False,
                "FLAG_DOCUMENT_17": False,
                "FLAG_DOCUMENT_18": False,
                "FLAG_DOCUMENT_19": False,
                "FLAG_DOCUMENT_20": False,
                "FLAG_DOCUMENT_21": False,
                "AMT_REQ_CREDIT_BUREAU_HOUR": 0.0,
                "AMT_REQ_CREDIT_BUREAU_DAY": 0.0,
                "AMT_REQ_CREDIT_BUREAU_WEEK": 0.0,
                "AMT_REQ_CREDIT_BUREAU_MON": 0.0,
                "AMT_REQ_CREDIT_BUREAU_QRT": 0.0,
                "BUREAU_SK_ID_BUREAU_max": 6302024.0,
                "BUREAU_DAYS_CREDIT_mean": -1279.759493670886,
                "BUREAU_DAYS_CREDIT_max": -869.0,
                "BUREAU_DAYS_CREDIT_min": -1518.0,
                "BUREAU_CREDIT_DAY_OVERDUE_mean": 0.0,
                "BUREAU_CREDIT_DAY_OVERDUE_sum": 0.0,
                "BUREAU_DAYS_CREDIT_ENDDATE_mean": -788.0,
                "BUREAU_DAYS_CREDIT_ENDDATE_max": -788.0,
                "BUREAU_DAYS_CREDIT_ENDDATE_min": -788.0,
                "BUREAU_DAYS_CREDIT_ENDDATE_sum": -39400.0,
                "BUREAU_DAYS_ENDDATE_FACT_max": -822.0,
                "BUREAU_DAYS_ENDDATE_FACT_sum": -41100.0,
                "BUREAU_AMT_CREDIT_MAX_OVERDUE_max": 0.0,
                "BUREAU_CNT_CREDIT_PROLONG_max": 0.0,
                "BUREAU_CNT_CREDIT_PROLONG_sum": 0.0,
                "BUREAU_AMT_CREDIT_SUM_mean": 251276.58227848102,
                "BUREAU_AMT_CREDIT_SUM_min": 233892.0,
                "BUREAU_AMT_CREDIT_SUM_sum": 19850850.0,
                "BUREAU_AMT_CREDIT_SUM_DEBT_max": 0.0,
                "BUREAU_AMT_CREDIT_SUM_DEBT_sum": 0.0,
                "BUREAU_AMT_CREDIT_SUM_LIMIT_mean": 103243.67088607595,
                "BUREAU_AMT_CREDIT_SUM_LIMIT_sum": 8156250.0,
                "BUREAU_AMT_CREDIT_SUM_OVERDUE_max": 0.0,
                "BUREAU_AMT_CREDIT_SUM_OVERDUE_sum": 0.0,
                "BUREAU_AMT_ANNUITY_mean": 28125.0,
                "BUREAU_AMT_ANNUITY_min": 28125.0,
                "BUREAU_MONTHS_BALANCE_max": 0.0,
                "BUREAU_CREDIT_ACTIVE_NUNIQUE": 2.0,
                "BUREAU_CREDIT_CURRENCY_NUNIQUE": 1.0,
                "BUREAU_CREDIT_TYPE_NUNIQUE": 2.0,
                "BUREAU_STATUS_NUNIQUE": 3.0,
                "BUREAU_CREDIT_ACTIVE_Bad_debt": 0.0,
                "BUREAU_CREDIT_ACTIVE_Sold": 0.0,
                "BUREAU_CREDIT_CURRENCY_currency_2": 0.0,
                "BUREAU_CREDIT_CURRENCY_currency_3": 0.0,
                "BUREAU_CREDIT_CURRENCY_currency_4": 0.0,
                "BUREAU_CREDIT_TYPE_Another_type_of_loan": 0.0,
                "BUREAU_CREDIT_TYPE_Car_loan": 0.0,
                "BUREAU_CREDIT_TYPE_Cash_loan__non_earmarked_": 0.0,
                "BUREAU_CREDIT_TYPE_Interbank_credit": 0.0,
                "BUREAU_CREDIT_TYPE_Loan_for_business_development": 0.0,
                "BUREAU_CREDIT_TYPE_Loan_for_purchase_of_shares__margin_lending_": 0.0,
                "BUREAU_CREDIT_TYPE_Loan_for_the_purchase_of_equipment": 0.0,
                "BUREAU_CREDIT_TYPE_Loan_for_working_capital_replenishment": 0.0,
                "BUREAU_CREDIT_TYPE_Microloan": 0.0,
                "BUREAU_CREDIT_TYPE_Mobile_operator_loan": 0.0,
                "BUREAU_CREDIT_TYPE_Mortgage": 0.0,
                "BUREAU_CREDIT_TYPE_Real_estate_loan": 0.0,
                "BUREAU_CREDIT_TYPE_Unknown_type_of_loan": 0.0,
                "BUREAU_STATUS_1": 0.0,
                "BUREAU_STATUS_2": 0.0,
                "BUREAU_STATUS_4": 0.0,
                "BUREAU_STATUS_5": 0.0,
                "PREV_AMT_ANNUITY_mean": 11156.58,
                "PREV_AMT_ANNUITY_min": 11156.58,
                "PREV_AMT_APPLICATION_min": 93600.0,
                "PREV_AMT_DOWN_PAYMENT_sum": 0.0,
                "PREV_HOUR_APPR_PROCESS_START_mean": 18.0,
                "PREV_NFLAG_LAST_APPL_IN_DAY_max": 1.0,
                "PREV_NFLAG_LAST_APPL_IN_DAY_min": 1.0,
                "PREV_RATE_DOWN_PAYMENT_max": 0.0,
                "PREV_RATE_DOWN_PAYMENT_sum": 0.0,
                "PREV_RATE_INTEREST_PRIMARY_max": None,
                "PREV_RATE_INTEREST_PRIMARY_sum": 0.0,
                "PREV_RATE_INTEREST_PRIVILEGED_max": None,
                "PREV_SELLERPLACE_AREA_sum": 21.0,
                "PREV_CNT_PAYMENT_max": 10.0,
                "PREV_CNT_PAYMENT_min": 10.0,
                "PREV_DAYS_FIRST_DRAWING_mean": 365243.0,
                "PREV_DAYS_FIRST_DRAWING_max": 365243.0,
                "PREV_DAYS_FIRST_DRAWING_sum": 365243.0,
                "PREV_DAYS_FIRST_DUE_min": -1475.0,
                "PREV_DAYS_LAST_DUE_mean": -1205.0,
                "PREV_DAYS_LAST_DUE_min": -1205.0,
                "PREV_DAYS_TERMINATION_mean": -1200.0,
                "PREV_NFLAG_INSURED_ON_APPROVAL_sum": 0.0,
                "PREV_NAME_PAYMENT_TYPE_NUNIQUE": 1.0,
                "PREV_CODE_REJECT_REASON_NUNIQUE": 1.0,
                "PREV_NAME_TYPE_SUITE_NUNIQUE": 1.0,
                "PREV_NAME_CLIENT_TYPE_NUNIQUE": 1.0,
                "PREV_NAME_PRODUCT_TYPE_NUNIQUE": 1.0,
                "PREV_NAME_SELLER_INDUSTRY_NUNIQUE": 1.0,
                "PREV_NAME_CONTRACT_TYPE_XNA": 0.0,
                "PREV_WEEKDAY_APPR_PROCESS_START_FRIDAY": 0.0,
                "PREV_WEEKDAY_APPR_PROCESS_START_MONDAY": 0.0,
                "PREV_WEEKDAY_APPR_PROCESS_START_SATURDAY": 0.0,
                "PREV_WEEKDAY_APPR_PROCESS_START_SUNDAY": 0.0,
                "PREV_WEEKDAY_APPR_PROCESS_START_THURSDAY": 0.0,
                "PREV_WEEKDAY_APPR_PROCESS_START_TUESDAY": 0.0,
                "PREV_WEEKDAY_APPR_PROCESS_START_WEDNESDAY": 1.0,
                "PREV_FLAG_LAST_APPL_PER_CONTRACT_N": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Building_a_house_or_an_annex": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Business_development": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_garage": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_holiday_home___land": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_home": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_new_car": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_used_car": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Car_repairs": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Education": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Everyday_expenses": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Furniture": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Gasification___water_supply": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Hobby": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Journey": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Medicine": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Money_for_a_third_person": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Other": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Payments_on_other_loans": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Purchase_of_electronic_equipment": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Refusal_to_name_the_goal": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Repairs": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Urgent_needs": 0.0,
                "PREV_NAME_CASH_LOAN_PURPOSE_Wedding___gift___holiday": 0.0,
                "PREV_NAME_CONTRACT_STATUS_Refused": 0.0,
                "PREV_NAME_CONTRACT_STATUS_Unused_offer": 0.0,
                "PREV_NAME_PAYMENT_TYPE_Cashless_from_the_account_of_the_employer": 0.0,
                "PREV_NAME_PAYMENT_TYPE_Non_cash_from_your_account": 0.0,
                "PREV_CODE_REJECT_REASON_LIMIT": 0.0,
                "PREV_CODE_REJECT_REASON_SCO": 0.0,
                "PREV_CODE_REJECT_REASON_SCOFR": 0.0,
                "PREV_CODE_REJECT_REASON_SYSTEM": 0.0,
                "PREV_CODE_REJECT_REASON_VERIF": 0.0,
                "PREV_CODE_REJECT_REASON_XNA": 0.0,
                "PREV_NAME_TYPE_SUITE_Children": 0.0,
                "PREV_NAME_TYPE_SUITE_Family": 1.0,
                "PREV_NAME_TYPE_SUITE_Group_of_people": 0.0,
                "PREV_NAME_TYPE_SUITE_Other_A": 0.0,
                "PREV_NAME_TYPE_SUITE_Other_B": 0.0,
                "PREV_NAME_TYPE_SUITE_Spouse__partner": 0.0,
                "PREV_NAME_CLIENT_TYPE_New": 1.0,
                "PREV_NAME_CLIENT_TYPE_Refreshed": 0.0,
                "PREV_NAME_CLIENT_TYPE_XNA": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Additional_Service": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Animals": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Audio_Video": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Auto_Accessories": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Clothing_and_Accessories": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Computers": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Consumer_Electronics": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Direct_Sales": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Education": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Fitness": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Gardening": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Homewares": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Insurance": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Jewelry": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Medical_Supplies": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Medicine": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Office_Appliances": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Other": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Photo___Cinema_Equipment": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Sport_and_Leisure": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Tourism": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Vehicles": 0.0,
                "PREV_NAME_GOODS_CATEGORY_Weapon": 0.0,
                "PREV_NAME_GOODS_CATEGORY_XNA": 0.0,
                "PREV_NAME_PORTFOLIO_POS": 1.0,
                "PREV_NAME_PRODUCT_TYPE_walk_in": 0.0,
                "PREV_CHANNEL_TYPE_AP___Cash_loan_": 0.0,
                "PREV_CHANNEL_TYPE_Car_dealer": 0.0,
                "PREV_CHANNEL_TYPE_Channel_of_corporate_sales": 0.0,
                "PREV_CHANNEL_TYPE_Contact_center": 0.0,
                "PREV_CHANNEL_TYPE_Regional___Local": 0.0,
                "PREV_CHANNEL_TYPE_Stone": 1.0,
                "PREV_NAME_SELLER_INDUSTRY_Auto_technology": 0.0,
                "PREV_NAME_SELLER_INDUSTRY_Connectivity": 0.0,
                "PREV_NAME_SELLER_INDUSTRY_Construction": 0.0,
                "PREV_NAME_SELLER_INDUSTRY_Industry": 0.0,
                "PREV_NAME_SELLER_INDUSTRY_Jewelry": 0.0,
                "PREV_NAME_SELLER_INDUSTRY_MLM_partners": 0.0,
                "PREV_NAME_SELLER_INDUSTRY_Tourism": 0.0,
                "PREV_NAME_YIELD_GROUP_XNA": 0.0,
                "PREV_NAME_YIELD_GROUP_low_action": 0.0,
                "PREV_NAME_YIELD_GROUP_low_normal": 0.0,
                "PREV_PRODUCT_COMBINATION_Card_Street": 0.0,
                "PREV_PRODUCT_COMBINATION_Cash_Street__high": 0.0,
                "PREV_PRODUCT_COMBINATION_Cash_Street__low": 0.0,
                "PREV_PRODUCT_COMBINATION_Cash_Street__middle": 0.0,
                "PREV_PRODUCT_COMBINATION_Cash_X_Sell__high": 0.0,
                "PREV_PRODUCT_COMBINATION_Cash_X_Sell__middle": 0.0,
                "PREV_PRODUCT_COMBINATION_POS_industry_with_interest": 1.0,
                "PREV_PRODUCT_COMBINATION_POS_industry_without_interest": 0.0,
                "PREV_PRODUCT_COMBINATION_POS_mobile_without_interest": 0.0,
                "PREV_PRODUCT_COMBINATION_POS_other_with_interest": 0.0,
                "PREV_PRODUCT_COMBINATION_POS_others_without_interest": 0.0,
                "INST_PAY_NUM_INSTALMENT_VERSION_mean": 1.0,
                "INST_PAY_DAYS_ENTRY_PAYMENT_mean": -1345.2,
                "INST_PAY_DAYS_ENTRY_PAYMENT_min": -1485.0,
                "INST_PAY_AMT_PAYMENT_mean": 11150.5725,
                "INST_PAY_AMT_PAYMENT_min": 11096.505,
                "INST_PAY_AMT_PAYMENT_sum": 111505.725,
                "INST_PAY_PAYMENT_DELAY_mean": -5.2,
                "INST_PAY_PAYMENT_DELAY_max": -1.0,
                "INST_PAY_PAYMENT_DELAY_min": -10.0,
                "INST_PAY_PAYMENT_DELAY_sum": -52.0,
                "INST_PAY_PAYMENT_RATIO_mean": 1.0,
                "INST_PAY_PAYMENT_RATIO_min": 1.0,
                "CC_MONTHS_BALANCE_mean": None,
                "CC_MONTHS_BALANCE_max": None,
                "CC_AMT_BALANCE_mean": None,
                "CC_AMT_CREDIT_LIMIT_ACTUAL_max": None,
                "CC_AMT_CREDIT_LIMIT_ACTUAL_sum": None,
                "CC_AMT_DRAWINGS_ATM_CURRENT_mean": None,
                "CC_AMT_DRAWINGS_ATM_CURRENT_sum": None,
                "CC_AMT_DRAWINGS_CURRENT_mean": None,
                "CC_AMT_DRAWINGS_CURRENT_max": None,
                "CC_AMT_DRAWINGS_CURRENT_min": None,
                "CC_AMT_DRAWINGS_POS_CURRENT_min": None,
                "CC_AMT_INST_MIN_REGULARITY_min": None,
                "CC_AMT_PAYMENT_CURRENT_min": None,
                "CC_AMT_PAYMENT_TOTAL_CURRENT_max": None,
                "CC_CNT_DRAWINGS_ATM_CURRENT_mean": None,
                "CC_CNT_DRAWINGS_ATM_CURRENT_min": None,
                "CC_CNT_DRAWINGS_ATM_CURRENT_sum": None,
                "CC_CNT_DRAWINGS_CURRENT_max": None,
                "CC_CNT_DRAWINGS_CURRENT_min": None,
                "CC_CNT_DRAWINGS_OTHER_CURRENT_mean": None,
                "CC_CNT_DRAWINGS_OTHER_CURRENT_min": None,
                "CC_SK_DPD_max": None,
                "CC_SK_DPD_DEF_max": None,
                "CC_UTILIZATION_mean": None,
                "CC_UTILIZATION_max": None,
                "CC_UTILIZATION_min": None,
                "CC_PAYMENT_RATIO_max": None,
                "CC_PAYMENT_RATIO_min": None,
                "CC_NAME_CONTRACT_STATUS_NUNIQUE": None,
                "CC_NAME_CONTRACT_STATUS_Approved": None,
                "CC_NAME_CONTRACT_STATUS_Completed": None,
                "CC_NAME_CONTRACT_STATUS_Refused": None,
                "CC_NAME_CONTRACT_STATUS_Sent_proposal": None,
                "CC_NAME_CONTRACT_STATUS_Signed": None,
                "POS_CNT_INSTALMENT_min": 10.0,
                "POS_CNT_INSTALMENT_FUTURE_min": 0.0,
                "POS_SK_DPD_mean": 0.0,
                "POS_SK_DPD_min": 0.0,
                "POS_SK_DPD_DEF_max": 0.0,
                "POS_SK_DPD_DEF_min": 0.0,
                "POS_NAME_CONTRACT_STATUS_NUNIQUE": 2.0,
                "POS_NAME_CONTRACT_STATUS_Amortized_debt": 0.0,
                "POS_NAME_CONTRACT_STATUS_Approved": 0.0,
                "POS_NAME_CONTRACT_STATUS_Canceled": 0.0,
                "POS_NAME_CONTRACT_STATUS_Completed": 1.0,
                "POS_NAME_CONTRACT_STATUS_Returned_to_the_store": 0.0,
                "POS_NAME_CONTRACT_STATUS_Signed": 0.0,
                "POS_NAME_CONTRACT_STATUS_XNA": 0.0}
        }
    }