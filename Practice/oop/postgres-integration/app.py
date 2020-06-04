from user import User
from database import Database

Database.initialise(
    database='postgres',
    user='postgres',
    password='root', port=54320,
    host='localhost'
)

my_user = User('elijah@gmail.com', 'elddd', 'test', None)

my_user.save_to_db()