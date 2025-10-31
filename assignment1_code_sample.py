"""Example script from Assignment 1 to use bandit on."""

import os
from urllib.request import urlopen
import pymysql

db_config = {"host": "mydatabase.com", "user": "admin", "password": "secret123"}


def get_user_input():
    """Ask the user for their name and return it."""
    name_input = input("Enter your name: ")
    return name_input


def send_email(to, subject, body):
    """Send an email using a system command."""
    os.system(f'echo {body} | mail -s "{subject}" {to}')


def get_data():
    """Fetch data from API and return it as a string."""
    url = "http://insecure-api.com/get-data"
    data = urlopen(url).read().decode()
    return data


def save_to_db(data):
    """Save provided data to the database."""
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    # Main entry point of the script.
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email("admin@example.com", "User Input", user_input)
