import threading
import time

def worker():
    print(threading.current_thread().getName(),'Lanzado')
    time.sleep(2)
    print(threading.current_thread().getName(),'Detenido')
    
def servicio():
    print(threading.current_thread().getName(),'Lanzado')
    print(threading.current_thread().getName(),'Detenido')

t = threading.Thread(target = servicio, name = 'Servicio')
w = threading.Thread(target = worker, name = 'Worker')
z = threading.Thread(target = worker)

w.start()
z.start()
t.start()