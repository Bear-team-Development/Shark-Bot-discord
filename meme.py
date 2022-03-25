
@bot.slash_command(description="meme")
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://memes.tw/wtf/api") as resp:
            data = random.choice(await resp.json())
            embed = discord.Embed(title=data["title"], url=data["url"])

            embed.set_image(url=data["src"])
    await ctx.respond(embed=embed)
