The Flaws In My Code

- When I was first building my code their was an infinite loop and it speed through my code very quickly eventually causing my laptop to crash. My solved this by using the sleep() function from the time library. This allowed me to analysis the output and sequence of steps in a slower manner without spamming the interperator.

- Initially when implementing the event() object. I was trying to put my single barber to sleep using the wait(). I placed that in my Barber module. It succeeded in blocking (putting the barber to sleep) however it kept looping over the satements previously causing errors in the expected sequence of steps for a barber. My solution was to create a separate module with only the wait() function as it will not interfere with other code.

- When implementing my Reset(event) function (clear()), I positioned it after the block (wait()) function. Initially, I was not aware that the internal flag had to be set to false inorder to block (wait()) so my Block finction was always immediately passing as true which messed uo the boolean statement when I was originally using isSet() to check if a single barber was sleeping.