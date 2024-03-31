class Plant():
    def __init__(self, dehydration_rate, mature_time, plant_type, x, y):
        self.type = plant_type
        self.hydration = 100 #Percent
        self.dehydration_rate = dehydration_rate #Percent/tick
        self.time_left = mature_time #Seconds
        self.x = x
        self.y = y

    def harvest(self):
        pass #I forgot how to delete classes and im on a plane with no wifi rn

    def water(self):
        self.hydration = 100 #Percent

    def tick(self):
        self.hydration += self.dehydration_rate
        self.time_left += -0.1

class SingleHarvest(Plant):
    def __init__(self, dehydration_rate, mature_time, plant_type, x, y):
        super.__init__(dehydration_rate, mature_time, plant_type, x, y)

# class MultiHarvest(Plant()):
# #    super.__init__()
#     pass
#
# class SeedDropper(Plant()):
# #    super.__init__()
#     pass