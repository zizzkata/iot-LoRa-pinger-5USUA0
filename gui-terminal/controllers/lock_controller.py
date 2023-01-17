from utils.async_wrapper import threaded_task
import utils.file_utils as fu
import utils.hashing_utils as hu

user = None

def unlock_screen(pass_code: str, callback):
    global user
    if user:
        callback(user["pass_code"] == hu.hash_string(pass_code))
    else:
        print("No user found")
        callback(False)

     
def import_user():
    global user
    try:
        user = fu.get_user()
        print("User found")
    except Exception as e:
        print("Failed to get the user")
        print(e)

threaded_task(import_user, ())
