class Gratitudes():

    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        gratitudes_string = ""
        for gratitude in self.gratitudes[0:-1]:
            gratitudes_string += gratitude + ", "
        gratitudes_string += "and " + self.gratitudes[-1]
        return f"I am grateful for: {gratitudes_string}."