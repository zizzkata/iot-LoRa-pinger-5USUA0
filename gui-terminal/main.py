import sys
import views.MainWindow as mw
import models.serial_model as sm

def kill_program(main):
    sm.kill_deamon()
    main.destroy()


if __name__ == "__main__":
    main = mw.MainWindow()
    sm.start_serial_daemon()
    main.protocol("WM_DELETE_WINDOW", lambda x=main: kill_program(x))
    if (len(sys.argv) <= 1 or sys.argv[1] != "--headless"):
        main.mainloop()
    else:
        while(True):
            pass