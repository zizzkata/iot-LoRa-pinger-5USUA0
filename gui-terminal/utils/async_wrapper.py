import threading

def threaded_task(target, args):
    thread = threading.Thread(target=target, args=args)
    thread.daemon = True
    thread.start()
