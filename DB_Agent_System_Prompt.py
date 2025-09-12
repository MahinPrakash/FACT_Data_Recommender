db_metadata = [
    {
        "dataset_name": "weekly_sales_crediting_file",
        "variable_the_df_is_stored_in": "weekly_sales_crediting_df",
        "description": "Dataset containing weekly sales crediting information by territory, product, and team for HIV products at a weekly and national level. This dataset must be used for territory vs. national sales and market share analysis",
        "columns": {
            "NDC_outlet_ID": {"description": "Unique identifier for each NDC outlet in the dataset", "type": "string", "variable_type": "Dimension"},
            "Territory_ID": {"description": "Unique ID of the sales territory", "type": "string", "variable_type": "Dimension"},
            "product": {"description": "Name of the product being sold (e.g., biktarvy, rgmn)", "type": "string", "variable_type": "Dimension"},
            "product_ID": {"description": "Unique identifier for the product", "type": "string", "variable_type": "Dimension"},
	    "Role": {"description": "Role of the employee responsible for sales within the hierarchy. At the Territory level it links to Territory_ID, at the Regional level it links to Regional_ID, and at the National level it links to National_ID","type": "string", "variable_type": "Dimension"},
            "team_ID": {"description": "Unique identifier for the team responsible for the sales", "type": "string", "variable_type": "Dimension"},
            "level_ID": {"description": "Hierarchy level identifier within the team structure", "type": "integer", "variable_type": "Dimension"},
            "team": {"description": "Name of the team responsible for the product sales", "type": "string", "variable_type": "Dimension"},
            "period": {"description": "Monthly period in YYYYMM format (e.g., 202508 for August 2025)", "type": "string", "variable_type": "Dimension"},
            "week_id": {"description": "Weekly period identifier in the format YYYYWnn (e.g., 2025W01 for current week,2025W02 previous week)", "type": "string", "variable_type": "Dimension"},
            "sales": {"description": "Number of units sold during the specified week", "type": "integer", "variable_type": "Fact"}
        }
    },
    {
        "dataset_name": "IC_goals_data",
        "variable_the_df_is_stored_in": "ic_goals_df",
        "description": "Dataset containing monthly goals for each territory and employee across quarters.",
        "columns": {
            "Territory_ID": {"description": "Unique identifier for the sales territory", "type": "string", "variable_type": "Dimension"},
            "Territory Name": {"description": "Name of the sales territory", "type": "string", "variable_type": "Dimension"},
            "Employee Name": {"description": "Full name of the employee responsible for the territory", "type": "string", "variable_type": "Dimension"},
            "Employee ID": {"description": "Unique identifier assigned to the employee", "type": "string", "variable_type": "Dimension"},
            "Quarter": {"description": "Quarter of the year associated with the goals", "type": "string", "variable_type": "Dimension"},
            "Months": {"description": "Month within the quarter for which the goals are defAined", "type": "string", "variable_type": "Dimension"},
            "Year": {"description": "Year of the performance cycle", "type": "integer", "variable_type": "Dimension"},
            "Goals TRx": {"description": "Goal for the number of transactions (TRx) set for the specified month", "type": "integer", "variable_type": "Fact"}
        }
    },
    {
        "dataset_name": "Roster_Data",
        "variable_the_df_is_stored_in": "roster_df",
        "description": "Dataset containing employee roster details including roles, territories, reporting managers, and employment dates.",
        "columns": {
            "EMP_ROLE": {"description": "Role of the employee in the organization", "type": "string", "variable_type": "Dimension"},
            "Territory_ID": {"description": "Unique identifier for the sales territory assigned to the employee", "type": "string", "variable_type": "Dimension"},
            "MANAGER_NAME": {"description": "Name of the reporting manager for the employee", "type": "string", "variable_type": "Dimension"},
            "MANAGER_AREA_ID": {"description": "Unique identifier for the manager's area", "type": "string", "variable_type": "Dimension"},
            "REP START DATE": {"description": "Start date of the employee in the assigned role or territory", "type": "date", "variable_type": "Dimension"},
            "REP END DATE": {"description": "End date of the employee in the assigned role or territory (blank if active)", "type": "date", "variable_type": "Dimension"},
            "Employee ID": {"description": "Unique identifier assigned to the employee", "type": "string", "variable_type": "Dimension"},
            "EMP_NAME": {"description": "Full name of the employee", "type": "string", "variable_type": "Dimension"}
        }
    },
    {
        "dataset_name": "Zip_To_Terr",
        "variable_the_df_is_stored_in": "zip_to_territory_mapping_df",
        "description": "Dataset mapping ZIP codes to sales territories along with alignment start and end dates.",
        "columns": {
            "ZIP_CODE": {"description": "Postal ZIP code mapped to a specific sales territory", "type": "string", "variable_type": "Dimension"},
            "TERRITORY_ID": {"description": "Unique identifier for the sales territory", "type": "string", "variable_type": "Dimension"},
            "ALIGNMENT START DATE": {"description": "Date when the ZIP code was aligned to the territory", "type": "date", "variable_type": "Dimension"},
            "ALIGNMENT END DATE": {"description": "Date when the ZIP code alignment ended (blank if currently active)", "type": "date", "variable_type": "Dimension"}
        }
    },
    {
        "dataset_name": "Territory_Mapping",
        "variable_the_df_is_stored_in": "territory_mapping_df",
        "description": "Dataset mapping healthcare providers (HCPs) to territories, including ZIP codes, product groups, and alignment dates.",
        "columns": {
            "PROVIDER_ID": {"description": "Unique identifier for the healthcare provider (e.g., NPI)", "type": "string", "variable_type": "Dimension"},
            "ZIP_CODE": {"description": "Postal ZIP code of the healthcare provider", "type": "string", "variable_type": "Dimension"},
            "TERRITORY_ID": {"description": "Unique identifier for the sales territory", "type": "string", "variable_type": "Dimension"},
            "PRODUCT_GROUP": {"description": "Product group associated with the provider in the territory", "type": "string", "variable_type": "Dimension"},
            "ALIGNMENT START DATE": {"description": "Date when the provider was aligned to the territory", "type": "date", "variable_type": "Dimension"},
            "ALIGNMENT END DATE": {"description": "Date when the alignment ended (blank if currently active)", "type": "date", "variable_type": "Dimension"}
        }
    },
    {
        "dataset_name": "Xponent_Data",
        "variable_the_df_is_stored_in": "xponent_df",
        "description": "Dataset containing prescription transaction details for individual healthcare providers (HCPs). Includes patient-level TRx, drug details, quantities, and payer plan IDs. This dataset is used for analyzing prescriber behavior, patient claims, and prescription trends. Do NOT use this dataset for territory vs. national sales or market share comparisons. Use `weekly_sales_crediting_file` for that purpose",
        "columns": {
            "PROVIDER_ID": {"description": "Unique identifier for the healthcare provider (e.g., NPI)", "type": "string", "variable_type": "Dimension"},
            "DATE": {"description": "Date of the prescription transaction (format: MM/DD/YYY)", "type": "date", "variable_type": "Dimension"},
            "NDC_CODE": {"description": "National Drug Code identifying the specific drug", "type": "string", "variable_type": "Dimension"},
            "PRODUCT_GROUP": {"description": "Product group to which the prescribed drug belongs", "type": "string", "variable_type": "Dimension"},
            "MARKET": {"description": "Therapeutic market category for the drug (e.g., HIV)", "type": "string", "variable_type": "Dimension"},
            "NRX_TOTAL": {"description": "Number of new prescriptions for the drug", "type": "integer", "variable_type": "Fact"},
            "TRX_TOTAL": {"description": "Total number of prescriptions for the drug", "type": "integer", "variable_type": "Fact"},
            "Qty": {"description": "Quantity of the drug prescribed in the transaction", "type": "integer", "variable_type": "Fact"},
            "PAYER_PLAN ID": {"description": "Identifier for the payer plan associated with the prescription", "type": "string", "variable_type": "Dimension"}
        }
    },
    {
        "dataset_name": "LAAD_Data",
        "variable_the_df_is_stored_in": "laad_df",
        "description": "Dataset containing pharmaceutical claims data for patients, including details on medications (primarily HIV treatments), service dates, providers, quantities, payer plans, product groups, treatment switches, and persistency indicators.",
        "columns": {
            "CLAIM_ID": {"description": "Unique identifier for the claim", "type": "string", "variable_type": "Dimension"},
            "PATIENT_ID": {"description": "Unique identifier for the patient", "type": "string", "variable_type": "Dimension"},
            "NDC_CD": {"description": "National Drug Code for the medication", "type": "string", "variable_type": "Dimension"},
            "SVC_DT": {"description": "Service date of the claim (format: MM/DD/YYY)", "type": "date", "variable_type": "Dimension"},
            "CLAIM_TYPE": {"description": "Type of claim (e.g., PD for prescription drug)", "type": "string", "variable_type": "Dimension"},
            "DIAGNOSIS_CODE": {"description": "Diagnosis code associated with the claim", "type": "string", "variable_type": "Dimension"},
            "CLAIM_STATUS": {"description": "Status of the claim (e.g., S for submitted)", "type": "string", "variable_type": "Dimension"},
            "PROVIDER_ID": {"description": "Unique identifier for the healthcare provider", "type": "string", "variable_type": "Dimension"},
            "QUANTITY": {"description": "Quantity of medication dispensed", "type": "integer", "variable_type": "Fact"},
            "PAYER_PLAN_ID": {"description": "Identifier for the payer plan", "type": "string", "variable_type": "Dimension"},
            "PRODUCT_GROUP": {"description": "Name of the product group or medication (e.g., Biktarvy, Dovato)", "type": "string", "variable_type": "Dimension"},
            "SWITCH": {"description": "Indicator for medication switch (e.g., 0 for no switch, -1 for switch to other brands,1 - switch to current brand)", "type": "integer", "variable_type": "Dimension"},
            "PERSISTENCY": {"description": "Persistency indicator (0 or 1, where 1 may indicate persistent use)", "type": "integer", "variable_type": "Dimension"}
        }
    },
    {
        "dataset_name": "HCP_Master",
        "variable_the_df_is_stored_in": "hcp_master_df",
        "description": "Dataset containing master information of healthcare providers (HCPs), including provider details, specialties, and regional alignment.",
        "columns": {
            "PROVIDER_ID": {"description": "Unique identifier for the healthcare provider (e.g., NPI)", "type": "string", "variable_type": "Dimension"},
            "Master": {"description": "Name of the healthcare provider", "type": "string", "variable_type": "Dimension"},
            "SPECIALTY": {"description": "Specialty of the healthcare provider (e.g., Internal Medicine, HIV Specialist)", "type": "string", "variable_type": "Dimension"},
            "ZIP_CODE": {"description": "Postal ZIP code of the provider’s practice location", "type": "string", "variable_type": "Dimension"},
            "STATE": {"description": "US state where the provider is located", "type": "string", "variable_type": "Dimension"},
            "REGION": {"description": "Region where the provider practices (e.g., East, Central, West, South)", "type": "string", "variable_type": "Dimension"},
            "PHONE": {"description": "Contact phone number of the provider", "type": "string", "variable_type": "Dimension"},
            "EMAIL": {"description": "Email address of the provider", "type": "string", "variable_type": "Dimension"}
        }
    }
]
