import logging
from dataclasses import dataclass
from typing import Callable

from homeassistant.config_entries import ConfigEntry

from homeassistant.core import HomeAssistant
from homeassistant.components.binary_sensor import BinarySensorDeviceClass, BinarySensorEntityDescription, DOMAIN as BS_DOMAIN
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .update_coordinator import AntistormUpdateCoordinator, AntistormData
from .entity import AntistormEntity

_LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class AntistormBinarySensorDescriptionMixin:
    value_fn: Callable[[AntistormData], bool]


@dataclass(frozen=True)
class AntistormBinarySensorEntityDescription(BinarySensorEntityDescription, AntistormBinarySensorDescriptionMixin):
    device_class = BinarySensorDeviceClass.SAFETY
    has_entity_name = True


entity_descriptions = [
    AntistormBinarySensorEntityDescription(
        key='storm_alarm',
        translation_key='storm_alarm',
        icon="mdi:weather-lightning",
        value_fn=lambda data: data.storm_alarm,
    ),
    AntistormBinarySensorEntityDescription(
        key='rain_alarm',
        translation_key='rain_alarm',
        icon="mdi:weather-pouring",
        value_fn=lambda data: data.precipitation_alarm,
    ),
    AntistormBinarySensorEntityDescription(
        key='storm_active',
        translation_key='storm_active',
        icon="mdi:weather-lightning-rainy",
        value_fn=lambda data: data.storm_active,
    ),
]


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry,
                            async_add_entities: AddEntitiesCallback) -> bool:
    coordinator: AntistormUpdateCoordinator = hass.data[DOMAIN][config_entry.entry_id]
    entities = []
    for entity_description in entity_descriptions:
        entities.append(AntistormBinarySensor(coordinator, config_entry, entity_description))
    async_add_entities(entities)
    return True


class AntistormBinarySensor(AntistormEntity, BinarySensorEntity):
    entity_description: AntistormBinarySensorEntityDescription

    def __init__(self, coordinator: AntistormUpdateCoordinator, config_entry: ConfigEntry,
                 description: AntistormBinarySensorEntityDescription) -> None:
        super().__init__(coordinator, config_entry)
        self.entity_description = description
        self._attr_unique_id = f"{DOMAIN}_{description.key}"
        self.entity_id = f"{BS_DOMAIN}.{DOMAIN}_{self.city_id}_{description.key}"

    @property
    def is_on(self) -> bool | None:
        if self.get_data() is None:
            return None
        return self.entity_description.value_fn(self.get_data())

    @property
    def unique_id(self) -> str:
        return f"{super().unique_id}_{self.entity_description.key}"
