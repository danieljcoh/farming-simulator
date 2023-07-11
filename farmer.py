from crop import Crop


class Farmer:
    def __init__(self, name):
        self.name = name
        self.garden = []
        # Eventually we will want to update the plot size - update_plot()
        self.plot_size = 8
        self.money = 100

    def add_to_garden(self, crop):
        self.garden.append(crop.name)
        print(f"{self.name} added {crop.name} to their garden.")

    def show_info(self):
        print(f"The crops in your garden are: {self.garden}")
        print(f"You have ${self.money}.")
        print(f"You have {self.plot_size}, plots left.")

    def turn(self, turn_counter):
        turn_counter += 1
        answer = input("What do you want to do? (plant)").lower()
        if answer == "plant":
            self.plant_crop()

    def plant_crop(self):
        answer = input("Which crop do you want to plant? ").lower()
        crop = Crop(answer, )
        while answer not in corn.crops_available:
            if answer in corn.crops_available:
                pass
            else:
                print("Please input an existent crop to plant.")
                answer = input("Which crop do you want to plant? ").lower()

