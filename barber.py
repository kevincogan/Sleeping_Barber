import threading
import time
import random

waiting_room = []
sleeping_barber = []


def Barber(name, event):
    print("%s starting job..." % (name,))
    while True:
        if len(waiting_room) > 0:
            waiting_room.pop(0)
            print("%s is cutting hair..." %(name,))
            customerInterval = random.randrange(15,25)
            time.sleep(customerInterval)
            print("%s: All done now..."%(name,))

        print("%s checks waiting room..."%(name,))
        if len(waiting_room) == 0:
            sleeping_barber.append(event)
            Reset(event)
            Block(name,event)
            print("%s awakens!..." % (name,))

def Customer(event):
    while True:
        print("Customer enters...")
        print("-----------------------------------------------")
        if len(sleeping_barber) > 0:
            print("Customer wakes barber...")
            WakeUp(sleeping_barber[0])
            waiting_room.append("Customer")

        elif len(waiting_room) < 15:
            print("Customer takes a seat in the waiting room...")
            print("Seats taken is: " + str(len(waiting_room) + 1))
            waiting_room.append("Customer")

        else:
            print("Customer leaves the barber shop...")

        customerInterval = random.randrange(5,15)
        time.sleep(customerInterval)

def WakeUp(event):
    sleeping_barber[0].set()
    sleeping_barber.pop(0)

def Block(name, event):
    print("%s goes to sleep..." % (name,))
    event.wait()
    

def Reset(event):
    event.clear()



e1 = threading.Event()
e2 = threading.Event()
e3 = threading.Event()
threading.Thread(target=Barber, args=('Barber 1', e1)).start()
threading.Thread(target=Barber, args=('Barber 2', e2)).start()
threading.Thread(target=Barber, args=('Barber 3', e3)).start()


time.sleep(1)
Customer(e1)



