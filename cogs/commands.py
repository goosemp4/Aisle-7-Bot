import discord
from discord.ext import commands
from datetime import date
import json

client = discord.Client()

suggestUrl = "https://cdn.discordapp.com/attachments/865993082297516052/865993157568757760/wrench.png"


class Cmds(commands.Cog):

	def __init__(self, client):
		self.client = client



	@commands.Cog.listener()
	async def on_message(self, message):
		"""Deletes a messaged that contains a blacklisted word"""


		msg = message.content

		blacklist = ["nigger", "fag","faggot","fggt","fagg","faggt","ngger","ngger","n1gger","n1gg3r","nigg3r","ngg3r", "n1ggr","f4g","f4ggot","f4gg0t","f4ggt","fgg0t"]

		try:

			check = blacklist.index(msg)
			await message.delete()
			await message.author.send(":no_entry_sign: You have been detected of saying an innopropriate word. Your message has been deleted; do **NOT** say that.")

		except ValueError:
			pass


	@commands.command()
	async def mverify(self, ctx, member:discord.Member):
		"""Manually verify a member that could not/did not get captcha solved"""

		for i in ctx.author.roles:
			if i.id == 862811341772423190:
				await ctx.channel.purge(limit=1)

				await member.add_roles(member.guild.get_role(862811433662545940))
				await member.add_roles(member.guild.get_role(862813454812971088))
				await member.add_roles(member.guild.get_role(862829754779303956))
				await member.add_roles(member.guild.get_role(862813524870299668))
				await member.remove_roles(member.guild.get_role(871477918369468416))
				
			else:
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

		try:
			await member.send(f"You have been kicked from Aisle #7 for: **{reason}**")
		except discord.Forbidden:
			pass

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

		try:
			await member.send(f"You have been banned from Aisle #7 for: **{reason}**")
		except discord.Forbidden:
			pass

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
			


	@commands.Cog.listener()
	async def on_raw_reaction_add(self, payload):
		"""Detects reactions for react-role"""

		if payload.member.bot is True:
			pass
		
		else:
			with open('cogs/reactrole.json') as rrFile:
				dataStuff = json.load(rrFile)
				for x in dataStuff:
					if x['emoji'] == str(payload.emoji) and x['messageID'] == str(payload.message_id):
	
						role = discord.utils.get(self.client.get_guild(payload.guild_id).roles, id = x['roleID'])

						await payload.member.add_roles(role)


		

	@commands.Cog.listener()
	async def on_raw_reaction_remove(self, payload):
		"""Removes role if user removes reaction"""

		with open('cogs/reactrole.json') as rrFile:
			dataStuff = json.load(rrFile)
			for x in dataStuff:
				if x['emoji'] == str(payload.emoji) and x['messageID'] == str(payload.message_id):

					role = discord.utils.get(self.client.get_guild(payload.guild_id).roles, id = x['roleID'])

					await self.client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)



	@commands.command(pass_context=True)
	@commands.has_permissions(administrator=True)
	async def rr(self, ctx, channel, msgID, emoji, role: discord.Role):
		"""React role"""
		
		channelid = ""
		for i in channel:
			try:
				i = int(i)
				i = str(i)
				channelid += i

			except ValueError or TypeError:
				pass

		await self.client.wait_until_ready()
		channel = self.client.get_channel(int(channelid))
		message = await channel.fetch_message(msgID)
		await message.add_reaction(emoji)

		with open("cogs/reactrole.json") as jfile:
			data = json.load(jfile)

			new_reactrole = {
				'roleName':role.name,
				'roleID':role.id,
				'emoji':emoji,
				'messageID':msgID
			}

			data.append(new_reactrole)
		
		with open("cogs/reactrole.json", "w") as f:
			json.dump(data, f, indent=4)
		
		await ctx.reply("<a:check:871473852465709146> Reaction role successfully added!")




def setup(client):
	client.add_cog(Cmds(client))