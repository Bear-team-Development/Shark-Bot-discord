from discord.commands import Option

@bot.slash_command(description="開啟語音活動（感謝ChinGH#2459提供活動代碼)，僅限電腦版")
async def game(
    ctx,
    channel: Option(VoiceChannel, "頻道", required=True),
    game: Option(
        str,
        "選擇遊戲",
        choices=[
            "youtube",
            "youtube(dev)",
            "西洋棋",
            "西洋棋(dev)",
            "Betrayal.io",
            "撲克之夜",
            "Fishington.io",
            "lettertile",
            "wordsnack",
            "你猜我畫",
            "awkword",
            "spellcast",
            "checkers",
        ],
    ),
):
    code = {
        "youtube": "880218394199220334",
        "youtube(dev)": "880218832743055411",
        "撲克之夜": "755827207812677713",
        "betrayal": "773336526917861400",
        "Fishington.io": "814288819477020702",
        "西洋棋": "832012774040141894",
        "西洋棋(dev)": "832012586023256104",
        "lettertile": "879863686565621790",
        "wordsnack": "879863976006127627",
        "你猜我畫": "878067389634314250",
        "awkword": "879863881349087252",
        "spellcast": "852509694341283871",
        "checkers": "832013003968348200",
        "puttparty": "763133495793942528",
    }
    invite = await channel.create_activity_invite(
        int(code[game]), max_age=3600, max_uses=20
    )
    await ctx.respond(f"[點連結加入]({invite})")
