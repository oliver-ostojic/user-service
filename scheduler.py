from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from mongodb_connection import users_collection, client


# Function to update all appointment statuses
def update_appointment_status():
    # Set the current time
    current_date = datetime.now()
    # Find all users
    users = users_collection.find()
    # Update all appointments
    for user in users:
        updated_appointments = []
        for appointment in user.get('appointments', []):
            start_time = datetime.fromisoformat(appointment.get('start_time'))
            if start_time < current_date:
                appointment['status'] = "passed"
            else:
                appointment['status'] = "upcoming"
            updated_appointments.append(appointment)
        users_collection.update_one(
            {'_id': user.get('_id')},
            {'$set': {'appointments': updated_appointments}}
            )
    client.close()


# Function to start the scheduler
def start_scheduler():
    scheduler = BackgroundScheduler()
    # Schedule the task to run daily at midnight
    scheduler.add_job(update_appointment_status, 'cron', hour=0)
    scheduler.start()
    print("Scheduler started")
