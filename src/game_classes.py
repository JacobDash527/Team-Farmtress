import ui_classes
import textures

class Plant():
    def __init__(self, dehydration_rate, mature_time, plant_type, x, y, texture):
        self.type = plant_type
        self.hydration = 100 #Percent
        self.dehydration_rate = dehydration_rate #Percent/tick
        self.time_left = mature_time #Seconds
        self.x = x
        self.y = y
        self.button = ui_classes.Button(x * 180 +120, y * 180 + 250, texture, 1.4)
        self.menu_open = True
        self.dehydrated = False
        self.old = False
        self.stage_scale = 1

    def water(self):
        self.hydration = 100 #Percent
        self.dehydrated = False

    def tick(self):
        self.hydration += -self.dehydration_rate
        self.time_left += -0.1
        if self.hydration <= 10:
            self.dehydrated = True
    
    def is_clicked(self):
        return(self.button.is_clicked())
    
    def draw(self, x, y):
        self.button.draw(x * 180 + 120, y * 180 + 250, self.stage_scale, self.dehydrated)

class SingleHarvest(Plant):
    def __init__(self, dehydration_rate, mature_time, plant_type, x, y, texture):
        self.value = 69
        super().__init__(dehydration_rate, mature_time, plant_type, x, y, texture)

    def harvest(self):
        return([self.value, 0])

class SeedDropper(Plant):
    def __init__(self, dehydration_rate, mature_time, plant_type, x, y, texture):
        self.value = 69
        super().__init__(dehydration_rate, mature_time, plant_type, x, y, texture)

    def harvest(self):
        return([self.value, 2])