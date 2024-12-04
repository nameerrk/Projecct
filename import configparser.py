import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read('config.ini')  # Make sure the path is correct

# Access the values
user = config['MYSQL']['USER']
password = config['MYSQL']['PASSWORD']
host = config['MYSQL']['HOST']
db = config['MYSQL']['DB']

print(f"User: {user}")
print(f"Password: {password}")
print(f"Host: {host}")
print(f"Database: {db}")
