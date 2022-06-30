#!bin/sh
docker-compose up --build -d
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
brew install libpq-dev
pip install -r requirements.txt
pytest --driver Remote --capability browserName chrome book_webscraping_to_postgres.py