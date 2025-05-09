# This file is for extracting the data from the API endpoints.
# API key for ACLED not included.
import pandas as pd
import requests
from hdx.api.configuration import Configuration
from hdx.data.dataset import Dataset

# Extracting ACLED Data:
APIKEY = "" # place apikey here
EMAIL = "" # place email here
URL = "https://api.acleddata.com/acled/read"
parameters1 = {
    "email": EMAIL,
    "key": APIKEY,
    "country": "Sudan",
    "year": 2025,
    "event_type": "Violence against civilians"
}

response1 = requests.get(url = URL, params = parameters1)
response1.raise_for_status()
response1_json = response1.json()
acled_df = pd.DataFrame(response1_json["data"]) # Where results are in nested json
acled_df.to_csv("cache/acled_data.csv", index = False)

# Extracting Humanitarian Exchange Data:
Configuration.create(hdx_site="prod", user_agent="sudan_war_dashboard1", hdx_read_only=True)
dataset_name = "sudan-displacement-data-idps-iom-dtm" # Displacement dataset name
dataset = Dataset.read_from_hdx(dataset_name)

## The "dataset" actually has multiple "resources" that link to excel sheet/csv,
## so the following identifies the correct data from the list of resources generated
## from the dataset:
resources = dataset.get_resources()
target_resource = next((r for r in resources if "round 7" in r["name"].lower()), None)
target_resource.download(folder = "cache")