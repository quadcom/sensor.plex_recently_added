from homeassistant.core import HomeAssistant
from .plex_api import PlexApi

async def setup_client(
    hass: HomeAssistant,
    name: str,
    ssl: bool,
    token: str,
    max: int,
    on_deck: bool,
    sort_by: str,
    host: str,
    port: int,
    section_types: list,
    section_libraries: list,
    exclude_keywords: list,
):
    client = PlexApi(hass, name, ssl, token, max, on_deck, sort_by, host, port, section_types, section_libraries, exclude_keywords)

    await client.update()
    return client