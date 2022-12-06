class Superhero:
    
    people = 'people'
    
    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    
    def name_print(self):
        print(f'{self.name}')
    
    def double_health(self):
        print(self.health_points * 2)
    
    def others(self):
        print(f'nickname: {self.nickname}, superpower: {self.superpower}, health: {self.health_points}')
    
    def length(self):
        print(len(self.catchphrase))

hero = Superhero('Killua', 'Killer', 'Thunder', 100, 'jnsjnjd fjif')
hero.name_print()
hero.double_health()
hero.others()
hero.length()