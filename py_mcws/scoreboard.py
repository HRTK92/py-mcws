import py_mcws

class ScoreBoard:
    def __init__(self, name, display_name):
        self.name = name
        self.display_name = display_name
        self.conditions = "dummy"
        await self.command(f"scoreboard objectives add {self.name} {self.conditions} {self.display_name}")

    def players_add(self, name, number):
        pass

    def players_remove(self, name):
        pass

    def players_set(self, name, number):
        pass

    async def show(self, display_position="sidebar"):
        self.display_position = display_position
        await self.command(f"scoreboard objectives setdisplay {self.display_position} {self.name} ascending")
