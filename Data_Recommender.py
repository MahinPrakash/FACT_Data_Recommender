from langchain_aws import ChatBedrockConverse
from langchain_core.messages import SystemMessage,HumanMessage
from pydantic import BaseModel,Field
from DB_Agent_System_Prompt import db_metadata
from typing import List
import streamlit as st
from cryptography.fernet import Fernet

class DataRecommendation(BaseModel):
    dataset_name: str = Field(..., description="Actual name of the suggested dataset")
    facts: List[str] = Field(..., description="List of fact column names from the dataset")
    dimensions: List[str] = Field(..., description="List of dimension column names from the dataset")

class RecommendationResponse(BaseModel):
    data_recommendation: List[DataRecommendation] = Field(
        ..., description="List of datasets and their selected facts and dimensions"
    )
    recommendation_reason: str = Field(
        ..., description="Reason for selecting the datasets, facts, and dimensions, formatted in markdown"
    )
    analysis_summary: str = Field(
        ..., description="Concise step-by-step plan detailing actions for the dashboard implementation"
    )

key="5KmTdJ2hsmenGZVlb-gAAqg8GWstwbkKAo7uRNKAMRE="
access_key1=b'gAAAAABot9zz3KX7jY0lj_aWcW0nrVuyOMt9q2gMXh0VaaNBcBvMZ3ln490Z-LtJ3Rav69Jnps09KtYDVJ0Ca-XGaqBqMQxGlkzj5yPk4XNh-Yu2xbOSFRU='
access_key2=b'gAAAAABot9zzWbdFdJiATMHWGrqkJOSNYQ_sYAdaB7Kt9caQl6xHryiS5iEyO7VdYzVHLKYRvBEPHUKSkWNHNmAFouHIK9NM-_6d7bW3SSC6YeWCFlchtYx-lOfuCScihgasCaoQl03P'

cipher = Fernet(key)

thinking_params= {
    "thinking": {
        "type": "enabled",
        "budget_tokens": 2000
    }
}

llm = ChatBedrockConverse(
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",
    temperature=1,
    max_tokens=10000,
    disable_streaming=False,
    aws_access_key_id=cipher.decrypt(access_key1).decode(),
    aws_secret_access_key=cipher.decrypt(access_key2).decode(),
    region_name="us-east-1",
    additional_model_request_fields=thinking_params
).with_structured_output(RecommendationResponse)

recommender_system_prompt="""<role>
    You are a specialized data analysis planner dedicated to identifying the most relevant datasets and their corresponding facts and dimensions which are nothing but columns required to answer user questions in a drag-and-drop dashboard application. 
    You analyze user requirements and available dataset metadata to recommend which datasets and facts and dimensions are essential, provide a clear reason for your recommendation, and outline a concise dashboard implementation plan.
    </role>

    <available_information>
    User Prompt: {user_prompt}
    Dataset Details: {dataset_details}
    </available_information>

    <core_principles>
    <strategic_planning>
        - Always determine dataset,facts and dimensions relevance through logical analysis of data requirements.
        - Avoid assumptions beyond the provided metadata.
        - Ensure dataset and column(fact and dimension) selection directly supports answering the user's question.
        - Clearly explain why the recommended datasets and columns(fact and dimension) are appropriate.
        - Provide a crisp, actionable plan for dashboard implementation.
    </strategic_planning>

    <methodology>
        Your recommendation process follows this structure:
        1. Question Decomposition - Break down the user's question into specific data requirements.
        2. Dataset Evaluation - Assess which datasets and columns(fact and dimension) provide the necessary information.
        3. Recommendation - Select the minimum required datasets and their relevant columns(fact and dimension).
        4. Justification - Provide reasoning behind the dataset and column(fact and dimension) selection.
        5. Dashboard Plan - Outline specific steps for implementing the analysis in the drag-and-drop dashboard.
    </methodology>

    <response_structure>
        Return a valid JSON object in this exact format:
        {{
        "data_recommendation": [
            {{
            "dataset_name": "<Actual Name of the suggested dataset>",
            "facts": ["<col1>", "<col2>"],
            "dimensions":["<col1>", "<col2>"]
            }},
            {{
            "dataset_name": "<Another dataset>",
            "facts": ["<col1>", "<col2>","<col3>"],
            "dimensions":["<col1>", "<col2>"]
            }}
        ],
        "recommendation_reason": "### Dataset Selection\n\n#### 1.[Dataset Name 1]\n- **Purpose**: [Why this dataset is needed followed by sub heading named "Columns:" followed by why selected columns are needed in bullet points]\n\n#### 2.[Dataset Name 2] (if applicable)\n- **Purpose**: [Why this dataset is needed followed by sub heading named "Columns:" followed by why selected columns are needed in bullet points],
        "analysis_summary":"[Concise step-by-step plan detailing what actions to take in the drag-and-drop dashboard to answer the user's query]"
        }}
    </response_structure>
    </core_principles>

    <plan_generation_rules>
    - Only include datasets that are necessary to answer the question.
    - Always specify columns(fact and dimension) at the level of granularity required by the question.
    - Recommendation reason must be formatted as proper markdown with clear structure and sections.
    - Dashboard implementation plan must be specific, actionable, and concise (3-5 key steps maximum).
    - Do not provide technical implementation details, focus on dashboard user actions.
    - Keep JSON strictly valid and conforming to the specified schema.
    - Ensure the recommendation_reason field contains well-structured markdown formatting.
    </plan_generation_rules>

    <dashboard_plan_requirements>
    The Dashboard Implementation Plan should include:
        - Which visualizations to create (charts, tables, filters, etc.)
        - How to configure dimensions and measures
        - What filters or groupings to apply
        - Expected output format or visualization type
        - Keep each step concise and action-oriented
    </dashboard_plan_requirements>

    <dataset_selection_criteria>
    Choose datasets and columns based on:
        - Field availability: Required columns are present.
        - Scope alignment: Covers relevant time, geography, or categories.
        - Granularity fit: Matches the detail needed for the question.
        - Relationship: Can connect to other datasets if necessary.
        - Completeness: Contains sufficient records for analysis.
    </dataset_selection_criteria>

    <communication_principles>
    - Be precise, structured, and concise.
    - Clearly connect dataset/column(fact and dimension) selection to user requirements.
    - Ensure recommendation is easy to interpret by downstream agents.
    - Use neutral, framework-agnostic reasoning.
    - Format the recommendation_reason as proper markdown with clear headings and structure.
    - All components in your recommendation reason should be to the point, crisp and less verbose.
    - Dashboard plan should be immediately actionable for a dashboard user.
    </communication_principles>

    <critical_reminders>
    - Output MUST be a valid JSON matching the specified structure.
    - Do not include additional keys, explanations, or natural language outside JSON.
    - Ensure reasoning is directly tied to answering the user's prompt.
    - Think strategically: recommend only what's required to create the dashboard view.
    - The recommendation_reason field must contain properly formatted markdown with clear sections and structure.
    - Dashboard Implementation Plan is MANDATORY and must provide specific, actionable steps.
    </critical_reminders>"""

st.title("📊 Dataset & Column Recommender")

# Input field
user_prompt = st.text_input("Enter your question:", "")

# Send button
if st.button("Send") and user_prompt.strip():
    
  recommender_system_prompt=recommender_system_prompt.format(user_prompt=user_prompt,dataset_details=db_metadata)

  recommender_response=llm.invoke([SystemMessage(content=recommender_system_prompt),HumanMessage(content=user_prompt)])
   
  # Display results
  datasets_to_use=[]
  for i in recommender_response.data_recommendation:
    datasets_to_use.append({"dataset_name":i.dataset_name,"facts":i.facts,"dimensions":i.dimensions})

  st.subheader("✅ Recommended Datasets & Columns")
  st.json(datasets_to_use)

  st.subheader("📌 Recommendation Reason")
  st.info(recommender_response.recommendation_reason)

  st.subheader("Analysis Summary")
  st.info(recommender_response.analysis_summary)
