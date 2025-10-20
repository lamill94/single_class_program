class Reminder():

    def __init__(self, name):
        self.name = name

    def remind_me_to(self, task):
        self._task = task

    def remind (self):
        return f"{self.name}, {self._task}"
    
reminder = Reminder("Lauren")
reminder.remind_me_to("Walk the dog")
print(reminder.remind())
    
