class Movement:

    x_loc: int = 0
    y_loc: int = 0 # should be located at the feed
    is_ducking = False
    is_sliding = False #can remove this later but just an idea
    is_jumping = False

    def __init__(self, movement_speed: int, height: int, jump_height: int, ducking_height: int,
                 sliding_height: int):
        print("Hello, I am a thing that can move!")
        self.movement_speed = movement_speed
        self.height = height
        self.jump_height = jump_height
        self.ducking_height = ducking_height
        self.sliding_height = sliding_height

    def slide_start(self):
        self.is_sliding = True

    def slide_end(self):
        # IF THERE IS A BLOCK ABOVE
            # KEEP SLIDING
        # ELSE
        self.is_sliding = False

    def get_current_height(self):
        if self.is_sliding:
            return self.sliding_height
        elif self.is_ducking:
            return self.ducking_height
        else:
            return self.height
