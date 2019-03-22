# SettleMySettle
A web application for users to share and comment on starting locations within various strategy games, developed for WAD2.

### Team Members

Lewis Dyer (2299195D)
Luke Gall (2298070G)
Liam Lau (2314991L)
Aidan Randtoul (2323851R)

### Deployment instructions

In a newly created virtual environment, in Python 3.7, clone the repository by typing:
```
git clone https://github.com/settlemysettle/SettleMySettle
```
Access the project folder by typing:
```
cd settlemysettle
```

Install the required packages by running:
```
pip install -r requirements.txt
```

Set up the database by running:
```
python manage.py migrate
```
Populate the database with useful data by running:
```
python populate_settle.py
```

Run the server by running:
```
python manage.py runserver
```

And finally navigate to `http://127.0.0.1:8000/settle/`

---

The website is also deployed on PythonAnywhere at `http://settlemysettle.pythonanywhere.com` (although this may not be available if you're reading this several months in the future).

---

### External Sources

* The Bootstrap CSS toolkit was used, which is available at https://getbootstrap.com/.
* The jQuery JavaScript library was used, available at https://jquery.com/.
* Infinite scrolling was implemented using the Waypoints library along with the Infinite Scroll extension, available at https://github.com/imakewebthings/waypoints.
* The Steam Web API was used to obtain information from the Steam News Feed for particular games - more documentation on the API is available at https://steamcommunity.com/dev.
