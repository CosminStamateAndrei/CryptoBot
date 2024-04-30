import discord
from discord import Intents, Profile
from discord.ext import commands, tasks
import pandas as pd
import json
import time

client = commands.Bot(command_prefix='.')

def write_json(data):
    with open ('db.json', "w") as f:
        json.dump(data, f, indent=4)


@client.event
async def on_ready():
  print("Bot is ready")
  # algo.start()
  # srm.start()
  # xtz.start()
  # alc.start()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Chihiro\'s dreams! <3"))

@client.event
async def on_voice_state_update(member, before, after):
  with open("db.json") as json_file:
    data = json.load(json_file)
    temp = data["users"]
    if after.mute == False:
      for user in temp:
        if str(member.id) == user['user_id']:
          if user['muted'] == "True":
            await set_to_muted(member)
            time.sleep(0.5)
    elif after.mute == True:
      for user in temp:
        if str(member.id) == user['user_id']:
          if user['muted'] == "False":
            await set_to_unmuted(member)
            time.sleep(0.5)



@client.event
async def on_member_join(member):
  hasAccount = False
  with open("db.json") as json_file:
      data = json.load(json_file)
      temp = data["users"]
      y = {"user_id": f"{member.id}", "name": f"{member.name}", "mod": "False", "admin": "False", "muted": "False", "mutedby": "0"}
      for user in temp:
          if str(member.id) == user['user_id']:
              hasAccount = True
      if hasAccount == False:
          temp.append(y)
  write_json(data)


# @tasks.loop(seconds=420)
# async def srm():
#   rightChannel = client.get_channel(888142354442244116)
#   url = "https://coinmarketcap.com/currencies/serum/"
#   dfs = pd.read_html(url, header=0)
#   tabled = pd.read_html(url, match='Serum Price')[0]
#   actlprice = float(tabled[1][0].split('$')[1])
#   df = dfs[0]
#   await rightChannel.send(f'```{df}```')
#   if actlprice <= 8.07 and actlprice >= 7.3:
#     await rightChannel.send('@everyone')
#     await rightChannel.send('```SRM DID HIT ENTRY```')

# @tasks.loop(seconds=420)
# async def algo():
#   rightChannel = client.get_channel(888713718832168990)
#   url = "https://coinmarketcap.com/currencies/algorand/"
#   dfs = pd.read_html(url, header=0)
#   tabled = pd.read_html(url, match='Algorand Price')[0]
#   actlprice = float(tabled[1][0].split('$')[1])
#   df = dfs[0]
#   await rightChannel.send(f'```{df}```')
#   if actlprice <= 1.33 and actlprice >= 1.25:
#     await rightChannel.send('@everyone')
#     await rightChannel.send('```ALGO DID HIT ENTRY```')
  
# @tasks.loop(seconds=420)
# async def xtz():
#   rightChannel = client.get_channel(889476556362231818)
#   url = "https://coinmarketcap.com/currencies/tezos/"
#   dfs = pd.read_html(url, header=0)
#   tabled = pd.read_html(url, match='Tezos Price')[0]
#   actlprice = float(tabled[1][0].split('$')[1])
#   df = dfs[0]
#   await rightChannel.send(f'```{df}```')
#   if actlprice <= 4.706 and actlprice >= 4.2:
#     await rightChannel.send('@everyone')
#     await rightChannel.send('```XTZ DID HIT ENTRY```')

# @tasks.loop(seconds=420)
# async def alc():
#   rightChannel = client.get_channel(889484774220103700)
#   url = "https://coinmarketcap.com/currencies/myneighboralice/"
#   dfs = pd.read_html(url, header=0)
#   tabled = pd.read_html(url, match='MyNeighborAlice')[0]
#   actlprice = float(tabled[1][0].split('$')[1])
#   df = dfs[0]
#   await rightChannel.send(f'```{df}```')
#   if actlprice <= 3.52 and actlprice >= 2.5 :
#     await rightChannel.send('@everyone')
#     await rightChannel.send('```ALC DID HIT ENTRY```')



@client.command()
async def clear(ctx, amount):
  with open("db.json") as json_file:
    data = json.load(json_file)
    temp = data["users"]
    for user in temp:
      if str(ctx.author.id) == user['user_id']:
        if user['admin'] == "True":
          amount = int(amount)
          await ctx.channel.purge(limit=1)
          await ctx.channel.purge(limit=amount)
          return
        if user['mod'] == "True":
          amount = int(amount)
          if amount <= 3:
            await ctx.channel.purge(limit=1)
            await ctx.channel.purge(limit=amount)
          else:
            await ctx.channel.purge(limit=1)
            await ctx.channel.send('```Grief suspected!```', delete_after = 3)



@client.command(aliases=['cc'])
async def clearall(ctx):
  if ctx.author.id == 248143211007180810 or ctx.author.id == 518331788880510979:
    await ctx.channel.purge(limit=100)

@client.command()
async def stop(ctx):
  if ctx.author.id == 518331788880510979:
    exit()

@client.command()
async def register(ctx):
    hasAccount = False
    with open("db.json") as json_file:
        data = json.load(json_file)
        temp = data["users"]
        y = {"user_id": f"{ctx.author.id}", "name": f"{ctx.author.name}", "mod": "False", "admin": "False", "muted": "False", "mutedby": "0"}
        for user in temp:
            if str(ctx.author.id) == user['user_id']:
                await ctx.send('```You already have an account```')
                hasAccount = True
        if hasAccount == False:
            temp.append(y)
            await ctx.send('```Account created succesfully```')
    write_json(data)

@client.command()
async def reg(ctx, member: discord.Member):
  hasAccount = False
  with open("db.json") as json_file:
        data = json.load(json_file)
        temp = data["users"]
        y = {"user_id": f"{member.id}", "name": f"{member.name}", "mod": "False", "admin": "False", "muted": "False", "mutedby": "0"}
        for user in temp:
            if str(member.id) == user['user_id']:
                await ctx.send('```He already has an account```')
                hasAccount = True
        if hasAccount == False:
            temp.append(y)
            await ctx.send('```Account created succesfully```')
  write_json(data)

@client.command()
async def givemod(ctx, targetMen: discord.Member):
  with open("db.json") as json_file:
    data = json.load(json_file)
    temp = data["users"]
    for user in temp:
      if str(ctx.author.id) == user['user_id']:
        if user['admin'] == "True":
          pass
        else:
          return
    for user in temp:
        if str(targetMen.id) == user['user_id']:
          user['mod'] = "True"
    write_json(data)

@client.command(aliases = ["newchart", "nc"])
async def create_chart():
  with open("db.json") as json_file:
    data = json.load(json_file)
    temp = data["users"]

@client.command()
async def mute(ctx, member: discord.Member):
  with open("db.json") as json_file:
    data = json.load(json_file)
    temp = data["users"]
    for user in temp:
      if str(ctx.author.id) == user['user_id']:
        if user['admin'] == "True":
          pass
        else:
          return
    for user in temp:
      if str(member.id) == user['user_id']:
        if member.id != 518331788880510979 and member.id != 248143211007180810: 
          user['muted'] = "True"
          user['mutedby'] = str(ctx.author.id)
          try:
            channel = member.voice.channel.id
          except Exception:
            await ctx.channel.send("He is in no channel.")
        else:
          await ctx.channel.send('```WASTED! Smecherii fut, fraierii comenteaza. Cu multa stima si respect.```', delete_after = 4)
          return
    write_json(data)
    await set_to_muted(member)


@client.command()
async def unmute(ctx, member: discord.Member):
  with open("db.json") as json_file:
    data = json.load(json_file)
    temp = data["users"]
    for user in temp:
      if str(ctx.author.id) == user['user_id']:
        if user['admin'] == "True":
          pass
        else:
          return
    for user in temp:
      if str(member.id) == user['user_id']:
        if user['mutedby'] == str(ctx.author.id) or ctx.author.id == 518331788880510979 or ctx.author.id == 248143211007180810:
          user['muted'] = "False"
          user['mutedby'] = "0"
          try:
            channel = member.voice.channel.id
          except Exception:
            await ctx.channel.send("He is in no channel.")
    write_json(data)
    await set_to_unmuted(member)

async def set_to_muted(member: discord.Member):
    await member.edit(mute=True)

async def set_to_unmuted(member: discord.Member):
    await member.edit(mute=False)

client.run('')