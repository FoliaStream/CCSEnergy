import requests
import time

API_URL = "https://ccsenergy-api.onrender.com"

def get_with_retry(url, params=None, timeout=90, retries=2):
    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(3)
    raise Exception("API did not respond after retries")

plants = get_with_retry(f"{API_URL}/items")
print(f"Total plants: {len(plants)}")