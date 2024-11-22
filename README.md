# User Service

The **User Service** is a microservice that handles user authentication, authorization, and appointment booking functionalities. It is a core component of the broader `find_doc` project, designed as a healthcare appointment system. 

---

## Features

- **Authentication and Authorization**:
  - JWT-based user authentication.
  - Middleware for token validation.
  - Secure user registration and login routes.

- **User Management**:
  - CRUD operations for user profiles.
  - Password hashing and secure storage.

- **Appointment Management**:
  - Schedule creation and management.
  - Booking appointments with providers.
  - Conflict resolution for overlapping appointments.

- **Utility and Configuration**:
  - MongoDB integration for database operations.
  - Configurable deployment with Docker and Heroku.

---

## Directory Structure

user_service/ ├── app.py # Main entry point for the service ├── auth_module/ # Authentication and authorization logic │ ├── middleware/ # Token validation middleware │ ├── auth_routes.py # Authentication routes │ └── user_model.py # User model for database integration ├── booking_module/ # Appointment and scheduling logic │ ├── models/ # Database models for users, appointments, schedules │ ├── routes/ # Routes for managing bookings and schedules ├── mongodb_connection.py # MongoDB connection utility ├── scripts/ # Utility scripts (e.g., mock data generation) ├── Dockerfile # Docker configuration ├── Pipfile # Python dependencies ├── Pipfile.lock # Locked dependencies for reproducibility ├── heroku.yml # Heroku deployment configuration └── README.md # Project documentation

---

## Installation

### Prerequisites

- Python 3.9+
- MongoDB
- Pipenv (for dependency management)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/oliver-ostojic/user_service.git
   cd user_service

2. Install dependences:
   pipenv install
3. Configure environment variables:
   Create a .env file in the root directory with the following variables:
   MONGO_URI=<your_mongo_connection_string>
   JWT_SECRET=<your_jwt_secret>
4. Start the service:
   pipenv run python app.py
   
