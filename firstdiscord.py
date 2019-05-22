import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("botstart")
    game = discord.Game("KartRider")
    await client.change_presence(status=discord.Status.idle, activity=game)

    @client.event
    async def on_message(message):
     if message.content.startswith("Hi"):
           await message.channel.send("안녕하세요")



client.run("NTgwMTkyOTUxNjQxMDQ3MDU2.XOPpAg.7WwZjTchkMiRVIyxAptw5VkdZhI")