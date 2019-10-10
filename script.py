from receiver import main as rxscript
from sender import main as txscript
import threading
import time

t1 = threading.Thread(target=rxscript)
t1.start()
time.sleep(1)
t2 = threading.Thread(target=txscript)
t2.start()
