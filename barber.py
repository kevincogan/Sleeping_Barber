import threading
import time
import random

#This keeps track of the number of customers in the waiting room.
waiting_room = []

#This keeps track of the barbers that are availabe in order.
sleeping_barber = []

#This contains all the activiy of the barber.
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

#This randomly generates customers and the activity of the customer.
def Customer(event):
    customer_today = 1
    while True:
        print("Customer enters...")
        print("-----------------------------------------------")
        
        #If a barber is asleep the customer wakes the barber up.
        if len(sleeping_barber) > 0:
            print("Customer " + str(customer_today) + " wakes barber...")
            WakeUp(sleeping_barber[0])
            waiting_room.append("Customer " + str(customer_today))
        
        #If their is a chair availabe in the waiting room take a seat.
        elif len(waiting_room) < number_of_chairs:
            print("Customer " + str(customer_today) + " takes a seat in the waiting room...")
            print("Seats taken is: " + str(len(waiting_room) + 1))
            waiting_room.append("Customer " + str(customer_today))
        
        #If no seats are available leave the barber shop.
        else:
            print("Customer leaves the barber shop...")
        
        #Customers randomly enters the shop between 5 and 15 seconds.
        customerInterval = random.randrange(5,15)
        time.sleep(customerInterval)
        customer_today = customer_today + 1

#This wakes up the barber by activating the thread.
def WakeUp(event):
    sleeping_barber[0].set()
    sleeping_barber.pop(0)

#This block the thread barber to go to sleep.
def Block(name, event):
    print("%s goes to sleep..." % (name,))
    event.wait()

#This resets the state of the thread.
def Reset(event):
    event.clear()

#This enables the user to change the number of barbers working and how many chairs are in the waiting room.
number_of_barbers = 4
number_of_chairs = 15

#This creates a thread for each barber and assigns them a unique number.
i = 1
while i != number_of_barbers + 1:
    barber_name = "Barber " + str(i)
    threading.Thread(target=Barber, args=(barber_name, threading.Event())).start()
    i = i + 1

#This initiates the customer thread so users can randomly enter the shop.
time.sleep(1)
Customer(threading.Event())



