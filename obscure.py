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
        """
            returns the new position of the camera,
            and never moves beyond the boundaries.
        """

        next_x = self.__pos[0] + self.__speed[0]
        next_y = self.__pos[1] + self.__speed[1]

        boundary_left = 0
        boundary_right = LEVEL_WIDTH - SCREEN_WIDTH
        boundary_top = 0
        boundary_bottom = LEVEL_HEIGHT - SCREEN_HEIGHT

        if next_x < boundary_left:
            next_x = boundary_left
        if next_x > boundary_right:
            next_x = boundary_right
        if next_y < boundary_top:
            next_y = boundary_top
        if next_y > boundary_bottom:
            next_y = boundary_top

        return (next_x, next_y)


class FollowCamera(object):
    """
        a camera that follows a target, the target
        appears in the middle of the screen, it uses
        the target's rect object and the screen dimensions
        to center the target on the screen.
    """

    def __init(self, pos=(0, 0)):
        self.__pos = pos

    def apply(self):
        return (-self.__pos[0], -self.__pos[1])

    def update(self, target):
        self.__pos = (
            target.rect.left - SCREEN_WIDTH / 2,
            target.rect.top - SCREEN_HEIGHT / 2,
        )
