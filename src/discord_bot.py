import discord

from champions import randomize_champion
from config import LEAGUE_OF_LEGENDS_VERSION
from items import randomize_boots, randomize_legendary_items
from runes import randomize_primary_rune, randomize_rune_tree
from summoner_spells import randomize_summoner_spells


def get_bot_password():
    return open("bot_password.txt", "r").read()


RUN_COMMAND_KEYWORD = "!aramki"


def run_discord_bot(
    legendary_items, boots_items, champions, summoner_spells, primary_runes, rune_trees
):
    client = discord.Client()
    password = get_bot_password()

    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.mention_everyone:
            return

        if client.user.mentioned_in(message):
            embed = discord.Embed(title="Oxygen's Bot Help")
            embed.add_field(
                name="Available commands:",
                value=f"{RUN_COMMAND_KEYWORD} - generate random stuff",
            )
            embed.set_footer(text="https://github.com/karolstawowski/false_bravery")
            await message.channel.send(embed=embed)

    client.run(password)
