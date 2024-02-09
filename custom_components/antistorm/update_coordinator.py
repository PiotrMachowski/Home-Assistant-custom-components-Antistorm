import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .connector import AntistormConnector, AntistormData
from .const import DOMAIN, DEFAULT_UPDATE_INTERVAL

_LOGGER = logging.getLogger(__name__)


class AntistormUpdateCoordinator(DataUpdateCoordinator[AntistormData]):

    def __init__(self, hass: HomeAssistant, city_id: int) -> None:
        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=DEFAULT_UPDATE_INTERVAL,
                         update_method=self.update_method)
        self.connector = AntistormConnector(city_id)

    async def update_method(self) -> AntistormData:
        return await self.hass.async_add_executor_job(self._update)

    def _update(self) -> AntistormData:
        return self.connector.get_data()
