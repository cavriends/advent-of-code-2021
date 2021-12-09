with open("example.txt") as f:
    initial_state = list(map(int, f.read().split(",")))

class lanternFish:
    def __init__(self, born=True, timer=9):
        if born:
            self.timer = timer
        else:
            self.timer = timer

    def decrease_timer(self):
        if self.timer == 0:
            self.timer = 6
        else:
            self.timer -= 1

    def get_timer(self):
        return self.timer


class simulatePopulation:
    def __init__(self, days, initial_state):
        self.days = days
        self.state = initial_state
        self.pool = []

    def create_pool(self):
        for value in self.state:
            self.pool.append(lanternFish(born=False, timer=value))

    def add_fish(self):
        self.pool.append(lanternFish())

    def simulate(self, verbose=False):
        self.create_pool()
        create_fish_counter = 0
        for day in range(self.days):
            for i in range(create_fish_counter):
                self.add_fish()
            create_fish_counter = 0
            for fish_number, fish in enumerate(self.pool):
                self.pool[fish_number].decrease_timer()
                if fish.get_timer() == 0:
                    create_fish_counter += 1

            timer_values = list(map(lambda obj: obj.get_timer(), self.pool))

            if not verbose:
                print(f"After \t {day+1}: \t {timer_values}")


            print(f"{round(((day+1)/self.days)*100,4)}%")
            pool_size = len(timer_values)


        return pool_size

fish_simulation = simulatePopulation(80, initial_state)
final_pool_size = fish_simulation.simulate(True)

print(f"Answer: {final_pool_size}") # 355386
