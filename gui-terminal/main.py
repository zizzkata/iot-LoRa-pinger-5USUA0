import views.MainWindow as mw
import models.serial_model as sm

if __name__ == "__main__":
    main = mw.MainWindow()
    sm.start_serial_daemon()
    main.mainloop()