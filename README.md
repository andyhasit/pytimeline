# pytimeline

An extremely simple but effective (and efficient) timeline for simulations.

### Usage

Initiate a Timeline object with a start and end time (it won't started running until you tell it to)

```python
from datetime import datetime, timedelta
from pytimeline import Timeline

start = datetime.now()
end = start_time + timedelta(days=365*2)
timeline = Timeline(start, end)
```

Schedule events by passing a callable, and the datetime when you want it to trigger.

```python
in_3_days = datetime.now() + timedelta(days=3)

def foo():
    print("hello")
    
timeline.schedule(in_3_days, foo)
```

Note that in a real application this function will likely be bound to an object in your simulation, and result in additional tasks being scheduled.

You can then start your timeline:

```python
timeline.start()
```

### How it works

The timeline will run through the events in datetime order, calling each one of them before determining the next event. New events can be added so long as they are scheduled between the current excecution time and the end time, in fact this is what you'll mostly be doing.

The timeline will instantly jump to the next event without delay or care for how much "simulation time" lies in between two events. In future I may add a time stepping method but for now this is how it works.

### What can you do with it?

This was originally designed to determine the optimal supply chain for vaccine centers third world countries, where:

- An unknown number of people might showing to get vaccinated on any given day

- Health centers could set different opening times

- Batches of vaccines expire a certain time after being opened

- Batches come in different sizes

In other words it can be used to simulate large ecosystems of real world objects interacting with one another, tracking their states, and reporting conditions.

See __/examles__ 

### Recommendations

Use clean OOP design to model your objects, and put separate concerns into separate classes. For example, a bank account should only really track its balance. Applying overdraft fees or interest should be done by separate objects.