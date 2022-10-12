class Movement:

    x_loc: int = 0
    y_loc: int = 0
    is_ducking = False

    def __init__(self, movement_speed: int, jump_height: int):
        print("Hello, I am a thing that can move!")
        self.movement_speed = movement_speed
        self.jump_height = jump_height