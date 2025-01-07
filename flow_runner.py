import requests
from typing import Optional

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "222d5a9b-adc6-4a87-9117-1dc37c25fc7c"


def run_flow(
    message: str,
    endpoint: str,
    output_type: str = "chat",
    input_type: str = "chat",
    tweaks: Optional[dict] = None,
    application_token: Optional[str] = None,
) -> dict:
    """
    Run a flow with a given message and optional tweaks.
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"
    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = {"Content-Type": "application/json"}
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers["Authorization"] = "Bearer " + application_token
    response = requests.post(api_url, json=payload, headers=headers)
    response.raise_for_status()  
    return response.json()
