import threading
import time
import random

waiting_room = []
sleeping_barber = []


def Barber(name, event):
    print("%s starting job..." % (name,))
    while True:
        if len(waiting_room) > 0:
            cust = waiting_room.pop(0)
            print("%s is cutting hair of %s..." %(name, cust,))
            customerInterval = random.randrange(15,25)
            time.sleep(customerInterval)
            print("%s is all done now with %s..."%(name, cust,))

        print("%s checks waiting room..."%(name,))
        if len(waiting_room) == 0:
            sleeping_barber.append(event)
            Reset(event)
            Block(name,event)
            print("%s awakens!..." % (name,))

def Customer(event):
    customer_today = 1
    while True:
        print("Customer enters...")
        print("-----------------------------------------------")
        if len(sleeping_barber) > 0:
            print("Customer " + str(customer_today) + " wakes barber...")
            WakeUp(sleeping_barber[0])
            waiting_room.append("Customer " + str(customer_today))

        elif len(waiting_room) < number_of_chairs:
            print("Customer " + str(customer_today) + " takes a seat in the waiting room...")
            print("Seats taken is: " + str(len(waiting_room) + 1))
            waiting_room.append("Customer " + str(customer_today))

        else:
            print("Customer leaves the barber shop...")

        customerInterval = random.randrange(5,15)
        time.sleep(customerInterval)
        customer_today = customer_today + 1

def WakeUp(event):
    sleeping_barber[0].set()
    sleeping_barber.pop(0)

def Block(name, event):
    print("%s goes to sleep..." % (name,))
    event.wait()

def Reset(event):
    event.clear()

number_of_barbers = 4
number_of_chairs = 15
i = 1
while i != number_of_barbers + 1:
    barber_name = "Barber " + str(i)
    threading.Thread(target=Barber, args=(barber_name, threading.Event())).start()
    i = i + 1

time.sleep(1)
Customer(threading.Event())



