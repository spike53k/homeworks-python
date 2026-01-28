class Weapon:
    def __init__(self,damage, modifier):
        self.damage = damage
        self._modifier = modifier

    def get_final_damage(self):
        return self.__apply_modifier()

    def __apply_modifier(self):
        return self.damage * self._modifier

w1 = Weapon(25, 1.2)
print(w1.get_final_damage())