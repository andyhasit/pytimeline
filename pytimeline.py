from datetime import datetime, timedelta


class Timeline(object):
    """Runs the overall simulation timeline."""

    def __init__(self, start_time, end_time):
        self.events = []
        self.current_time = start_time
        self.end_time = end_time

    def schedule(self, datetime, function, parameters=None):
        """Schedules a event at a set datetime"""
        if datetime <= self.current_time:
            raise ValueError("Cannot schedule an event in the past")
        if datetime <= self.end_time:
            self.events.append(Event(datetime, function, parameters))
            self.events.sort(key=lambda event: event.datetime)
        
    def offset(self, timedelta, function, parameters=None):
        """Schedules a event at on offset of current time"""
        datetime = self.current_time + timedelta
        self.schedule(datetime, function, parameters)
        return datetime

    def start(self, step=None):
        """Starts the simulation, which will run until end_time or there are no more events left."""

        if step is None:
            while True:
                next_event = self._pop_next_event()
                if next_event:
                    self.current_time = next_event.datetime
                    next_event.call()
                else:
                    break
        else:
            # TODO: this is not right...
            while True:
                run_to = self.current_time + step
                while True:
                    next_event = self._pop_next_event(run_to)
                    if next_event:
                        next_event.call()
                    else:
                        break
        print "{time} Simulation Finished".format(time=self.current_time)

    
    def _pop_next_event(self, run_to=None):
        try:
            next_event = self.events[0]
        except IndexError:
            return None
        if run_to is None:
            self.events.remove(next_event)
            return next_event
        else:
            if next_event.datetime <= run_to:
                self.events.remove(next_event)
                return next_event


class Event(object):
    def __init__(self, datetime, function, parameters):
        self.datetime = datetime
        self.function = function
        self.parameters = parameters
    
    def call(self):
        if self.parameters is None:
            self.function()
        else:
            self.function(*self.parameters)


class SimulationObject(object):
    """Base class for simulation object."""
    
    def __init__(self, timeline):
        self.timeline = timeline

    def schedule(self, datetime, function, parameters=None):
        """Schedules a event at a set datetime"""
        return self.timeline.schedule(datetime, function, parameters)
        
    def offset(self, timedelta, function, parameters=None):
        """Schedules a event at on offset of current time"""
        return self.timeline.offset(timedelta, function, parameters)


'''


        print "Simulation started at %s stopping at %s"  % (start_time, end_time)
        print "with %s objects" % len(WorldObject.world_objects)
        
    @property
    def datetime(self):
        return self.current_time.strftime('%d/%m/%Y %H:%M')

        print "Simulation ended at %s"  % end_time

'''