## Setup and Installation

[Python](https://www.python.org/downloads/release/python-3124/) version used - 3.12.4

- Make sure git is [setup](https://www.theodinproject.com/lessons/foundations-setting-up-git) properly on your system.

   ```bash
   git clone https://github.com/shivamgupta021/whatbytes-assignment.git && cd whatbytes-assignment
   ```

- #### Create and activate a virtual environment
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   ```

- #### Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

- #### Apply changes to the database schema
   ```bash
   python manage.py migrate
   ```

- #### Create a superuser account
   ```bash
   python manage.py createsuperuser
   ```

- #### Run the server
   ```bash
   python manage.py runserver
   ```