# bear.py
class Bear:
    def __init__(self):
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        self.hunger_score += num_fish
Fish Class in fish.py
python
Copy code
# fish.py
class Fish:
    def __init__(self):
        self.age = 0

    def one_day(self):
        self.age += 1
River Class in rivers.py
python
Copy code
# rivers.py
class River:
    def __init__(self, num_fish: int, num_bears: int):
        self.day = 0
        self.bears = [Bear() for _ in range(num_bears)]
        self.fish = [Fish() for _ in range(num_fish)]

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        for bear in self.bears:
            bear.one_day()
        for fish in self.fish:
            fish.one_day()
        self.day += 1

    def one_river_week(self):
        for _ in range(7):
            self.one_river_day()

    def check_ages(self):
        self.bears = [bear for bear in self.bears if bear.age <= 5]
        self.fish = [fish for fish in self.fish if fish.age <= 3]

    def remove_fish(self, amount: int):
        self.fish = self.fish[amount:]

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]

    def repopulate_bears(self):
        new_bears = len(self.bears) // 2
        self.bears.extend([Bear() for _ in range(new_bears)])

    def repopulate_fish(self):
        new_fish = (len(self.fish) // 2) * 4
        self.fish.extend([Fish() for _ in range(new_fish)])
Test Script in river_simulation.py
python
Copy code
# river_simulation.py
from rivers import River

def main():
    my_river = River(10, 2)
    my_river.view_river()

    # Simulating one week
    my_river.one_river_week()
    my_river.view_river()

    # Additional tests
    my_river.check_ages()
    my_river.bears_eating()
    my_river.check_hunger()
    my_river.repopulate_bears()
    my_river.repopulate_fish()
    my_river.view_river()

if __name__ == "__main__":
    main()