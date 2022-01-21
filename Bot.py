import config


class Bot():
    def __init__(self, prefix, activity, client, token):
        self.prefix = prefix
        self.activity = activity
        self.token = token
        self.client = client
        self.commands = config.commands

    def run(self):
        self.client.run(self.token)

    async def change_status(self):
        await self.client.change_presence(activity=self.activity)
