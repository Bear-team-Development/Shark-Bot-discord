
@bot.slash_command(name="help", description="查看指令列表")
async def help(ctx):
    embed = discord.Embed(title="指令", description="指令列表", color=0x00FF00)

    for i in bot.application_commands:
        if i.name not in ["reload", "server", "whois"]:

            embed.add_field(
                name=i.name,
                value=f"{i.description if i.description else '無說明'}",
                inline=False,
            )
    # add footer
    embed.set_footer(text="想要更多？點https://forms.gle/gZ5YKcf2QK3hZv8g9來建議")
    await ctx.respond(embed=embed)
