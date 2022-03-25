
@bot.slash_command(description="查看你所在伺服器的資料")
async def server_info(ctx):
    online = []
    offline = []
    ilde = []
    dnd = []
    for member in ctx.guild.members:
        if str(member.status) == "online":
            online.append(member)
        elif str(member.status) == "offline":
            offline.append(member)
        elif str(member.status) == "idle":
            ilde.append(member)
        else:
            dnd.append(member)
    embed = discord.Embed(title=f"{ctx.guild.name}伺服器資料", color=0x787FDD)
    try:
        embed.set_thumbnail(url=str(ctx.guild.icon_url))
    except:
        pass
    embed.add_field(name="伺服器名稱:", value=ctx.guild.name)
    embed.add_field(name="伺服器擁有者:", value=ctx.guild.owner.name)
    embed.add_field(
        name="伺服器成員狀態:",
        value=f"在線:{len(online)}人\n請勿打擾:{len(dnd)}人\n閒置:{len(ilde)}人\n離線:{len(offline)}人",
    )
    embed.add_field(name="伺服器地區:", value=ctx.guild.region)
    embed.add_field(name="伺服器表情數目:", value=len(ctx.guild.emojis))
    embed.add_field(name="伺服器總人數:", value=ctx.guild.member_count)
    embed.add_field(name="伺服器ID:", value=ctx.guild.id)

    await ctx.respond(embed=embed)
