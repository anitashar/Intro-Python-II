
class Items:
    def __init__(self,name,description):
        self.name = name
        self.description = description


    def __str__(self):
        return f"{self.name}: {self.description}"


    def on_take(self):
        print(f'\n You pick up the {self.name}.\n')

    def on_drop(self):
        print(f"\nYou drop the {self.name}.\n")