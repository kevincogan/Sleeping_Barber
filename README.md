# CA216 Sleeping Barber Assignment

In this document I have four parts.

Part 1, My Code:

In my code I used event objects. This enabled the threads to communicate with each other. The Event Objects I used were:

1. Event() : this initiated the event and set the internal flag initially to false. I used this when I was creating my threads so each thread was an Event Object.

2. wait() : This blocks the thread until the internal flag is set true. If the internal flag is true on entry it will return immediately. Otherwise, it will block the thread until another thread calls set() to change the internal flag to true. This is what I used to put the barbers to sleep or in more technical terms blocked the threads.


3. set() : is used to change the internal flag to true if the internal flag is set to false on entry. However, if the internal flag is true on entry then it will return immediately. This is what I used to wake the barbers up every time a customer entered and the barber was asleep.

4. clear() : is used to reset the internal flags to false. This is what I used to ensure the wait function was executing properly. If the wait function received a true internal flag it would cause an infinite loop in my program. This is further explained in the "My Flaws Section" below.



Part 2, A Step By Step Explanation Of My Code:

We begin where we have parameters that can be changed such as number of barbers and number of chairs. This allows us to change the numbers easily without having to look through the code and change each number manually. After this I have created a while loop that will loop according to the number in our number of barbers parameter. In this case it is four so four threads will be created and sent to the barber method each thread will be assigned a unique name and will be initiated as an Event Object. The thread will then begin by the start(). This will happen four times in this case.

The threads will now be sent to the Barber module. By the use of a boolean statement I can allow the barber to go to sleep and cut hair. When no one is in the barber shop the barber will go to sleep. During this process the barber name will be added to a list called sleepinf_barber, the thread(barber) will be reset using the clear() function to ensure the internal flags are set to false meaning the thread can be blocked(barber can go to sleep). The wait() function is in a separate module to ensure it does not cause any interference with the other code such as looping over the previous code as it is in an infinite looping barber module. 

At the end of the code a sleep timer is set to one to ensure that the barber threads are all set and ready to go before the infinite looping Customer module is started. Once started the customers will then start coming in at random times due to the random timer. If the barber is asleep the customer will wake up the first barber, by set(), in the sleeping barber list once the barber is awake the barber is pop() from the list and starts cutting the customer's hair. This sleeping barber list follows FIFO (First In First Out) this ensures that there is no starvation to the barber threads. Each
a customer is assigned a number starting from 1. This was a good way to ensure that each customer was getting their hair in the right order and once again ensuring there was no starvation of customers. The barber cuts the hair of the customer for a random time interval. Once the barber is finished the barber then checks the waiting room. Once again using boolean statements if the waiting room is empty the barber thread will be added to the sleeping barber list and be blocked by wait() or else if their is a customer in the waiting room the barber will pop() the top of the waitroom list following a FIFI order ensure no starvation occurs. Finally if the barbers are busy cutting hair and the waiting room is full any incoming customers will then leave the barber shop.



Part 3, How I Tested My Code

In order to test my code I used a number of print statements with the action that the tread was doing. This enabled me to visualise what my program was doing so I could understand how my program was running at each step of my code.

Part 4, The Flaws In My Code

1. When I was first building my code there was an infinite loop and it sped through my code very quickly eventually causing my laptop to crash. I solved this by using the sleep() function from the time library. This allowed me to analyze the output and sequence of steps in a slower manner without spamming the interpreter.

2. Initially when implementing the event() object. I was trying to put my single barber to sleep using the wait(). I placed that in my Barber module. It succeeded in blocking (putting the barber to sleep) however it kept looping over the statements previously causing errors in the expected sequence of steps for a barber. My solution was to create a separate module with only the wait() function as it will not interfere with other code.

3. When implementing my Reset(event) function (clear()), I positioned it after the block (wait()) function. Initially, I was not aware that the internal flag had to be set to false inorder to block (wait()) so my Block function was always immediately passing as true which messed up the boolean statement when I was originally using isSet() to check if a single barber was sleeping.
