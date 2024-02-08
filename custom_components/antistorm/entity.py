from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION, CONF_NAME
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .update_coordinator import AntistormUpdateCoordinator
from .connector import AntistormData
from .const import ATTRIBUTION, DEFAULT_NAME, DOMAIN, CONF_CITY_ID, BASE_URL


class AntistormEntity(CoordinatorEntity):

    def __init__(self, coordinator: AntistormUpdateCoordinator, config_entry: ConfigEntry):
        super().__init__(coordinator)
        self.config_entry = config_entry
        self.city_id = config_entry.data[CONF_CITY_ID]

    @property
    def extra_state_attributes(self) -> dict:
        return {ATTR_ATTRIBUTION: ATTRIBUTION}

    def get_data(self) -> AntistormData | None:
        return self.coordinator.data

    def base_name(self) -> str:
        return f"{DEFAULT_NAME} {self.config_entry.data[CONF_NAME]}"

    @property
    def unique_id(self) -> str:
        return f"{DOMAIN}_{self.config_entry.data[CONF_CITY_ID]}"

    @property
    def device_info(self) -> DeviceInfo:
        city_id = self.config_entry.data[CONF_CITY_ID]
        return {
            "identifiers": {(DOMAIN, city_id)},
            "name": self.base_name(),
            "configuration_url": BASE_URL,
        }
