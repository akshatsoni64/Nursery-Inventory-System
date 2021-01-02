# Nursery-Inventory-System
Installation Notes:
- Configure virtual environment(optional)<br>
<code>virtualenv venv -p python3</code>
- Activate virtualenv<br>
<code>source venv/bin/activate</code>
- Install dependencies from requirements.txt<br>
<code>pip3 install -r requirements.txt</code>
- Make empty database named 'nursery'
- Configure database connection in settings.py
- Migrate the database
<code>python3 manage.py migrate</code>
- Fire up the server
<code>python3 manage.py runserver</code>
- Register the users
- Use the app
