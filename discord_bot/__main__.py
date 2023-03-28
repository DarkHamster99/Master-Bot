import discord
from discord.ext import commands

from dotenv import load_dotenv
from os import getenv

load_dotenv()

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

#hi

@bot.slash_command(name="hello", description="send hello")
async def hello(ctx):
    emoji = await ctx.guild.fetch_emoji(1086182653188898816)
    await ctx.respond(f'Hello! {ctx.author.name} <:kekw:1086182653188898816>')

#commands

@bot.slash_command()
async def nice(ctx):
    await ctx.respond('haha, Im the best')

@bot.slash_command()
async def add(ctx, num1:int, num2:int):
    await ctx.respond(num1+num2)


@bot.slash_command()
async def subt(ctx, num3:int, num4:int):
    await ctx.respond(num3-num4)

@bot.slash_command()
async def mult(ctx, num5:int, num6:int):
    await ctx.respond(num5*num6)

@bot.slash_command(name="first_slash")
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command!")

#rules

@bot.slash_command()
async def rules(ctx):
    rules_embed = discord.Embed(
        description ='1- ممنوع السب و الشتم يكافة أنواعه\n2- ممنوع إرسال فيديوهات كرينج مثل ببجي\n3- ممنوع إرسال لنكات بكافة أنواعها إلا المفيدة \n4- ممنوع التتافه\n5- ممنوع نشر صور لنساء متبرجات',
        color = discord.Color.dark_blue()
    )

    await ctx.respond(embed=rules_embed)

#kick & ban

@bot.event
async def on_message(message):
    badwords = ["خرة", "زفت", "Fuck", "اللعنة", "ينعل","اخرس","انقلع", "يا ابن"]

    for word in badwords:
        if word in message.content: 
            await message.author.kick(reason=None)
            break 

#give role member to a new member join the server

@bot.event
async def on_member_join(member):
    guild = member.guild
    welcome_channel: discord.TextChannel = await guild.fetch_channel("1085933548361502800")
    
    welcome_embed = discord.Embed(
        description =f"hello <@{member.id}> <:kekw:1086182653188898816>",
        color = discord.Color.red()
    ).set_author(name=member.name, icon_url=member.display_avatar)
    
    member_role = guild.get_role(1085929545141600296)
    await member.add_roles(member_role)
    await welcome_channel.send(embed=welcome_embed)
@bot.event
async def on_ready():
    print("logged in!")

#TOKEN

bot.run(getenv('BOT_TOKEN'))


