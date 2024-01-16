#pip3.10 install -r requirements.txt
#python3.10 manage.py collectstatic

echo "Creating a virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing the latest version of pip..."
python3 -m pip install --upgrade pip

# Build the project
echo "Building the project..."
python3 -m pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

pip3 install whitenoise