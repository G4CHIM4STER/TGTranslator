# НЕ ЗАБУДЬ ПОМЕНЯТЬ ТОКЕН БОТА !
from discord.ext import commands

bot = commands.Bot(command_prefix='$')
role_list = []

@bot.event # Выводит сообщение о начале работы бота
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    


@bot.command()
async def say(ctx, arg):
    await ctx.send(arg)

#region Основной функционал по приему комманд

@bot.event
async def on_message(message): # "Принимаем" сообщения
    if message.author == bot.user:
        return

    if message.content.startswith('$привет'): # Приветствие
        await message.channel.send('Пошел нахуй!')

    if message.content.startswith('$анонс'): # Создание анонса (в дальнейшем)
        for x in range(len(message.role_mentions)): # Тут реализовано механизм выделения указанных в сообщении ролей
            role = message.role_mentions[x]
            print(role)

            await message.channel.send(message.role_mentions[x]) # выделение нужной роли

#endregion        

@bot.command()
async def test(ctx, *args):
     await ctx.send('{} аргумента: {}'.format(len(args), ','.join(args)))



bot.run('MTAwNzI4NTY1NjI3MzMwMTU5NQ.GdX3Mh.LAsDgiAiOOZbfl9cN2H_eKMKhOMWNGgiib7lKI')