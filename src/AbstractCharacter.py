from abc import ABC, abstractmethod

class AbstractCharacter(ABC):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0

    @abstractmethod
    def draw(self,win):
        pass