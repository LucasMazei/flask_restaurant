rm -r migrations
rm storage.db
python3 run.py db init
python3 run.py db migrate
python3 run.py db upgrade
