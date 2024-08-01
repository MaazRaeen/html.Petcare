
from app import app

with app.app_context():
    print("Application context created")
    # Your code that uses the application object goes here