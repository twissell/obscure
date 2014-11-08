class Camera(object):

    def __init__(self):
        self.pos = (0, 0)

    def apply(self):
        return (-self.pos[0], -self.pos[1])

    def update(self):
        self.pos = (self.pos[0] + 2, self.pos[1])
