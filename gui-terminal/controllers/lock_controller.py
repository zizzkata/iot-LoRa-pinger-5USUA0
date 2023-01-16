from utils.async_wrapper import threaded_task
import utils.file_utils as fu
import utils.hashing_utils as hu


def unlock_screen(pass_code: str, callback):
    def threaded_func():
        try:
            user = fu.get_user()
            if user:
                callback(user["pass_code"] == hu.hash_string(pass_code))
            else:
                raise Exception("No user found")
        except Exception as e:
            print(e)
            callback(False)
        
    threaded_task(threaded_func, ())
