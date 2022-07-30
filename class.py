class profile:

    def __init__(self, name, age, country):
        self.name = 'Gbolahan'
        self.age = 28
        self.country = 'Nigeria'
    
    def update(self):
        self.name = 'Shola'
        self.age = 30
        self.country = 'Ghana'
  
p = profile()
p.update()

print(p.country)


