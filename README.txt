
# start virtualEnv
virtualEnv mandelEnv
source mandelEnv/bin/activate

# use heroko locally
foreman start #why is it not in the toolbelt 

# use django locally
python manage.py runserver

git push heroku master
https://tranquil-anchorage-8416.herokuapp.com/

# Heroku commands
heroku ps:scale web=1
heroku ps
heroku open
heroku logs
heroku run python manage.py syncdb