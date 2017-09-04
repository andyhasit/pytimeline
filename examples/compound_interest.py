'''
This example shows how py_simulator can be used to calculate compound interest.

'''
from datetime import datetime, timedelta
from decimal import Decimal
from timeline import Timeline, SimulationObject

class CompoundInterestAccount(SimulationObject):
    
    def __init__(self, timeline, name, start_balance, interest_rate, frequency):
        SimulationObject.__init__(self, timeline)
        self.name = name
        self.balance =  Decimal(start_balance)
        self.interest_rate = Decimal(interest_rate)
        self.frequency = frequency
        self.offset(self.frequency, self.schedule_next_interest_payment)
        
    def apply_interest(self):
        self.balance = self.balance + ((self.balance / 100) * self.interest_rate)
        print "{time} {name}'s account has {balance}".format(
            name=self.name, balance=self.balance, time=self.timeline.current_time
        )

    def schedule_next_interest_payment(self):
        self.offset(self.frequency, self.schedule_next_interest_payment)
        self.apply_interest()

        
# Initialise timeline
start_time = datetime.now()
end_time = start_time + timedelta(days=365*2)
timeline = Timeline(start_time, end_time)

# Create two accounts
acc1 = CompoundInterestAccount(timeline, "Joe", 100, 5, timedelta(days=365))
acc2 = CompoundInterestAccount(timeline, "Jane", 100, 10, timedelta(days=365))

# Start simulation
timeline.start()

print acc1.balance # Should be 110.25
print acc2.balance # Should be 121.00
