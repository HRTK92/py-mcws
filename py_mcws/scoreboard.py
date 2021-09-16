class ScoreBoard:
    def __init__(self, name, display_name):
        self = WsClient
        self.name = name
        self.display_name = display_name
        self.conditions = "dummy"

    async def create(self):
        await self.command(f"scoreboard objectives add {self.name} {self.conditions} {self.display_name}")

    async def remove(self):
        await self.command(f"scoreboard objectives remove {self.name} {self.conditions} {self.display_name}")
    
    async def players_add(self, player, number):
        pass

    async def players_remove(self, player):
        pass

    async def players_set(self, player, number):
        await self.command(f"scoreboard players set {player} {self.name} {number}")

    async def show(self, display_position="sidebar"):
        self.display_position = display_position
        await self.command(f"scoreboard objectives setdisplay {self.display_position} {self.name} ascending")
