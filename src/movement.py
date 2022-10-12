class Movement:

    x_loc: int = 0
    y_loc: int = 0
    is_ducking = False
    is_sliding = False #can remove this later but just an idea

    def __init__(self, movement_speed: int, jump_height: int, ducking_height: int,
                 sliding_height: int):
        print("Hello, I am a thing that can move!")
        self.movement_speed = movement_speed
        self.jump_height = jump_height
        self.ducking_height = ducking_height
        self.sliding_height = sliding_height