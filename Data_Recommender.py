from langchain_aws import ChatBedrockConverse
from langchain_core.messages import SystemMessage,HumanMessage
from pydantic import BaseModel,Field
from DB_Agent_System_Prompt import db_metadata
from typing import List
import streamlit as st
from cryptography.fernet import Fernet

class DataRecommendation(BaseModel):
    dataset_name: str = Field(..., description="Actual name of the suggested dataset")
    columns: List[str] = Field(..., description="List of column names from the dataset to use")

class RecommendationResponse(BaseModel):
    data_recommendation: List[DataRecommendation] = Field(
        ..., description="List of datasets and their relevant columns"
    )
    recommendation_reason: str = Field(
        ..., description="Reason for selecting the datasets and columns"
    )


key="5KmTdJ2hsmenGZVlb-gAAqg8GWstwbkKAo7uRNKAMRE="
access_key1=b'gAAAAABot9zz3KX7jY0lj_aWcW0nrVuyOMt9q2gMXh0VaaNBcBvMZ3ln490Z-LtJ3Rav69Jnps09KtYDVJ0Ca-XGaqBqMQxGlkzj5yPk4XNh-Yu2xbOSFRU='
access_key2=b'gAAAAABot9zzWbdFdJiATMHWGrqkJOSNYQ_sYAdaB7Kt9caQl6xHryiS5iEyO7VdYzVHLKYRvBEPHUKSkWNHNmAFouHIK9NM-_6d7bW3SSC6YeWCFlchtYx-lOfuCScihgasCaoQl03P'

cipher = Fernet(key)

llm = ChatBedrockConverse(
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",
    temperature=0,
    max_tokens=10000,
    disable_streaming=False,
    aws_access_key_id=cipher.decrypt(access_key1).decode(),
    aws_secret_access_key=cipher.decrypt(access_key2).decode(),
    region_name="us-east-1"  # or your preferred region
).with_structured_output(RecommendationResponse)

recommender_system_prompt="""<role>
You are a specialized data analysis planner dedicated to identifying the most relevant datasets and their corresponding columns required to answer user questions in a drag-and-drop dashboard application. 
You analyze user requirements and available dataset metadata to recommend which datasets and columns are essential, and provide a clear reason for your recommendation.
</role>

<available_information>
User Prompt: {user_prompt}
Dataset Details: {dataset_details}
</available_information>

<core_principles>
  <strategic_planning>
    - Always determine dataset and column relevance through logical analysis of data requirements.
    - Avoid assumptions beyond the provided metadata.
    - Ensure dataset and column selection directly supports answering the user's question.
    - Clearly explain why the recommended datasets and columns are appropriate.
  </strategic_planning>

  <methodology>
    Your recommendation process follows this structure:
    1. Question Decomposition - Break down the user's question into specific data requirements.
    2. Dataset Evaluation - Assess which datasets and columns provide the necessary information.
    3. Recommendation - Select the minimum required datasets and their relevant columns.
    4. Justification - Provide reasoning behind the dataset and column selection.
  </methodology>

  <response_structure>
    Return a valid JSON object in this exact format:
    {{
      "data_recommendation": [
        {{
          "dataset_name": "<Actual Name of the suggested dataset>",
          "columns": ["<col1>", "<col2>"]
        }},
        {{
          "dataset_name": "<Another dataset>",
          "columns": ["<col1>", "<col2>", "<col3>"]
        }}
      ],
      "recommendation_reason": "### Dataset Selection\n\n#### [Dataset Name 1]\n- **Purpose**: [Why this dataset is needed]\n\n#### [Dataset Name 2] (if applicable)\n- **Purpose**: [Why this dataset is needed]\n### Analysis Summary:\n[Summary of how the selected datasets and columns together address the user's question]"
    }}
  </response_structure>
</core_principles>

<plan_generation_rules>
  - Only include datasets that are necessary to answer the question.
  - Always specify columns at the level of granularity required by the question.
  - Recommendation reason must be formatted as proper markdown with clear structure and sections.
  - Do not provide implementation details, only dataset/column selection logic.
  - Keep JSON strictly valid and conforming to the specified schema.
  - Ensure the recommendation_reason field contains well-structured markdown formatting.
</plan_generation_rules>

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
  - Clearly connect dataset/column selection to user requirements.
  - Ensure recommendation is easy to interpret by downstream agents.
  - Use neutral, framework-agnostic reasoning.
  - Format the recommendation_reason as proper markdown with clear headings and structure.
</communication_principles>

<critical_reminders>
  - Output MUST be a valid JSON matching the specified structure.
  - Do not include additional keys, explanations, or natural language outside JSON.
  - Ensure reasoning is directly tied to answering the user's prompt.
  - Think strategically: recommend only what's required to create the dashboard view.
  - The recommendation_reason field must contain properly formatted markdown with clear sections and structure.
</critical_reminders>"""

st.title("📊 F.A.C.T Data Recommender")

# Input field
user_prompt = st.text_input("Enter your question:", "")

# Send button
if st.button("Send") and user_prompt.strip():
    
  recommender_system_prompt=recommender_system_prompt.format(user_prompt=user_prompt,dataset_details=db_metadata)

  recommender_response=llm.invoke([SystemMessage(content=recommender_system_prompt),HumanMessage(content=user_prompt)])

  datasets_to_use=[]
  for i in recommender_response.data_recommendation:
    datasets_to_use.append({"dataset_name":i.dataset_name,"columns":i.columns})
   
  # Display results
  st.subheader("✅ Recommended Datasets & Columns")
  st.json(datasets_to_use)

  st.subheader("📌 Recommendation Reason")

  st.info(recommender_response.recommendation_reason)




