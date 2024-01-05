# crud-task-api
Django REST API to manage a Task entity with CRUD (Create, Read, Update, Delete) functionalities.



API Endpoints
List and Create Tasks
URL: /api/tasks/
Method: GET (List all tasks), POST (Create a new task)
Retrieve, Update, and Delete a Specific Task
URL: /api/tasks/<int:pk>/
Method: GET (Retrieve), PUT (Update), DELETE (Delete)


Project Structure
task_manager/: Django project directory
tasks/: Django app directory
models.py: Task model definition
serializers.py: Task model serializer
views.py: Views for handling API endpoints
urls.py: URL patterns for the app
tests.py: Unit tests for the API

Database: SQLite (configured in settings.py)


## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/amreshparida/crud-task-api.git
   cd crud-task-api
   cd task_crud
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver


  


