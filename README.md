# Barber Shop Simulation

This Python script simulates a barber shop with multiple barbers and customers entering randomly. The program models the classic "Sleeping Barber Problem" using threads.

## Features
- Simulates barbers cutting hair, going to sleep when idle, and being awakened by customers.
- Simulates customers entering the barber shop at random intervals.
- Manages waiting room seats for customers.
- Dynamically handles multiple barbers and customers.

## Prerequisites
- Python 3.x

## How It Works
### Main Components:
1. **Barber Function**
   - Represents a barber who cuts hair, checks the waiting room, and sleeps when no customers are present.

2. **Customer Function**
   - Simulates customers entering the shop at random intervals and determines their behavior:
     - Wakes up a sleeping barber.
     - Takes a seat in the waiting room if available.
     - Leaves if no seats are available.

3. **Event Handling**
   - `WakeUp(event)`: Wakes a sleeping barber by setting the thread event.
   - `Block(name, event)`: Blocks the barber thread (puts the barber to sleep).
   - `Reset(event)`: Resets the state of the barber’s thread.

### Variables:
- `waiting_room`: List tracking customers in the waiting room.
- `sleeping_barber`: List of barbers that are currently asleep.
- `number_of_barbers`: Number of barbers in the shop (default: 4).
- `number_of_chairs`: Number of chairs in the waiting room (default: 15).

### Workflow:
1. Barbers and customers are implemented as separate threads.
2. Customers arrive at random intervals (5-15 seconds) and:
   - Wake a sleeping barber if available.
   - Take a seat if there are available chairs in the waiting room.
   - Leave the shop if no chairs are available.
3. Barbers:
   - Cut hair for customers in the waiting room (takes 15-25 seconds).
   - Sleep when the waiting room is empty.
   - Wake up when a customer arrives and wakes them.

## How to Run
1. Save the script as `barber_shop_simulation.py`.
2. Run the script in the terminal:
   ```bash
   python barber_shop_simulation.py
   ```
3. The output will display the simulation of customers entering, barbers cutting hair, and barbers sleeping/waking up.

## Customization
- **Change the number of barbers:**
  Update `number_of_barbers` to the desired number of barbers.

- **Change the number of chairs in the waiting room:**
  Update `number_of_chairs` to reflect the size of the waiting area.

## Example Output
```
Barber 1 starting job...
Barber 2 starting job...
Barber 3 starting job...
Barber 4 starting job...
Customer enters...
Customer 1 takes a seat in the waiting room...
Seats taken is: 1
Barber 1 is cutting hair of Customer 1...
Customer enters...
Customer 2 wakes barber...
Barber 2 awakens!...
Customer enters...
Customer 3 takes a seat in the waiting room...
Seats taken is: 1
Barber 2 is cutting hair of Customer 2...
Barber 1 is all done now with Customer 1...
...
```

## Notes
- The simulation runs indefinitely, generating customers and processing barbers’ actions.
- To stop the simulation, use `Ctrl+C` in the terminal.

Enjoy experimenting with this fun simulation!

