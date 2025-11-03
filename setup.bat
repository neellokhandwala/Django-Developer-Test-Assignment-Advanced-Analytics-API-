@echo off
echo Setting up Sales Analytics API...

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Running migrations...
python manage.py makemigrations
python manage.py migrate

echo Creating superuser...
echo Please create a superuser account:
python manage.py createsuperuser

echo Setup completed!
echo.
echo To start the server:
echo 1. Activate virtual environment: venv\Scripts\activate
echo 2. Run server: python manage.py runserver
echo.
echo Optional: Load sample data with: python sample_data.py