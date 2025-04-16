import random

class Skill:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Player:
    def __init__(self, name, skills):
        self.name = name
        self.hp = 100
        self.skills = skills

    def handle_damage(self, damage):
        # self.hp -= damage
        self.hp = self.hp - damage

        if self.hp < 0:
            self.hp = 0
        
        return self.hp
    
    def choose_skill(self):
        skill_choice = int(input('Elige una habilidad: '))

        if skill_choice < 0 or skill_choice >= len(self.skills):
            print("Habilidad no válida. Intenta de nuevo.")
            return False

        skill = self.skills[skill_choice]
        return skill
    

class Bot(Player):
    def __init__(self, name, skills):
        super().__init__(name, skills)

    def choose_skill(self):
        skill_choice = random.randint(0, len(self.skills) - 1)
        skill = self.skills[skill_choice]
        return skill

class Game:
    def __init__(self, player1, player2):
        self.isRunning = True
        self.p1 = player1
        self.p2 = player2
        self.current_player = random.choice([self.p1, self.p2])

    def run(self):
        # Loop principal del juego
        while self.isRunning:
            # Lógica del juego
            print(f"Turno de {self.current_player.name}")
            print(f"HP de {self.p1.name}: {self.p1.hp}")
            print(f"HP de {self.p2.name}: {self.p2.hp}")

            if self.current_player == self.p1:
                # Turno del jugador 1, elegir habilidad -- Input en consola
                for i, skill in enumerate(self.p1.skills):
                    print(f"{i}. {skill.name} (Daño: {skill.damage})")

                skill = self.p1.choose_skill()

                if skill is False:
                    continue

                self.p2.handle_damage(skill.damage)

                print(f'{self.p1.name} usa {skill.name} contra {self.p2.name} causando {skill.damage} de daño.')
                    

            if self.current_player == self.p2:
                # Turno del jugador 2, elegir habilidad -- IA simple aleatoria
                
                skill = self.p2.choose_skill()
                self.p1.handle_damage(skill.damage)

                print(f'{self.p2.name} usa {skill.name} contra {self.p1.name} causando {skill.damage} de daño.')

            if self.current_player == self.p1 and self.p2.hp <= 0:
                print(f"{self.p2.name} ha sido derrotado.")
                self.isRunning = False
                
            if self.current_player == self.p2 and self.p1.hp <= 0:
                print(f"{self.p1.name} ha sido derrotado.")
                self.isRunning = False

            if self.current_player == self.p1:
                self.current_player = self.p2
            else:
                self.current_player = self.p1



if __name__ == "__main__":

    player1 = Player("Player 1", [
        Skill("Fireball", 20),
        Skill("Ice Spike", 15),
        Skill("Lightning Bolt", 25),
        Skill("Earthquake", 30),
    ])
    player2 = Bot("Player 2", [
        Skill("Shadow Strike", 20),
        Skill("Wind Slash", 15),
        Skill("Water Wave", 25),
        Skill("Rock Slide", 30),
    ])

    game = Game(player1, player2)

    game.run()
