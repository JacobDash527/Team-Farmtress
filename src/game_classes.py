import ui_classes
import textures

class Plant():
    def __init__(self, x, y, dehydration_rate, plant_type, texture, value, stages, death):
        self.type = plant_type
        self.hydration = 100 #Percent
        self.dehydration_rate = dehydration_rate #Percent/tick
        self.x = x
        self.y = y
        self.button = ui_classes.Button(x * 135 + 90, y * 135 + 20, texture, 1.4)
        self.dehydrated = False
        self.stage_scale = 1
        self.time = 0
        self.initial_value = value
        self.value = 0
        self.stages = stages
        self.death = death
        self.stage = ''

    def water(self):
        self.hydration = 100 #Percent
        self.dehydrated = False

    def tick(self):
        destroy = False

        self.hydration += -self.dehydration_rate
        self.time += 0.1
        if self.hydration <= 10:
            self.dehydrated = True

        if self.time >= self.stages['baby'][0] and self.time < self.stages['child'][0]:
            self.value = self.initial_value * self.stages['baby'][1]
            self.stage_scale = self.stages['baby'][1] + 0.3
            self.stage = 'Baby'
        elif self.time >= self.stages['child'][0] and self.time < self.stages['adult'][0]:
            self.value = self.initial_value * self.stages['child'][1]
            self.stage_scale = self.stages['child'][1]
            self.stage = 'Child'
        elif self.time >= self.stages['adult'][0] and self.time < self.stages['elderly'][0]:
            self.value = self.initial_value * self.stages['adult'][1]
            self.stage_scale = self.stages['adult'][1]
            self.stage = 'Adult'
        elif self.time >= self.stages['elderly'][0]:
            self.value = self.initial_value * self.stages['elderly'][1]
            self.stage_scale = self.stages['elderly'][1]
            self.stage = 'Elderly'

        if self.hydration <= 0 or self.time == self.death:
            destroy = True

        return(destroy)

    def is_clicked(self):
        return(self.button.is_clicked())
    
    def draw(self, x, y):
        self.button.draw(x * 135 + 100 + 50 * (1-self.stage_scale), y * 135 + 20 + 50 * (1-self.stage_scale), self.stage_scale * 0.7, self.dehydrated)

    def get_stats(self):
        return(self.stage, round(self.hydration))

#----------------------------------------------------------------------------------------------------------

class SingleHarvest(Plant):
    def __init__(self, x, y, dehydration_rate, plant_type, texture, value, stages, death):
        super().__init__(x, y, dehydration_rate, plant_type, texture, value, stages, death)

    def harvest(self):
        return([self.value, 0, True])

class SeedDropper(Plant):
    def __init__(self, x, y, dehydration_rate, plant_type, texture, value, stages, death, seeds):
        self.seeds = seeds
        super().__init__(x, y, dehydration_rate, plant_type, texture, value, stages, death)

    def harvest(self):
        if self.time >= self.stages['adult'][0] and self.time < self.stages['elderly'][0]:
            pass
        else:
            self.seeds = 0
        return([self.value, self.seeds, True])

class MultiHarvest(Plant):
    def __init__(self, x, y, dehydration_rate, plant_type, texture, value, stages, death):
        super().__init__(x, y, dehydration_rate, plant_type, texture, value, stages, death)

    def harvest(self):
        destroy = True
        if self.time >= self.stages['adult'][0] and self.time < self.stages['elderly'][0]:
            destroy = False
        self.time = 0
        return([self.value, 0, destroy])

#----------------------------------------------------------------------------------------------------------

class PlainBread(SingleHarvest):
    def __init__(self, x, y):
        super().__init__(x, y, 0.2, 'plain_bread', textures.privileged_bread, 15, {'baby':[0, 0], 'child':[30, 0.7], 'adult':[70, 1], 'elderly':[100, 0.6]}, 120)

class BreadMonster(SeedDropper):
    def __init__(self, x, y):
        super().__init__(x, y, 0.2, 'bread_monster', textures.bread_monster, 4, {'baby':[0, 0], 'child':[30, 0.5], 'adult':[70, 1], 'elderly':[100, 0.75]}, 120, 5)

class BreadCrab(MultiHarvest):
    def __init__(self, x, y):
        super().__init__(x, y, 0.3, 'bread_crab', textures.bread_crab, 10, {'baby':[0, 0], 'child':[20, 0.7], 'adult':[60, 1], 'elderly':[80, 0.75]}, 110)

class BabaGanoush(SingleHarvest):
    def __init__(self, x, y):
        super().__init__(x, y, 0.1, 'baba_ganoush', textures.baba_ganoush, 0, {'baby':[0, 0], 'child':[30, 0.7], 'adult':[70, 1], 'elderly':[100, 0.6]}, 120)