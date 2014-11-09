class AutomaticCamera(object):
    """
        a camera that moves automaticaly with a given
        velocity, that its a speed and a direction.
    """

    def __init__(self, pos=(0, 0), speed=(1, 0)):
        self.__pos = pos
        self.__speed = speed

    def apply(self):
        return (-self.__pos[0], -self.__pos[1])

    def update(self):
        self.__pos = (
            self.__pos[0] + self.__speed[0],
            self.__pos[1] + self.__speed[1]
        )
