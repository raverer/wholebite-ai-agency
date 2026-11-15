from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import json

from app.pipelines.content_pipeline import run_content_pipeline


def generate_and_store():

    input_data = {
        "brand": "WholeBite",
        "niche": "Fitness Nutrition",
        "audience": "Beginners in India",
        "platform": "Instagram",
        "goal": "Fat loss awareness"
    }

    result = run_content_pipeline(input_data)

    # Save with timestamp
    filename = f"outputs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"

    with open(filename, "w") as f:
        json.dump(result, f, indent=4)

    print(f"Saved: {filename}")


def start_scheduler():
    scheduler = BackgroundScheduler()

    # 🔥 Change interval here
    scheduler.add_job(generate_and_store, 'interval', hours=6)

    scheduler.start()