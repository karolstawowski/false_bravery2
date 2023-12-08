from config import LEAGUE_OF_LEGENDS_VERSION
from items import get_items_from_api
from ssl import verify_ssl_certificate
from champions import get_champions_from_api
from runes import get_runes_from_api
from summoner_spells import get_summoner_spells_from_api
from discord_bot import run_discord_bot

verify_ssl_certificate()

[legendary_items, boots_items] = get_items_from_api(LEAGUE_OF_LEGENDS_VERSION)
champions = get_champions_from_api(LEAGUE_OF_LEGENDS_VERSION)
summoner_spells = get_summoner_spells_from_api(LEAGUE_OF_LEGENDS_VERSION)
primary_runes, rune_trees = get_runes_from_api(LEAGUE_OF_LEGENDS_VERSION)

run_discord_bot(
    legendary_items, boots_items, champions, summoner_spells, primary_runes, rune_trees
)
