import threading

def worker(consec):
    print("Hilo ejecutandose" + str(consec))
    return

threads = []

for i in range(0,5):
    t = threading.Thread(target=worker, args=(i,)) #(i,) si no se van a poner más parametros
    threads.append(t)
    t.start() #como se inicia un hilo
