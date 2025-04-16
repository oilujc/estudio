import random, os, time

class Horse:
    def __init__(self, name):
        self.name = name
        self.speed = random.random() * 5 + 1  # Velocidad entre 1 y 5

    def move(self):
        # Simula el movimiento del caballo
        distance = random.random() * self.speed

        distance = int(distance) 


        return distance

    
class Game:
    def __init__(self, horses):
        self.horses = horses
        self.isRunning = True
        self.winner = None
        self.max_distance = 100
        self.bet = None

        self.current_distance = {i: 0 for i, horse in enumerate(self.horses)}
        
        # current_distance = {}
        # for i, horse in enumerate(self.horses):
        #     current_distance[i] = 0

    def set_bet(self):
        while True:
            bet = int(input(f'A qué caballo quieres apostar? (0, {len(self.horses) - 1}): '))
            if bet < 0 or bet >= len(self.horses):
                print("Caballo no válido. Intenta de nuevo.")
                continue
            
            self.bet = bet
            break

    def run(self):
        while self.isRunning:
    
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')

            mapper = {}

            for i, horse in enumerate(self.horses):
                mapper[i] = f'{i}.' + '-' * self.max_distance

                # Reemplazamos los guiones por @ en la posición actual del caballo
                position = self.current_distance[i]
                mapper[i] = mapper[i][:position] + '@' + mapper[i][position + 1:]

            for i, horse in enumerate(self.horses):
                distance = horse.move()
                self.current_distance[i] += distance

                if self.current_distance[i] > self.max_distance:
                    self.current_distance[i] = self.max_distance


            # imprimimos el estado actual de la carrera
            for i, position in mapper.items():
                print(f"{position}")


            # Verificamos si algún caballo ha llegado a la meta
            for i, distance in self.current_distance.items():
                if distance >= self.max_distance:
                    self.winner = self.horses[i]
                    print(f"¡{self.winner.name} ha ganado la carrera!") 
                    self.isRunning = False
                    break

        # Imprimimos el resultado final
        print("\nResultados finales:")
        results = []
        for i, horse in enumerate(self.horses):
            results.append((horse.name, horse.speed, self.current_distance[i], i))

        results.sort(key=lambda x: x[2], reverse=True)

        print("Caballos en orden de llegada:")
        for i, horse in enumerate(results):
            print(f"{horse[3]} ({horse[0]}).: {horse[2]} metros (Velocidad: {horse[1]:.2f})")

        print(f"Tu caballo: {self.horses[self.bet].name}")
        print(f"Caballo ganador: {self.winner.name}")

if __name__ == '__main__':
    # Definimos los caballos
    horses = [
        Horse("Spirit"),
        Horse("Shadow"),
        Horse("Thunder"),
        Horse("Blaze"),
        Horse("Storm"),
        Horse("Comet"),
        Horse("Lightning"),
    ]

    # Creamos el juego
    game = Game(horses)
    game.set_bet()

    # Iniciamos el juego
    game.run()