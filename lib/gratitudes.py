class Gratitudes():

# list has an underscore before it (_list) to make it PRIVATE

    def __init__(self):
        self._list = []

    def add(self, gratitude):
        self._list.append(gratitude)

    def format(self):
        gratitudes_string = ""
        for gratitude in self._list[0:-1]:
            gratitudes_string += gratitude + ", "
        gratitudes_string += "and " + self._list[-1]
        return f"I am grateful for: {gratitudes_string}."