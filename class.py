
class time:
    def __init__(self,count):
        if count < 2:
            self.hours = int(input("Enter the hours:"))
            self.minutes = int(input("Enter the minutes:"))
        else:
            while count > 2:
                break
    def add_time(a, b):
        t3 = time(3)
        t3.hours = a.hours + b.hours
        t3.minutes = a.minutes + b.minutes
        while t3.minutes >= 60:
            t3.hours += 1
            t3.minutes -= 60
        return t3
    def display_time(self):
        print("The time is", self.hours ,"hrs", self.minutes, "min")
    def displayMinutes(self):
        minutes = self.hours * 60 + self.minutes
        print(minutes,"min")
t1 = time(0)
t2 = time(1)
a = time.add_time(t1, t2)
a.display_time()
a.displayMinutes()                                 