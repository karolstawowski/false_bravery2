from config import LEAGUE_OF_LEGENDS_VERSION
from items import get_items_from_api
from ssl import verify_ssl_certificate

verify_ssl_certificate()

[legendary_items, boots_items] = get_items_from_api(LEAGUE_OF_LEGENDS_VERSION)
