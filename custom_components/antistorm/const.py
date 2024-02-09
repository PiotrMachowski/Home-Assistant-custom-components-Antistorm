from typing import Final
from datetime import timedelta

from homeassistant.const import Platform

DOMAIN: Final = "antistorm"
DEFAULT_NAME: Final = "Antistorm"
DEFAULT_UPDATE_INTERVAL: Final = timedelta(minutes=5)
BASE_URL: Final = 'https://antistorm.eu'
API_URL: Final = f"{BASE_URL}/webservice.php?id="
GET_CITY_URL: Final = f"{BASE_URL}/api-v1/szukaj-miasta.php"

ATTRIBUTION = 'Information provided by Antistorm.eu.'

PLATFORMS = [
    Platform.BINARY_SENSOR,
    Platform.SENSOR,
]

CONF_CITY_ID = "city_id"
CONF_CITY_NAME = "city_name"
