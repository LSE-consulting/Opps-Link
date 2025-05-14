import requests
import json

base_url = "https://www.contractsfinder.service.gov.uk/api/rest/2/search_notices/json"
keyword = "analysis"

params = {
    "searchCriteria": {
        "types": ["Contract", "Pipeline", "PreProcurement"],
        "statuses": ["Open"],
        "keyword": None,
        "queryString": None,
        "regions": None,
        "postcode": None,
        "radius": 0.0,
        "valueFrom": None,
        "valueTo": None,
        "publishedFrom": None,
        "publishedTo": None,
        "deadlineFrom": None,
        "deadlineTo": None,
        "approachMarketFrom": None,
        "approachMarketTo": None,
        "awardedFrom": None,
        "awardedTo": None,
        "isSubcontract": None,
        "suitableForSme": None,
        "suitableForVco": None,
        "awardedToSme": None,
        "awardedToVcse": None,
        "cpvCodes": [
            "79419000",
            "66171000",
            "79311400",
            "73210000",
            "75211200",
            "79315000",
            "73200000",
            "73110000",
            "79411000",
            "90713000",
            "73220000",
            "73100000",
            "73300000"
        ]
    },
    "size": 10000
}

# Make the POST request with json data
response = requests.post(base_url, json=params)


if response.status_code == 200:
    # Process and save the data
    data = response.json()
    
    if data:
        output_file = "output_data.json"  # Save as JSON file
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)  # Save with pretty formatting
        print(f"Data saved to {output_file}")
    else:
        print("No data found.")
else:
    print("Request failed with status code:", response.status_code)
    with open("error_log.txt", "w") as f:
        f.write(response.text)  # Save the raw error response
        print("Error details saved to error_log.txt")
