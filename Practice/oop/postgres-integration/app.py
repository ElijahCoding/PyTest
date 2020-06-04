from user import User
from database import Database

Database.initialise()

my_user = User('elijah@gmail.com', 'elddd', 'test', None)

my_user.save_to_db()