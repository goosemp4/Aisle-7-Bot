import discord
from discord.ext import commands
from datetime import date

client = discord.Client()

suggestUrl = "https://cdn.discordapp.com/attachments/865993082297516052/865993157568757760/wrench.png"


class Cmds(commands.Cog):

	def __init__(self, client):
		self.client = client



	@commands.Cog.listener()
	async def on_message(self, message):
		"""Deletes a messaged that contains a blacklisted word"""


		msg = message.content

		blacklist = [" "]

		try:

			check = blacklist.index(msg)
			await message.delete()

		except ValueError:
			pass



	@commands.command()	
	#@commands.has_permissions()
	#@commands.has_role()
	async def mute(self, ctx, member : discord.Member):
		"""This command mutes a user"""

		await member.add_role("enter mute role here")
		await ctx.send(f"{member} has been muted.")



	@commands.command(pass_context=True)
	@commands.has_role(862811341772423190)
	async def kick(self, ctx, member : discord.Member, *, reason=None):
		"""This command kicks a user"""

		kickMessage = discord.Embed(
			title="Kicked",
			description=f"<@{member.id}> has been kicked from the server",
			color=0x0000FF
		)
		kickMessage.add_field(
			name="Reason",
			value=reason,
			inline=True
		)
		kickMessage.set_footer(
			text=f"kicked by {ctx.author.display_name}",
			icon_url=ctx.author.avatar_url
		)

		await member.kick(reason=reason)
		await ctx.send(embed=kickMessage)


	
	@commands.command(pass_context=True)
	@commands.has_role(862811341772423190)
	async def ban(self, ctx, member : discord.Member, *, reason=None):
		"""This command bans a user"""

		banMessage = discord.Embed(
			title="Banned",
			description=f"<@{member.id}> has been banned from the server",
			color=0x0000FF
		)
		banMessage.add_field(
			name="Reason",
			value=reason,
			inline=False
		)
		banMessage.set_footer(
			text=f"banned by {ctx.author.display_name}",
			icon_url=ctx.author.avatar_url
		)

		await member.ban(reason=reason)
		await ctx.send(embed=banMessage)

	

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	#@commands.has_role()
	async def purge(self, ctx, amount):
		"""This command purges x amount of messages"""

		purgeMessage = discord.Embed(
			title=f"{amount} messages have been deleted",
			color=0xFF0000
		)
		purgeMessage.set_footer(
			text=f"purged by {ctx.author.display_name}",
			icon_url=ctx.author.avatar_url
		)
		amount = int(amount)
		await ctx.channel.purge(limit=amount+1)
		await ctx.send(embed=purgeMessage)

	

	@commands.command()	
	async def suggest(self, ctx, *, suggestion=None):
		"""Commands that allows user to suggest things"""

		imgFile = discord.File(f"images/wrench.png", filename="image.png")

		channel = self.client.get_channel(865992973204193280)

		suggestEmbed = discord.Embed(
			title=f"Suggestion",
			description=suggestion,
			color= 0xa9a9a9 
		)
		suggestEmbed.set_author(
			name=f"{ctx.author}",
			icon_url=ctx.author.avatar_url
		)

		suggestEmbed.add_field(
			name="Suggested by",
			value=f"<@{ctx.author.id}>"
		)

		suggestEmbed.set_footer(
			text=f"Suggested on {date.today()}"
		)
		
		suggestEmbed.set_thumbnail(
			url="attachment://image.png"
		)

			
		if suggestion is None:
			errorEmbed = discord.Embed(
				title=":x: You didn't suggest anything! Try again.",
				color=0xFF0000
			)

			await ctx.reply(embed=errorEmbed, mention_author=False)
			return

		message = await channel.send(file=imgFile, embed=suggestEmbed)
		check = "\N{WHITE HEAVY CHECK MARK}"
		x = "\N{CROSS MARK}"

		successEmbed = discord.Embed(
			title=f":white_check_mark: Your suggestion has been successfully recorded!",
			description="Check <#865992973204193280>.",
			color=0x77dd77
		)

		await ctx.reply(embed=successEmbed, mention_author=False)

		await message.add_reaction(check)
		await message.add_reaction(x)

	
	@commands.command(pass_context=True)
	@commands.has_permissions(administrator=True)
	async def info(self, ctx, member : discord.Member):
		"""Gets the user's roles"""
		roleList = []
		memberRoles = []
		for role in ctx.guild.roles:
			if role.name == "@everyone":
				pass

			else:
				roleList.append(role.id)

		for roles in member.roles:
			if roles.id in roleList:
				memberRoles.append(roles.id)
			else:
				pass
		memberRoles.reverse()
		
		rolesStr = ""
		for i in memberRoles:
			rolesStr += f"<@&{i}>\n"

		roleEmbed = discord.Embed(
			title=f"{member}",
			description=f"<@{member.id}>"
		)

		roleEmbed.add_field(
			name="Roles",
			value=rolesStr,
			inline=False
		)

		roleEmbed.add_field(
			name="Server Nickname",
			value=member.display_name
		)

		roleEmbed.add_field(
			name="Created On",
			value=member.created_at,			
		)

		roleEmbed.add_field(
			name="Joined Server On",
			value=member.joined_at
		)

		roleEmbed.add_field(
			name="User ID",
			value=member.id
		)

		if member.bot:
			botStr = "Yes"
		elif not member.bot:
			botStr = "No"
		roleEmbed.add_field(
			name="Bot",
			value=botStr
		)

		if member.guild_permissions.administrator is True:
			adminStr = "Yes"
		else:
			adminStr = "No"
		roleEmbed.add_field(
			name="Admin",
			value=adminStr
		)

		roleEmbed.set_thumbnail(
			url=member.avatar_url
		)

		await ctx.send(embed=roleEmbed)
			




def setup(client):
	client.add_cog(Cmds(client))