import discord, random, os
from discord.ext import commands
from keep_alive import keep_alive
from discord.utils import find
import requests

# bot made by goose.mp4

# discord.py API docs: https://discordpy.readthedocs.io/en/latest/api.html
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='?', intents=intents)
client.remove_command('help')



# loads all the cogs into 'main.py'
client.load_extension('cogs.commands')



@client.event
async def on_member_join(member):
	"""Sends a welcome message to a specific channel"""

	await client.wait_until_ready()
	channel = client.get_channel(862815252964966421)

	await channel.send(f"Welcome <@{member.id}>")

	await member.add_roles(member.guild.get_role(862811433662545940))
	await member.add_roles(member.guild.get_role(862813454812971088))
	await member.add_roles(member.guild.get_role(862829754779303956))
	await member.add_roles(member.guild.get_role(862813524870299668))

	welcomeEmbed = discord.Embed(
		title="Welcome to AISLE #7",
		description=f"Hey {member.name}! Welcome to AISLE #7 Coding Support. This server is for supporting people in programming in a large variety of languages. Please read the <#862808578502557721> to know our rules and info."
	)

	welcomeEmbed.add_field(
		name="How do I view support channels?",
		value="You need to get a programming language role from <#862808591505555466>. That will give you access to the general purpose coding channel and your language specific one.\n\nPlease **do not** ask for coding support in channels that are not dedicated to supporting you."
	)

	welcomeEmbed.add_field(
		name="How do I get support?",
		value="Go to one of the support channels once you have a role(s). You can then post your problem there. Please provide brief context on the purpose of code you are showing, the problems, where the problems are, and a snippet of the code. This will speed up helping you as there will be less questions and more fixing.\nFeel free the ping one of the support roles that is relative to the language you are working in if you need help urgently/you've been waiting for a while."
	)

	welcomeEmbed.set_thumbnail(
		url="https://cdn.discordapp.com/avatars/862836714727800883/82cc098b26ae9a49ba4ee3534026420c.webp?size=1024"
	)
	await member.send("** :exclamation: Please read me before asking questions in the server**")
	await member.send(embed=welcomeEmbed)

	if member.bot is True:
		await member.add_roles(member.guild.get_role(862813915652948008))




@client.event
async def on_member_remove(member):
	"""Sends a goodbye message to a specific channel"""

	await client.wait_until_ready()
	channel = client.get_channel(862857766804520971)

	await channel.send(f"Goodbye <@{member.id}>!")



# if a command flags an error it handles it
@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("You're missing some arguements for this command. Try again.")
		return

	if isinstance(error, commands.BotMissingPermissions):
		await ctx.send("I'm missing permissions to do this!")

	if isinstance(error, commands.ChannelNotFound):
		await ctx.send("Channel not found.")

	if isinstance(error, commands.CommandNotFound):
		return

	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send("Command on cooldown!")
		return

	if isinstance(error, commands.NotOwner):
		await ctx.send("Sorry! You're not the owner, you can't do that.")

	if isinstance(error, commands.MemberNotFound):
		await ctx.send("The member you mentioned couldn't be found... try again.")
		return

	if isinstance(error, commands.MissingRole):
		return

	if isinstance(error, commands.TooManyArguments):
		await ctx.send("That's too many arguements!")
		return

	if isinstance(error, commands.RoleNotFound):
		await ctx.send("I can't find that role! Check your spelling.")

	if isinstance(error, commands.UserNotFound):
		await ctx.send("I can't find that user.")

	if isinstance(error, commands.UserInputError):
		await ctx.send("Something you input caused an error.")
		return

	if isinstance(error, commands.ArgumentParsingError):
		return

	if isinstance(error, commands.BadArgument):
		return

	if isinstance(error, commands.BadBoolArgument):
		return

	if isinstance(error, commands.BadColourArgument):
		return

	if isinstance(error, commands.BadInviteArgument):
		return

	if isinstance(error, commands.BadUnionArgument):
		return

	if isinstance(error, commands.CommandError):
		return

	if isinstance(error, commands.CommandRegistrationError):
		return

	if isinstance(error, commands.ConversionError):
		return

	if isinstance(error, commands.EmojiNotFound):
		await ctx.send("I can't find that emoji.")
		return

	if isinstance(error, commands.ExtensionError):
		return

	if isinstance(error, commands.ExtensionAlreadyLoaded):
		return

	if isinstance(error, commands.ExtensionFailed):
		return

	if isinstance(error, commands.ExtensionNotFound):
		return

	if isinstance(error, commands.ExtensionNotLoaded):
		return

	if isinstance(error, commands.NoEntryPointError):
		return

	if isinstance(error, commands.NoPrivateMessage):
		await ctx.send("Private messages not allowed!")
		return

	if isinstance(error, commands.NSFWChannelRequired):
		await ctx.send("NSFW channel required.")
		return

	if isinstance(error, commands.PrivateChannel):
		await ctx.send("That's a private channel.")
		return

	else:
		print("Error")
		return


# -----
keep_alive()
client.run(os.getenv('token'))