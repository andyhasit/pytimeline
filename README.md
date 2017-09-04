# timeline

An extremely simple but effective (and efficient) timeline for simulations.

### Usage

Initiate a Timeline object with a start and end time (it won't started running until you tell it to)

```python
from datetime import datetime, timedelta
from tickless_simulator import Timeline

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

The timeline will work through the events in datetime order. New events can be added so long as they are scheduled between the current excecution time and the end time, in fact this is what you'll mostly be doing.

The timeline will instantly jump to the next event without delay or care for how much "simulation time" lies in between two events. In future I may add a time stepping method but for now this is how it works.

