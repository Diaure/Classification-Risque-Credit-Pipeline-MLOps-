
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
    BUREAU_CREDIT_ACTIVE_Bad debt: Optional[float] = None
    BUREAU_CREDIT_ACTIVE_Sold: Optional[float] = None
    BUREAU_CREDIT_CURRENCY_currency 2: Optional[float] = None
    BUREAU_CREDIT_CURRENCY_currency 3: Optional[float] = None
    BUREAU_CREDIT_CURRENCY_currency 4: Optional[float] = None
    BUREAU_CREDIT_TYPE_Another type of loan: Optional[float] = None
    BUREAU_CREDIT_TYPE_Car loan: Optional[float] = None
    BUREAU_CREDIT_TYPE_Cash loan (non-earmarked): Optional[float] = None
    BUREAU_CREDIT_TYPE_Interbank credit: Optional[bool] = None
    BUREAU_CREDIT_TYPE_Loan for business development: Optional[float] = None
    BUREAU_CREDIT_TYPE_Loan for purchase of shares (margin lending): Optional[bool] = None
    BUREAU_CREDIT_TYPE_Loan for the purchase of equipment: Optional[float] = None
    BUREAU_CREDIT_TYPE_Loan for working capital replenishment: Optional[float] = None
    BUREAU_CREDIT_TYPE_Microloan: Optional[float] = None
    BUREAU_CREDIT_TYPE_Mobile operator loan: Optional[bool] = None
    BUREAU_CREDIT_TYPE_Mortgage: Optional[float] = None
    BUREAU_CREDIT_TYPE_Real estate loan: Optional[float] = None
    BUREAU_CREDIT_TYPE_Unknown type of loan: Optional[float] = None
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
    PREV_NAME_CASH_LOAN_PURPOSE_Building a house or an annex: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Business development: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Buying a garage: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Buying a holiday home / land: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Buying a home: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Buying a new car: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Buying a used car: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Car repairs: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Education: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Everyday expenses: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Furniture: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Gasification / water supply: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Hobby: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Journey: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Medicine: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Money for a third person: Optional[bool] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Other: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Payments on other loans: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Purchase of electronic equipment: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Refusal to name the goal: Optional[bool] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Repairs: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Urgent needs: Optional[float] = None
    PREV_NAME_CASH_LOAN_PURPOSE_Wedding / gift / holiday: Optional[float] = None
    PREV_NAME_CONTRACT_STATUS_Refused: Optional[float] = None
    PREV_NAME_CONTRACT_STATUS_Unused offer: Optional[float] = None
    PREV_NAME_PAYMENT_TYPE_Cashless from the account of the employer: Optional[float] = None
    PREV_NAME_PAYMENT_TYPE_Non-cash from your account: Optional[float] = None
    PREV_CODE_REJECT_REASON_LIMIT: Optional[float] = None
    PREV_CODE_REJECT_REASON_SCO: Optional[float] = None
    PREV_CODE_REJECT_REASON_SCOFR: Optional[float] = None
    PREV_CODE_REJECT_REASON_SYSTEM: Optional[float] = None
    PREV_CODE_REJECT_REASON_VERIF: Optional[float] = None
    PREV_CODE_REJECT_REASON_XNA: Optional[float] = None
    PREV_NAME_TYPE_SUITE_Children: Optional[float] = None
    PREV_NAME_TYPE_SUITE_Family: Optional[float] = None
    PREV_NAME_TYPE_SUITE_Group of people: Optional[float] = None
    PREV_NAME_TYPE_SUITE_Other_A: Optional[float] = None
    PREV_NAME_TYPE_SUITE_Other_B: Optional[float] = None
    PREV_NAME_TYPE_SUITE_Spouse, partner: Optional[float] = None
    PREV_NAME_CLIENT_TYPE_New: Optional[float] = None
    PREV_NAME_CLIENT_TYPE_Refreshed: Optional[float] = None
    PREV_NAME_CLIENT_TYPE_XNA: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Additional Service: Optional[bool] = None
    PREV_NAME_GOODS_CATEGORY_Animals: Optional[bool] = None
    PREV_NAME_GOODS_CATEGORY_Audio/Video: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Auto Accessories: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Clothing and Accessories: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Computers: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Consumer Electronics: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Direct Sales: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Education: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Fitness: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Gardening: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Homewares: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Insurance: Optional[bool] = None
    PREV_NAME_GOODS_CATEGORY_Jewelry: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Medical Supplies: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Medicine: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Office Appliances: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Other: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Photo / Cinema Equipment: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Sport and Leisure: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Tourism: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Vehicles: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_Weapon: Optional[float] = None
    PREV_NAME_GOODS_CATEGORY_XNA: Optional[float] = None
    PREV_NAME_PORTFOLIO_POS: Optional[float] = None
    PREV_NAME_PRODUCT_TYPE_walk-in: Optional[float] = None
    PREV_CHANNEL_TYPE_AP+ (Cash loan): Optional[float] = None
    PREV_CHANNEL_TYPE_Car dealer: Optional[float] = None
    PREV_CHANNEL_TYPE_Channel of corporate sales: Optional[float] = None
    PREV_CHANNEL_TYPE_Contact center: Optional[float] = None
    PREV_CHANNEL_TYPE_Regional / Local: Optional[float] = None
    PREV_CHANNEL_TYPE_Stone: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_Auto technology: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_Connectivity: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_Construction: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_Industry: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_Jewelry: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_MLM partners: Optional[float] = None
    PREV_NAME_SELLER_INDUSTRY_Tourism: Optional[float] = None
    PREV_NAME_YIELD_GROUP_XNA: Optional[float] = None
    PREV_NAME_YIELD_GROUP_low_action: Optional[float] = None
    PREV_NAME_YIELD_GROUP_low_normal: Optional[float] = None
    PREV_PRODUCT_COMBINATION_Card Street: Optional[float] = None
    PREV_PRODUCT_COMBINATION_Cash Street: high: Optional[float] = None
    PREV_PRODUCT_COMBINATION_Cash Street: low: Optional[float] = None
    PREV_PRODUCT_COMBINATION_Cash Street: middle: Optional[float] = None
    PREV_PRODUCT_COMBINATION_Cash X-Sell: high: Optional[float] = None
    PREV_PRODUCT_COMBINATION_Cash X-Sell: middle: Optional[float] = None
    PREV_PRODUCT_COMBINATION_POS industry with interest: Optional[float] = None
    PREV_PRODUCT_COMBINATION_POS industry without interest: Optional[float] = None
    PREV_PRODUCT_COMBINATION_POS mobile without interest: Optional[float] = None
    PREV_PRODUCT_COMBINATION_POS other with interest: Optional[float] = None
    PREV_PRODUCT_COMBINATION_POS others without interest: Optional[float] = None
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
    CC_NAME_CONTRACT_STATUS_Sent proposal: Optional[bool] = None
    CC_NAME_CONTRACT_STATUS_Signed: Optional[float] = None
    POS_CNT_INSTALMENT_min: Optional[float] = None
    POS_CNT_INSTALMENT_FUTURE_min: Optional[float] = None
    POS_SK_DPD_mean: Optional[float] = None
    POS_SK_DPD_min: Optional[float] = None
    POS_SK_DPD_DEF_max: Optional[float] = None
    POS_SK_DPD_DEF_min: Optional[bool] = None
    POS_NAME_CONTRACT_STATUS_NUNIQUE: Optional[float] = None
    POS_NAME_CONTRACT_STATUS_Amortized debt: Optional[float] = None
    POS_NAME_CONTRACT_STATUS_Approved: Optional[float] = None
    POS_NAME_CONTRACT_STATUS_Canceled: Optional[bool] = None
    POS_NAME_CONTRACT_STATUS_Completed: Optional[float] = None
    POS_NAME_CONTRACT_STATUS_Returned to the store: Optional[float] = None
    POS_NAME_CONTRACT_STATUS_Signed: Optional[float] = None
    POS_NAME_CONTRACT_STATUS_XNA: Optional[bool] = None


    # --- Configuration du modèle ---
    model_config = {
        "json_schema_extra": {
            "example": {
    "SK_ID_CURR": 438651,
    "NAME_CONTRACT_TYPE": "Cash loans",
    "CODE_GENDER": "F",
    "FLAG_OWN_CAR": "N",
    "FLAG_OWN_REALTY": "Y",
    "CNT_CHILDREN": 0,
    "AMT_INCOME_TOTAL": 180000.0,
    "AMT_GOODS_PRICE": 450000.0,
    "NAME_TYPE_SUITE": "Unaccompanied",
    "NAME_INCOME_TYPE": "Working",
    "NAME_EDUCATION_TYPE": "Secondary / secondary special",
    "NAME_FAMILY_STATUS": "Single / not married",
    "NAME_HOUSING_TYPE": "House / apartment",
    "REGION_POPULATION_RELATIVE": 0.007305,
    "DAYS_BIRTH": -21927,
    "DAYS_EMPLOYED": -1498,
    "DAYS_REGISTRATION": -9037.0,
    "DAYS_ID_PUBLISH": -4019,
    "OWN_CAR_AGE": null,
    "FLAG_MOBIL": true,
    "FLAG_EMP_PHONE": true,
    "FLAG_WORK_PHONE": false,
    "FLAG_CONT_MOBILE": true,
    "FLAG_PHONE": false,
    "FLAG_EMAIL": false,
    "OCCUPATION_TYPE": "Laborers",
    "REGION_RATING_CLIENT_W_CITY": 3,
    "WEEKDAY_APPR_PROCESS_START": "FRIDAY",
    "HOUR_APPR_PROCESS_START": 12,
    "REG_REGION_NOT_LIVE_REGION": false,
    "REG_REGION_NOT_WORK_REGION": false,
    "LIVE_REGION_NOT_WORK_REGION": false,
    "REG_CITY_NOT_LIVE_CITY": false,
    "REG_CITY_NOT_WORK_CITY": false,
    "LIVE_CITY_NOT_WORK_CITY": false,
    "ORGANIZATION_TYPE": "Services",
    "EXT_SOURCE_1": 0.2088905681464756,
    "EXT_SOURCE_2": 0.5922952796456947,
    "EXT_SOURCE_3": 0.6195277080511546,
    "BASEMENTAREA_AVG": 0.1474,
    "ELEVATORS_AVG": 0.24,
    "ENTRANCES_AVG": 0.2069,
    "FLOORSMAX_AVG": 0.375,
    "NONLIVINGAPARTMENTS_AVG": 0.0,
    "NONLIVINGAREA_AVG": 0.0,
    "YEARS_BEGINEXPLUATATION_MEDI": 0.9881,
    "YEARS_BUILD_MEDI": 0.8390000000000001,
    "COMMONAREA_MEDI": 0.0981,
    "LANDAREA_MEDI": 0.2119,
    "FONDKAPREMONT_MODE": "reg oper account",
    "HOUSETYPE_MODE": "block of flats",
    "WALLSMATERIAL_MODE": "Panel",
    "EMERGENCYSTATE_MODE": "No",
    "OBS_30_CNT_SOCIAL_CIRCLE": 0.0,
    "DEF_30_CNT_SOCIAL_CIRCLE": 0.0,
    "DAYS_LAST_PHONE_CHANGE": -1972.0,
    "FLAG_DOCUMENT_2": false,
    "FLAG_DOCUMENT_3": true,
    "FLAG_DOCUMENT_4": false,
    "FLAG_DOCUMENT_5": false,
    "FLAG_DOCUMENT_6": false,
    "FLAG_DOCUMENT_7": false,
    "FLAG_DOCUMENT_8": false,
    "FLAG_DOCUMENT_9": false,
    "FLAG_DOCUMENT_10": false,
    "FLAG_DOCUMENT_11": false,
    "FLAG_DOCUMENT_12": false,
    "FLAG_DOCUMENT_13": false,
    "FLAG_DOCUMENT_14": false,
    "FLAG_DOCUMENT_15": false,
    "FLAG_DOCUMENT_16": false,
    "FLAG_DOCUMENT_17": false,
    "FLAG_DOCUMENT_18": false,
    "FLAG_DOCUMENT_19": false,
    "FLAG_DOCUMENT_20": false,
    "FLAG_DOCUMENT_21": false,
    "AMT_REQ_CREDIT_BUREAU_HOUR": 0.0,
    "AMT_REQ_CREDIT_BUREAU_DAY": 0.0,
    "AMT_REQ_CREDIT_BUREAU_WEEK": 0.0,
    "AMT_REQ_CREDIT_BUREAU_MON": 0.0,
    "AMT_REQ_CREDIT_BUREAU_QRT": 3.0,
    "BUREAU_SK_ID_BUREAU_max": 5646157.0,
    "BUREAU_DAYS_CREDIT_mean": -784.0,
    "BUREAU_DAYS_CREDIT_max": -784.0,
    "BUREAU_DAYS_CREDIT_min": -784.0,
    "BUREAU_CREDIT_DAY_OVERDUE_mean": 0.0,
    "BUREAU_CREDIT_DAY_OVERDUE_sum": 0.0,
    "BUREAU_DAYS_CREDIT_ENDDATE_mean": 268.0,
    "BUREAU_DAYS_CREDIT_ENDDATE_max": 268.0,
    "BUREAU_DAYS_CREDIT_ENDDATE_min": 268.0,
    "BUREAU_DAYS_CREDIT_ENDDATE_sum": 6968.0,
    "BUREAU_DAYS_ENDDATE_FACT_max": null,
    "BUREAU_DAYS_ENDDATE_FACT_sum": 0.0,
    "BUREAU_AMT_CREDIT_MAX_OVERDUE_max": null,
    "BUREAU_CNT_CREDIT_PROLONG_max": 0.0,
    "BUREAU_CNT_CREDIT_PROLONG_sum": 0.0,
    "BUREAU_AMT_CREDIT_SUM_mean": 630000.0,
    "BUREAU_AMT_CREDIT_SUM_min": 630000.0,
    "BUREAU_AMT_CREDIT_SUM_sum": 16380000.0,
    "BUREAU_AMT_CREDIT_SUM_DEBT_max": 0.0,
    "BUREAU_AMT_CREDIT_SUM_DEBT_sum": 0.0,
    "BUREAU_AMT_CREDIT_SUM_LIMIT_mean": 0.0,
    "BUREAU_AMT_CREDIT_SUM_LIMIT_sum": 0.0,
    "BUREAU_AMT_CREDIT_SUM_OVERDUE_max": 0.0,
    "BUREAU_AMT_CREDIT_SUM_OVERDUE_sum": 0.0,
    "BUREAU_AMT_ANNUITY_mean": 0.0,
    "BUREAU_AMT_ANNUITY_min": 0.0,
    "BUREAU_MONTHS_BALANCE_max": 0.0,
    "BUREAU_CREDIT_ACTIVE_NUNIQUE": 1.0,
    "BUREAU_CREDIT_CURRENCY_NUNIQUE": 1.0,
    "BUREAU_CREDIT_TYPE_NUNIQUE": 1.0,
    "BUREAU_STATUS_NUNIQUE": 2.0,
    "BUREAU_CREDIT_ACTIVE_Bad debt": 0.0,
    "BUREAU_CREDIT_ACTIVE_Sold": 0.0,
    "BUREAU_CREDIT_CURRENCY_currency 2": 0.0,
    "BUREAU_CREDIT_CURRENCY_currency 3": 0.0,
    "BUREAU_CREDIT_CURRENCY_currency 4": 0.0,
    "BUREAU_CREDIT_TYPE_Another type of loan": 0.0,
    "BUREAU_CREDIT_TYPE_Car loan": 0.0,
    "BUREAU_CREDIT_TYPE_Cash loan (non-earmarked)": 0.0,
    "BUREAU_CREDIT_TYPE_Interbank credit": 0.0,
    "BUREAU_CREDIT_TYPE_Loan for business development": 0.0,
    "BUREAU_CREDIT_TYPE_Loan for purchase of shares (margin lending)": 0.0,
    "BUREAU_CREDIT_TYPE_Loan for the purchase of equipment": 0.0,
    "BUREAU_CREDIT_TYPE_Loan for working capital replenishment": 0.0,
    "BUREAU_CREDIT_TYPE_Microloan": 0.0,
    "BUREAU_CREDIT_TYPE_Mobile operator loan": 0.0,
    "BUREAU_CREDIT_TYPE_Mortgage": 0.0,
    "BUREAU_CREDIT_TYPE_Real estate loan": 0.0,
    "BUREAU_CREDIT_TYPE_Unknown type of loan": 0.0,
    "BUREAU_STATUS_1": 0.0,
    "BUREAU_STATUS_2": 0.0,
    "BUREAU_STATUS_4": 0.0,
    "BUREAU_STATUS_5": 0.0,
    "PREV_AMT_ANNUITY_mean": 21119.00625,
    "PREV_AMT_ANNUITY_min": 3017.925,
    "PREV_AMT_APPLICATION_min": 20191.5,
    "PREV_AMT_DOWN_PAYMENT_sum": 2250.0,
    "PREV_HOUR_APPR_PROCESS_START_mean": 9.625,
    "PREV_NFLAG_LAST_APPL_IN_DAY_max": 1.0,
    "PREV_NFLAG_LAST_APPL_IN_DAY_min": 1.0,
    "PREV_RATE_DOWN_PAYMENT_max": 0.1146411483253588,
    "PREV_RATE_DOWN_PAYMENT_sum": 0.1146411483253588,
    "PREV_RATE_INTEREST_PRIMARY_max": null,
    "PREV_RATE_INTEREST_PRIMARY_sum": 0.0,
    "PREV_RATE_INTEREST_PRIVILEGED_max": null,
    "PREV_SELLERPLACE_AREA_sum": 637.0,
    "PREV_CNT_PAYMENT_max": 36.0,
    "PREV_CNT_PAYMENT_min": 6.0,
    "PREV_DAYS_FIRST_DRAWING_mean": 365243.0,
    "PREV_DAYS_FIRST_DRAWING_max": 365243.0,
    "PREV_DAYS_FIRST_DRAWING_sum": 1826215.0,
    "PREV_DAYS_FIRST_DUE_min": -2549.0,
    "PREV_DAYS_LAST_DUE_mean": -1570.8,
    "PREV_DAYS_LAST_DUE_min": -2219.0,
    "PREV_DAYS_TERMINATION_mean": -1566.0,
    "PREV_NFLAG_INSURED_ON_APPROVAL_sum": 1.0,
    "PREV_NAME_PAYMENT_TYPE_NUNIQUE": 2.0,
    "PREV_CODE_REJECT_REASON_NUNIQUE": 2.0,
    "PREV_NAME_TYPE_SUITE_NUNIQUE": 2.0,
    "PREV_NAME_CLIENT_TYPE_NUNIQUE": 2.0,
    "PREV_NAME_PRODUCT_TYPE_NUNIQUE": 2.0,
    "PREV_NAME_SELLER_INDUSTRY_NUNIQUE": 3.0,
    "PREV_NAME_CONTRACT_TYPE_XNA": 0.0,
    "PREV_WEEKDAY_APPR_PROCESS_START_FRIDAY": 0.0,
    "PREV_WEEKDAY_APPR_PROCESS_START_MONDAY": 0.0,
    "PREV_WEEKDAY_APPR_PROCESS_START_SATURDAY": 0.0,
    "PREV_WEEKDAY_APPR_PROCESS_START_SUNDAY": 1.0,
    "PREV_WEEKDAY_APPR_PROCESS_START_THURSDAY": 4.0,
    "PREV_WEEKDAY_APPR_PROCESS_START_TUESDAY": 3.0,
    "PREV_WEEKDAY_APPR_PROCESS_START_WEDNESDAY": 0.0,
    "PREV_FLAG_LAST_APPL_PER_CONTRACT_N": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Building a house or an annex": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Business development": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Buying a garage": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Buying a holiday home / land": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Buying a home": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Buying a new car": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Buying a used car": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Car repairs": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Education": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Everyday expenses": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Furniture": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Gasification / water supply": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Hobby": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Journey": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Medicine": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Money for a third person": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Other": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Payments on other loans": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Purchase of electronic equipment": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Refusal to name the goal": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Repairs": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Urgent needs": 0.0,
    "PREV_NAME_CASH_LOAN_PURPOSE_Wedding / gift / holiday": 0.0,
    "PREV_NAME_CONTRACT_STATUS_Refused": 2.0,
    "PREV_NAME_CONTRACT_STATUS_Unused offer": 0.0,
    "PREV_NAME_PAYMENT_TYPE_Cashless from the account of the employer": 0.0,
    "PREV_NAME_PAYMENT_TYPE_Non-cash from your account": 0.0,
    "PREV_CODE_REJECT_REASON_LIMIT": 0.0,
    "PREV_CODE_REJECT_REASON_SCO": 0.0,
    "PREV_CODE_REJECT_REASON_SCOFR": 0.0,
    "PREV_CODE_REJECT_REASON_SYSTEM": 0.0,
    "PREV_CODE_REJECT_REASON_VERIF": 0.0,
    "PREV_CODE_REJECT_REASON_XNA": 0.0,
    "PREV_NAME_TYPE_SUITE_Children": 0.0,
    "PREV_NAME_TYPE_SUITE_Family": 1.0,
    "PREV_NAME_TYPE_SUITE_Group of people": 0.0,
    "PREV_NAME_TYPE_SUITE_Other_A": 0.0,
    "PREV_NAME_TYPE_SUITE_Other_B": 0.0,
    "PREV_NAME_TYPE_SUITE_Spouse, partner": 0.0,
    "PREV_NAME_CLIENT_TYPE_New": 0.0,
    "PREV_NAME_CLIENT_TYPE_Refreshed": 2.0,
    "PREV_NAME_CLIENT_TYPE_XNA": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Additional Service": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Animals": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Audio/Video": 1.0,
    "PREV_NAME_GOODS_CATEGORY_Auto Accessories": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Clothing and Accessories": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Computers": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Consumer Electronics": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Direct Sales": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Education": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Fitness": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Gardening": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Homewares": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Insurance": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Jewelry": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Medical Supplies": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Medicine": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Office Appliances": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Other": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Photo / Cinema Equipment": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Sport and Leisure": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Tourism": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Vehicles": 0.0,
    "PREV_NAME_GOODS_CATEGORY_Weapon": 0.0,
    "PREV_NAME_GOODS_CATEGORY_XNA": 6.0,
    "PREV_NAME_PORTFOLIO_POS": 2.0,
    "PREV_NAME_PRODUCT_TYPE_walk-in": 0.0,
    "PREV_CHANNEL_TYPE_AP+ (Cash loan)": 0.0,
    "PREV_CHANNEL_TYPE_Car dealer": 0.0,
    "PREV_CHANNEL_TYPE_Channel of corporate sales": 0.0,
    "PREV_CHANNEL_TYPE_Contact center": 3.0,
    "PREV_CHANNEL_TYPE_Regional / Local": 0.0,
    "PREV_CHANNEL_TYPE_Stone": 0.0,
    "PREV_NAME_SELLER_INDUSTRY_Auto technology": 0.0,
    "PREV_NAME_SELLER_INDUSTRY_Connectivity": 1.0,
    "PREV_NAME_SELLER_INDUSTRY_Construction": 0.0,
    "PREV_NAME_SELLER_INDUSTRY_Industry": 0.0,
    "PREV_NAME_SELLER_INDUSTRY_Jewelry": 0.0,
    "PREV_NAME_SELLER_INDUSTRY_MLM partners": 0.0,
    "PREV_NAME_SELLER_INDUSTRY_Tourism": 0.0,
    "PREV_NAME_YIELD_GROUP_XNA": 0.0,
    "PREV_NAME_YIELD_GROUP_low_action": 0.0,
    "PREV_NAME_YIELD_GROUP_low_normal": 3.0,
    "PREV_PRODUCT_COMBINATION_Card Street": 0.0,
    "PREV_PRODUCT_COMBINATION_Cash Street: high": 0.0,
    "PREV_PRODUCT_COMBINATION_Cash Street: low": 0.0,
    "PREV_PRODUCT_COMBINATION_Cash Street: middle": 2.0,
    "PREV_PRODUCT_COMBINATION_Cash X-Sell: high": 1.0,
    "PREV_PRODUCT_COMBINATION_Cash X-Sell: middle": 1.0,
    "PREV_PRODUCT_COMBINATION_POS industry with interest": 0.0,
    "PREV_PRODUCT_COMBINATION_POS industry without interest": 0.0,
    "PREV_PRODUCT_COMBINATION_POS mobile without interest": 0.0,
    "PREV_PRODUCT_COMBINATION_POS other with interest": 0.0,
    "PREV_PRODUCT_COMBINATION_POS others without interest": 0.0,
    "INST_PAY_NUM_INSTALMENT_VERSION_mean": 1.123076923076923,
    "INST_PAY_DAYS_ENTRY_PAYMENT_mean": -1959.8153846153846,
    "INST_PAY_DAYS_ENTRY_PAYMENT_min": -2544.0,
    "INST_PAY_AMT_PAYMENT_mean": 15510.95376923077,
    "INST_PAY_AMT_PAYMENT_min": 4.5,
    "INST_PAY_AMT_PAYMENT_sum": 1008211.995,
    "INST_PAY_PAYMENT_DELAY_mean": -9.307692307692308,
    "INST_PAY_PAYMENT_DELAY_max": 9.0,
    "INST_PAY_PAYMENT_DELAY_min": -46.0,
    "INST_PAY_PAYMENT_DELAY_sum": -605.0,
    "INST_PAY_PAYMENT_RATIO_mean": 0.7854934814876456,
    "INST_PAY_PAYMENT_RATIO_min": 0.00018625442354255913,
    "CC_MONTHS_BALANCE_mean": null,
    "CC_MONTHS_BALANCE_max": null,
    "CC_AMT_BALANCE_mean": null,
    "CC_AMT_CREDIT_LIMIT_ACTUAL_max": null,
    "CC_AMT_CREDIT_LIMIT_ACTUAL_sum": null,
    "CC_AMT_DRAWINGS_ATM_CURRENT_mean": null,
    "CC_AMT_DRAWINGS_ATM_CURRENT_sum": null,
    "CC_AMT_DRAWINGS_CURRENT_mean": null,
    "CC_AMT_DRAWINGS_CURRENT_max": null,
    "CC_AMT_DRAWINGS_CURRENT_min": null,
    "CC_AMT_DRAWINGS_POS_CURRENT_min": null,
    "CC_AMT_INST_MIN_REGULARITY_min": null,
    "CC_AMT_PAYMENT_CURRENT_min": null,
    "CC_AMT_PAYMENT_TOTAL_CURRENT_max": null,
    "CC_CNT_DRAWINGS_ATM_CURRENT_mean": null,
    "CC_CNT_DRAWINGS_ATM_CURRENT_min": null,
    "CC_CNT_DRAWINGS_ATM_CURRENT_sum": null,
    "CC_CNT_DRAWINGS_CURRENT_max": null,
    "CC_CNT_DRAWINGS_CURRENT_min": null,
    "CC_CNT_DRAWINGS_OTHER_CURRENT_mean": null,
    "CC_CNT_DRAWINGS_OTHER_CURRENT_min": null,
    "CC_SK_DPD_max": null,
    "CC_SK_DPD_DEF_max": null,
    "CC_UTILIZATION_mean": null,
    "CC_UTILIZATION_max": null,
    "CC_UTILIZATION_min": null,
    "CC_PAYMENT_RATIO_max": null,
    "CC_PAYMENT_RATIO_min": null,
    "CC_NAME_CONTRACT_STATUS_NUNIQUE": null,
    "CC_NAME_CONTRACT_STATUS_Approved": null,
    "CC_NAME_CONTRACT_STATUS_Completed": null,
    "CC_NAME_CONTRACT_STATUS_Refused": null,
    "CC_NAME_CONTRACT_STATUS_Sent proposal": null,
    "CC_NAME_CONTRACT_STATUS_Signed": null,
    "POS_CNT_INSTALMENT_min": 2.0,
    "POS_CNT_INSTALMENT_FUTURE_min": 0.0,
    "POS_SK_DPD_mean": 0.0,
    "POS_SK_DPD_min": 0.0,
    "POS_SK_DPD_DEF_max": 0.0,
    "POS_SK_DPD_DEF_min": 0.0,
    "POS_NAME_CONTRACT_STATUS_NUNIQUE": 3.0,
    "POS_NAME_CONTRACT_STATUS_Amortized debt": 0.0,
    "POS_NAME_CONTRACT_STATUS_Approved": 0.0,
    "POS_NAME_CONTRACT_STATUS_Canceled": 0.0,
    "POS_NAME_CONTRACT_STATUS_Completed": 4.0,
    "POS_NAME_CONTRACT_STATUS_Returned to the store": 0.0,
    "POS_NAME_CONTRACT_STATUS_Signed": 2.0,
    "POS_NAME_CONTRACT_STATUS_XNA": 0.0
            }}}