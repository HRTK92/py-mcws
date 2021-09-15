from .server import WsClient

class ScoreBoard:
    def __init__(self, name, display_name):
        self.name = name
        self.display_name = display_name
        self.conditions = "dummy"

    async def create(self):
        await self.command(f"scoreboard objectives add {self.name} {self.conditions} {self.display_name}")

    async def players_add(self, name, number):
        pass

    async def players_remove(self, name):
        pass

    async def players_set(self, name, number):
        pass

    async def show(self, display_position="sidebar"):
        self.display_position = display_position
        await self.command(f"scoreboard objectives setdisplay {self.display_position} {self.name} ascending")
