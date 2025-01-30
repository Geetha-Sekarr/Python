#create a config file
# store configuration variables config.py
DATABASE_HOST = 'localhost'
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'password123'
DATABASE_NAME = 'my_database'

LOG_LEVEL = 'DEBUG'
LOG_FILE = 'app.log'

#store the file in setting in config.ini
#Create a Python script to read the configuration
import configparser

# Initialize the configparser object
config = configparser.ConfigParser()

# Read the config file
config.read('config.ini')

# Access the settings
database_host = config['database']['host']
database_user = config['database']['user']
database_password = config['database']['password']
database_name = config['database']['name']

log_level = config['logging']['level']
log_file = config['logging']['logfile']

# Using the configuration settings
print(f"Connecting to database {database_name} at {database_host} with user {database_user}")
print(f"Logging at {log_level} level to file {log_file}")


#JSON file
{
  "database": {
    "host": "localhost",
    "user": "root",
    "password": "password123",
    "name": "my_database"
  },
  "logging": {
    "level": "DEBUG",
    "logfile": "app.log"
  }
}

