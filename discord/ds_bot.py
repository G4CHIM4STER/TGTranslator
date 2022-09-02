# НЕ ЗАБУДЬ ПОМЕНЯТЬ ТОКЕН БОТА !
import discord

role_list = []

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event # Выводит сообщение о начале работы бота
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(discord.Guild.members)
    # for x in discord.Role.members:
    #     print(discord.Guild.members[x])
    
#region Основной функционал по приему комманд

@client.event
async def on_message(message): # "Принимаем" сообщения
    if message.author == client.user:
        return

    if message.content.startswith('$привет'): # Приветствие
        await message.channel.send('Пошел нахуй!')

    if message.content.startswith('$анонс'): # Создание анонса (в дальнейшем)
        for x in range(len(message.role_mentions)): # Тут реализовано механизм выделения указанных в сообщении ролей
            role = message.role_mentions[x]
            print(role)

            await message.channel.send(message.role_mentions[x]) # выделение нужной роли

#endregion        

client.run('MTAwNzI4NTY1NjI3MzMwMTU5NQ.G-EsDM.c1gB7Mu6ggJtMCV-jwB1JxG4OTTW8XR4vVQaqE')