class Camera(object):

    def __init__(self, pos=(0, 0)):
        self.__pos = (0, 0)

    def apply(self):
        return (-self.__pos[0], -self.__pos[1])

    def update(self):
        self.__pos = (self.__pos[0] + 2, self.__pos[1])
