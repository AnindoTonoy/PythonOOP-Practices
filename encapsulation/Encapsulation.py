class Speed:
    def __init__(self):
        self.speed = 10
        self.__new_speed = 80  # private attribute starts with __

    # getter method
    def get_new_speed(self):
        return self.__new_speed

    # setter method
    def set_new_speed(self, new_speed):
        self.__new_speed = new_speed


s = Speed()
print("Normal speed:", s.speed)

# s.__new_speed = 100
print("New speed:", s.get_new_speed())

print("--------")

s.set_new_speed(250)                            # Set new speed as 250
print("set_new_speed:", s.get_new_speed())      # Get new speed as 250
