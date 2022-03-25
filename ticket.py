
@bot.event
async def on_interaction(interactions: discord.Interaction):
    if interactions.is_component():
        if interactions.data["custom_id"] == "delete-ticket":
            await interactions.channel.send("ticket將會在幾秒之後關閉")
            await interactions.channel.delete()
        elif interactions.data["custom_id"] == "create-ticket":

            channel = await interactions.guild.create_text_channel(
                f"ticket-{random.randint(1,9999)}"
            )
            del_button = discord.ui.Button(
                label="delete ticket",
                style=discord.ButtonStyle.danger,
                custom_id="delete-ticket",
                emoji="🗑",
            )
            v = discord.ui.View()
            v.add_item(del_button)
            embed = discord.Embed(
                title="點擊按鈕刪除此ticket",
                color=0x787FDD,
                description=f"{interactions.user.mention} 建立了此ticket",
            )
            await channel.send(embed=embed, view=v)

            await channel.set_permissions(bot.user, view_channel=True)
            await channel.set_permissions(
                interactions.guild.default_role, view_channel=False
            )
            await channel.set_permissions(interactions.user, view_channel=True)

    await bot.process_application_commands(interactions)


@bot.slash_command(name="ticket", description="生成ticket建立按鈕")
async def ticket(ctx):
    # if user is admin
    if not ctx.author.guild_permissions.administrator:
        return await ctx.send("你不是管理員")
    cre_button = discord.ui.Button(
        label="create ticket",
        style=discord.ButtonStyle.green,
        custom_id="create-ticket",
        emoji="🎫",
    )

    v = discord.ui.View()
    v.add_item(cre_button)
    await ctx.respond(embed=discord.Embed(title="點擊按鈕創建ticket"), view=v)

