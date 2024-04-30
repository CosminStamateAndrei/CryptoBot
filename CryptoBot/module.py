import discord

def hasRole(member: discord.Member, roleToAdd: discord.Role):
    roles = member.roles
    for role in roles:
        if role == roleToAdd:
            return True


def isOwner(member: discord.Member):
    roles = member.roles
    for role in roles:
        if role.permissions.value == 2146959359:
            return True
    return False

def isOwnerServer(ctx, member: discord.Member):
    guild = ctx.guild
    if guild.owner == member:
        return True
    return False