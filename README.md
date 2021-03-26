# Sleeping Barber Assignment


**Part 1 - My Code:**

In my code I used event objects. This enabled the threads to communicate with each other. The Event Objects I used were:

1. **Event() :** this initiated the event and set the internal flag initially to false. I used this when I was creating my threads so each thread was an Event Object.

2. **wait() :** This blocks the thread until the internal flag is set true. If the internal flag is true on entry it will return immediately. Otherwise, it will block the thread until another thread calls set() to change the internal flag to true. This is what I used to put the barbers to sleep or in more technical terms blocked the threads.


3. **set() :** is used to change the internal flag to true if the internal flag is set to false on entry. However, if the internal flag is true on entry then it will return immediately. This is what I used to wake the barbers up every time a customer entered and the barber was asleep.

4. **clear() :** is used to reset the internal flags to false. This is what I used to ensure the wait function was executing properly. If the wait function received a true internal flag it would cause an infinite loop in my program. This is further explained in the "My Flaws Section" below.



**Part 2 - A Step By Step Explanation Of My Code:**

We begin where we have parameters that can be changed such as number of barbers and number of chairs. This allows us to change the numbers easily without having to look through the code and change each number manually. After this I have created a while loop that will loop according to the number in our number of barbers parameter. In this case it is four so four threads will be created and sent to the barber method each thread will be assigned a unique name and will be initiated as an Event Object. The thread will then begin by the start(). This will happen four times in this case.

The threads will now be sent to the Barber module. By the use of a boolean statement I can allow the barber to go to sleep and cut hair. When no one is in the barber shop the barber will go to sleep. During this process the barber name will be added to a list called sleepinf_barber, the thread(barber) will be reset using the clear() function to ensure the internal flags are set to false meaning the thread can be blocked(barber can go to sleep). The wait() function is in a separate module to ensure it does not cause any interference with the other code such as looping over the previous code as it is in an infinite looping barber module. 

At the end of the code a sleep timer is set to one to ensure that the barber threads are all set and ready to go before the infinite looping Customer module is started. Once started the customers will then start coming in at random times due to the random timer. If the barber is asleep the customer will wake up the first barber, by set(), in the sleeping barber list once the barber is awake the barber is pop() from the list and starts cutting the customer's hair. This sleeping barber list follows FIFO (First In First Out) this ensures that there is no starvation to the barber threads. Each
a customer is assigned a number starting from 1. This was a good way to ensure that each customer was getting their hair in the right order and once again ensuring there was no starvation of customers. The barber cuts the hair of the customer for a random time interval. Once the barber is finished the barber then checks the waiting room. Once again using boolean statements if the waiting room is empty the barber thread will be added to the sleeping barber list and be blocked by wait() or else if their is a customer in the waiting room the barber will pop() the top of the waitroom list following a FIFI order ensure no starvation occurs. Finally if the barbers are busy cutting hair and the waiting room is full any incoming customers will then leave the barber shop.
