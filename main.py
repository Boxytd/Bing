import requests
import time
from datetime import datetime

# --- Configuration ---
DEPLOY_URL = "https://api.vercel.com/v1/integrations/deploy/prj_gq4aeOjXyOvCUw51WEZ2xBQHR2jy/2QMpr1sxW5"
INTERVAL_SECONDS = 3600  # 1 hour
# ---------------------

def trigger_deploy():
    """Sends the deploy request and logs the outcome to the console."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Triggering deploy...")

    try:
        response = requests.post(DEPLOY_URL, timeout=20)
        if response.ok:
            print(f"[{timestamp}] ✅ Success! Status Code: {response.status_code}")
        else:
            print(f"[{timestamp}] ❌ Error! Status Code: {response.status_code}")
    except Exception as e:
        print(f"[{timestamp}] ❌ A critical network error occurred: {e}")
    finally:
        print("-" * 20)

if __name__ == "__main__":
    print("🚀 Background worker started. Triggering initial deploy...")
    trigger_deploy()

    while True:
        print(f"Sleeping for 1 hour until the next trigger...")
        time.sleep(INTERVAL_SECONDS)
        trigger_deploy()
