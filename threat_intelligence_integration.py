import requests

url = 'https://api.threatintelligenceplatform.com/v1/indicators?apikey=your_api_key'
response = requests.get(url)

if response.status_code == 200:
    threat_data = response.json()
    # Process threat intelligence data
else:
    print('Error fetching threat intelligence:', response.status_code)
