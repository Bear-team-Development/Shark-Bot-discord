
@bot.slash_command(name="about", description="查看關於我們")
async def about(ctx):
    embed = discord.Embed(title=f"關於 {bot.user.name}")
    embed.add_field(name="開發團隊：", value="Bear-Team")
    embed.add_field(name="項目領導者：", value="<@564344442127908875> (MiniIce)")
    embed.add_field(name="美術：", value="<@564344442127908875> (MiniIce)")
    embed.add_field(name="主程序：", value="<@755861933961511074> (cutebear)")
    embed.add_field(name="版本：", value=f"{__version__}")
    if bot.user.id == 896429030574796831:
        embed.add_field(name="版本頻道：", value="Beta")
    elif bot.user.id == 888278703975579698:
        embed.add_field(name="版本頻道：", value="Stable")
    else:
        embed.add_field(name="版本頻道：", value="Unknown")
    embed.add_field(name="python版本：", value=f"{python_version()}")
    embed.add_field(name="作業系統：", value=f"{platform()}")
    embed.add_field(name="使用伺服器數量：", value=f"{len(bot.guilds)}")

    await ctx.respond(embed=embed)
