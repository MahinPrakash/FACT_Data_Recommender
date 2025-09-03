db_metadata= [
    {
        "dataset_name": "weekly_sales_crediting_file",
        "variable_the_df_is_stored_in":"weekly_sales_crediting_df",
        "description": "Dataset containing weekly sales crediting information by territory, product, and team for HIV products",
        "columns": {
            "NDC_outlet_ID": {
                "description": "Unique identifier for each NDC outlet in the dataset",
                "type": "string"
            },
            "Territory_ID": {
                "description": "Identifier for the sales territory associated with the NDC outlet",
                "type": "string"
            },
            "product": {
                "description": "Name of the product being sold (e.g., biktarvy, rgmn)",
                "type": "string"
            },
            "product_ID": {
                "description": "Unique identifier for the product",
                "type": "string"
            },
            "team_ID": {
                "description": "Unique identifier for the team responsible for the sales",
                "type": "string"
            },
            "level_ID": {
                "description": "Hierarchy level identifier within the team structure",
                "type": "integer"
            },
            "team": {
                "description": "Name of the team responsible for the product sales",
                "type": "string"
            },
            "period": {
                "description": "Monthly period in YYYYMM format (e.g., 202508 for August 2025)",
                "type": "string"
            },
            "week_id": {
                "description": "Weekly period identifier in the format YYYYWnn (e.g., 2025W01 for Week 1 of 2025)",
                "type": "string"
            },
            "sales": {
                "description": "Number of units sold during the specified week",
                "type": "integer"
            }
        }
    },
    {
        "dataset_name": "IC_goals_data.csv",
        "variable_the_df_is_stored_in":"ic_goals_df",
        "description": "Dataset containing monthly goals for each territory and employee across quarters.",
        "columns": {
            "Territory ID": {
                "description": "Unique identifier for the sales territory",
                "type": "string"
            },
            "Territory Name": {
                "description": "Name of the sales territory",
                "type": "string"
            },
            "Employee Name": {
                "description": "Full name of the employee responsible for the territory",
                "type": "string"
            },
            "Employee ID": {
                "description": "Unique identifier assigned to the employee",
                "type": "string"
            },
            "Quarter": {
                "description": "Quarter of the year associated with the goals",
                "type": "string"
            },
            "Months": {
                "description": "Month within the quarter for which the goals are defined",
                "type": "string"
            },
            "Year": {
                "description": "Year of the performance cycle",
                "type": "integer"
            },
            "Goals TRx": {
                "description": "Goal for the number of transactions (TRx) set for the specified month",
                "type": "integer"
            }
        }
    },
    {
        "dataset_name": "Roster_Data",
        "variable_the_df_is_stored_in":"roster_df",
        "description": "Dataset containing employee roster details including roles, territories, reporting managers, and employment dates.",
        "columns": {
            "EMP_ROLE": {
                "description": "Role of the employee in the organization",
                "type": "string"
            },
            "TERRITORY_ID": {
                "description": "Unique identifier for the sales territory assigned to the employee",
                "type": "string"
            },
            "MANAGER_NAME": {
                "description": "Name of the reporting manager for the employee",
                "type": "string"
            },
            "MANAGER_AREA_ID": {
                "description": "Unique identifier for the manager's area",
                "type": "string"
            },
            "REP STAT DATE": {
                "description": "Start date of the employee in the assigned role or territory",
                "type": "date"
            },
            "REP END DATE": {
                "description": "End date of the employee in the assigned role or territory (blank if active)",
                "type": "date"
            },
            "EMPLOYE_ID": {
                "description": "Unique identifier assigned to the employee",
                "type": "string"
            },
            "EMP_NAME": {
                "description": "Full name of the employee",
                "type": "string"
            }
        }
    },
    {
        "dataset_name": "Zip_To_Terr",
        "variable_the_df_is_stored_in":"zip_to_territory_mapping_df",
        "description": "Dataset mapping ZIP codes to sales territories along with alignment start and end dates.",
        "columns": {
            "ZIP_CODE": {
                "description": "Postal ZIP code mapped to a specific sales territory",
                "type": "string"
            },
            "TERRITORY_ID": {
                "description": "Unique identifier for the sales territory",
                "type": "string"
            },
            "ALLIGNMENT START DATE": {
                "description": "Date when the ZIP code was aligned to the territory",
                "type": "date"
            },
            "ALLIGNMENT END DATE": {
                "description": "Date when the ZIP code alignment ended (blank if currently active)",
                "type": "date"
            }
        }
    },
    {
        "dataset_name": "Territory_Mapping",
        "variable_the_df_is_stored_in":"territory_mapping_df",
        "description": "Dataset mapping healthcare providers (HCPs) to territories, including ZIP codes, product groups, and alignment dates.",
        "columns": {
            "PROVIDER_ID": {
                "description": "Unique identifier for the healthcare provider (e.g., NPI)",
                "type": "string"
            },
            "ZIP_CODE": {
                "description": "Postal ZIP code of the healthcare provider",
                "type": "string"
            },
            "TERRITORY_ID": {
                "description": "Unique identifier for the sales territory",
                "type": "string"
            },
            "PRODUCT_GROUP": {
                "description": "Product group associated with the provider in the territory",
                "type": "string"
            },
            "ALLIGNMENT START DATE": {
                "description": "Date when the provider was aligned to the territory",
                "type": "date"
            },
            "ALLIGNMENT END DATE": {
                "description": "Date when the alignment ended (blank if currently active)",
                "type": "date"
            }
        }
    },
    {
        "dataset_name": "Xponent_Data",
        "variable_the_df_is_stored_in":"xponent_df",
        "description": "Dataset containing prescription transaction details for healthcare providers, including drug information, market, quantities, and payer plan IDs.",
        "columns": {
            "PROVIDER_ID": {
                "description": "Unique identifier for the healthcare provider (e.g., NPI)",
                "type": "string"
            },
            "DATE": {
                "description": "Date of the prescription transaction",
                "type": "date"
            },
            "NDC_CODE": {
                "description": "National Drug Code identifying the specific drug",
                "type": "string"
            },
            "PRODUCT_GROUP": {
                "description": "Product group to which the prescribed drug belongs",
                "type": "string"
            },
            "MARKET": {
                "description": "Therapeutic market category for the drug (e.g., HIV)",
                "type": "string"
            },
            "NRX_TOTAL": {
                "description": "Number of new prescriptions for the drug",
                "type": "integer"
            },
            "TRX_TOTAL": {
                "description": "Total number of prescriptions for the drug",
                "type": "integer"
            },
            "Qty": {
                "description": "Quantity of the drug prescribed in the transaction",
                "type": "integer"
            },
            "PAYER_PLAN ID": {
                "description": "Identifier for the payer plan associated with the prescription",
                "type": "string"
            }
        }
    },
    {
        "dataset_name": "LAAD_Data",
        "variable_the_df_is_stored_in": "laad_df",
        "description": "Dataset containing pharmaceutical claims data for patients, including details on medications (primarily HIV treatments), service dates, providers, quantities, payer plans, product groups, treatment switches, and persistency indicators.",
        "columns": {
            "CLAIM_ID": {
                "description": "Unique identifier for the claim",
                "type": "string"
            },
            "PATIENT_ID": {
                "description": "Unique identifier for the patient",
                "type": "string"
            },
            "NDC_CD": {
                "description": "National Drug Code for the medication",
                "type": "string"
            },
            "SVC_DT": {
                "description": "Service date of the claim (format: dd-mm-yyyy)",
                "type": "date"
            },
            "CLAIM_TYPE": {
                "description": "Type of claim (e.g., PD for prescription drug)",
                "type": "string"
            },
            "DIAGNOSIS_CODE": {
                "description": "Diagnosis code associated with the claim",
                "type": "string"
            },
            "CLAIM_STATUS": {
                "description": "Status of the claim (e.g., S for submitted)",
                "type": "string"
            },
            "PROVIDER_ID": {
                "description": "Unique identifier for the healthcare provider",
                "type": "string"
            },
            "QUANTITY": {
                "description": "Quantity of medication dispensed",
                "type": "integer"
            },
            "PAYER_PLAN_ID": {
                "description": "Identifier for the payer plan",
                "type": "string"
            },
            "PRODUCT_GROUP": {
                "description": "Name of the product group or medication (e.g., Biktarvy, Dovato)",
                "type": "string"
            },
            "SWITCH": {
                "description": "Indicator for medication switch (e.g., 0 for no switch, -1 for switch)",
                "type": "integer"
            },
            "PERSISTENCY": {
                "description": "Persistency indicator (0 or 1, where 1 may indicate persistent use)",
                "type": "integer"
            }
        }
    }
]
