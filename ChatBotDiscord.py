import discord
from discord.ext import commands
import math

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def calculadora(ctx,operacion:str,num1:int,num2:int):
    if operacion == "suma":
        resultado=num1 + num2
        await ctx.send(f"El resultado de la suma es {resultado}")
    if operacion == "resta":
        resultado=num1 - num2
        await ctx.send(f"El resultado de la resta es {resultado}")
    if operacion == "multiplicacion":
        resultado=num1 * num2
        await ctx.send(f"El resultado de la multiplicacion es {resultado}")
    if operacion == "division":
        if num2 != 0:
            resultado=num1 / num2
            await ctx.send(f"El resultado de la division es {resultado}")
        else:
            await ctx.send("la division entre cero no es posible :)")
    else:
        await ctx.send("la operacion que elejiste no son los correctos :(")
    


bot.run("aqui va tu token secreto :)")
 
