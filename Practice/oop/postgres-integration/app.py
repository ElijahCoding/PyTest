from user import User

my_user = User.load_from_db_by_email('elijah@gmail.com')
print(my_user)