import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

endpoint = "https://csc300-cv.services.ai.azure.com/api/projects/CVAssistant"

project_client = AIProjectClient(
    endpoint=endpoint,
    subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID"),
    resource_group_name=os.getenv("AZURE_RESOURCE_GROUP"),
    project_name=os.getenv("AZURE_PROJECT_NAME"),
    credential=DefaultAzureCredential()
)

openai_client = project_client.get_openai_client()

response = openai_client.responses.create(
    input=[{
        "role": "user",
        "content": "Tell me what you can help with."
    }],
    extra_body={
        "agent_reference": {
            "name": "AI-Career-Agent",
            "version": "5",
            "type": "agent_reference"
        }
    }
)

print(response.output_text)
