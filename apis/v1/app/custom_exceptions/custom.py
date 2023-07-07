
# Create you own custom exception here

class EnvError(Exception):
    def __init__(self, value):
        self.value = value

