import threading
import time

waiting_room = []
sleeping_barber = []


def Barber(name, event):
    print("%s starting job..." % (name,))
    while True:
        if len(waiting_room) > 0:
            waiting_room.pop(0)
            print("%s is cutting hair..." %(name,))
            time.sleep(2)
            print("All done now...")

        print("%s checks waiting room..."%(name,))
        if len(waiting_room) == 0:
            Reset(event)
            Block(name,event)
            print("%s awkens!..." % (name,))
        print("-----------------------------------------------")

def Customer(event):
    while True:
        print("Customer enters...")
        print(not flag_check(event))
        if not flag_check(event):
            print("Customer wakes barber...")
            WakeUp(event)
            waiting_room.append("Customer")

        elif len(waiting_room) <= 15:
            print("Customer takes a seat in the waiting room...")
            print("Seats taken is: " + str(len(waiting_room)))
            waiting_room.append("Customer")

        else:
            print("Customer leaves the barber shop...")

        time.sleep(20)

def WakeUp(event):
    event.set()

def Block(name, event):
    print("%s goes to sleep..." % (name,))
    event.wait()

def flag_check(event):
    return event.isSet()
    

def Reset(event):
    event.clear()



e1 = threading.Event()
#e2 = threading.Event()
threading.Thread(target=Barber, args=('Barber 1', e1)).start()
#threading.Thread(target=Barber, args=('Barber 2', e2)).start()

customers_list = []
time.sleep(1)
Customer(e1)



