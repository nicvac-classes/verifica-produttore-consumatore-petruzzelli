import threading
import random

DIM_BUFFER = 7
N_PRODUTTORI = 4
N_CONSUMATORI = 3
N_RICHIESTE = 4

buffer = [None] * DIM_BUFFER
metti = 0
togli = 0

vuoto = threading.Semaphore(DIM_BUFFER)
pieno = threading.Semaphore(0)
mutexP = threading.Semaphore(1)
mutexC = threading.Semaphore(1)


def genera_drone():
    return f"DRN-{random.randint(100, 999)}"


class ProduttoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

    # DA IMPLEMENTARE (run)
    delf run (self)
    global metti
    for in range (N_RICHIESTE):
        richiesta=genera_drone
        vuoto.acquire()
        metti.acquire()
        buffer[metti]=richiesta
        metti=(metti+1) % DIM_BUFFER
        print(f"[SENSOR-{self.idx}] segnala {richiesta}")
        mutexP.release()
        pieno.release()

class ConsumatoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

    # DA IMPLEMENTARE (run)
    def run (self):
    global togli
    while True:
        pieno.acquire()
        mutexC.acquire()
        richiesta=buffer[togli]
        buffer[togli]=None
        togli=(togli+1) % DIM_BUFFER
        mutexC.release()
        vuoto.release()
        if richiesta is None
        break
        
        print(f"[RUNWAY-{self.idx}] autorizza {richiesta}")



def main():
    global metti

    produttori = [ProduttoreThread(i + 1) for i in range(N_PRODUTTORI)]
    consumatori = [ConsumatoreThread(i + 1) for i in range(N_CONSUMATORI)]

    # DA IMPLEMENTARE: start dei thread produttori e consumatori
    for p in produttori:
        p.start()
    for c in consumatori:
        c.start()

    # DA IMPLEMENTARE: join di tutti i produttori
    for p in produttori:
        p.join()

    print("Tutti i sensori hanno terminato. Chiusura piste...")

    # Invia una sentinella None per ogni pista attiva.
    for _ in range(N_CONSUMATORI):
        # DA IMPLEMENTARE: inserire None nel buffer
        vuoto.acquire()
        mutexP.acquire()
        buffer[metti]=None
        metti= (metti+1) % DIM_BUFFER
        mutexP.release()
        pieno.release()
        pass

    # DA IMPLEMENTARE: join di tutti i consumatori
    for c in consumatori:
        c.join()

    print("Torre operativa chiusa.")


if __name__ == "__main__":
    main()