from discord.commands import Option

@bot.slash_command(name="math", description="算數學(2*2=4)")
async def math(ctx, query=Option(str, "問題", required=True, default=None)):
    res = client.query(query)
    embed = discord.Embed(title=next(res.results).text)
    for i in wolframalpha.Image(res)["pod"]:
        if i["@id"] == "NumberLine":
            embed.set_thumbnail(url=i["subpod"]["img"]["@src"])
            break
    embed.set_footer(text="power by wolframalpha")
    await ctx.respond(embed=embed)
