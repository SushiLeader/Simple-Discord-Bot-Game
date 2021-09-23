from discord.ext import commands
from useraccount import beg_money, register_account, check_balance


client = commands.Bot(command_prefix='$')


@client.command()
async def register(ctx):
    await ctx.send(register_account(ctx.author.id))


@client.command()
async def beg(ctx):
    await ctx.send(beg_money(ctx.author.id))


@client.command()
async def balance(ctx):
    await ctx.send(check_balance(ctx.author.id))


client.run('TOKEN')
