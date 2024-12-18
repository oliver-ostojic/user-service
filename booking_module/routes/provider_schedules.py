import os
from bson.objectid import InvalidId
from flask import Blueprint, jsonify
from mongodb_connection import provider_schedules_collection
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
uri = os.getenv("MONGODB_URI")
# Set blueprint
provider_schedules_bp = Blueprint('provider_schedules_bp', __name__)


@provider_schedules_bp.route('/<provider_id>', methods=['GET'])
def get_schedule(provider_id):
    try:
        schedule = provider_schedules_collection.find_one({'provider_id': int(provider_id)})
        if schedule:
            schedule['_id'] = str(schedule['_id'])
            # Update availability to only show available slots
            unbooked_slots = []
            for slot in schedule['availability']:
                if slot['is_booked'] is False:
                    unbooked_slots.append(slot)
            schedule['availability'] = unbooked_slots
            return jsonify(schedule), 200
        else:
            return jsonify({'message': 'Schedule not found for provider with id: {}'.format(provider_id)}), 404
    except (InvalidId, ValueError):
        return jsonify({'message': 'Invalid provider ID'}), 400
