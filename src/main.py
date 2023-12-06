from config import LEAGUE_OF_LEGENDS_VERSION
from items import get_items_from_api
from ssl import verify_ssl_certificate
from champions import get_champions_from_api

verify_ssl_certificate()

[legendary_items, boots_items] = get_items_from_api(LEAGUE_OF_LEGENDS_VERSION)
champions = get_champions_from_api(LEAGUE_OF_LEGENDS_VERSION)
