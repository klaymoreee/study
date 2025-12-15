class Hero():

  def __init__(self, name, posessions):
    self.name = name
    self.posessions = posessions
    self.refactor_posessions = ', '.join(self.posessions)

  def __repr__(self):
      
      return f'Герой {self.name} взял с собой {self.refactor_posessions}'
# Не удаляйте код ниже, он нужен для проверки

hero = Hero("Питомир", ["меч", "плащ", "шляпа"]) 
print(hero)