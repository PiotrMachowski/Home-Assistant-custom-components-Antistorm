import logging
from dataclasses import dataclass
from typing import Callable

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfTime

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback


from homeassistant.components.sensor import SensorEntity, SensorEntityDescription, DOMAIN as S_DOMAIN
from homeassistant.helpers.typing import StateType

from .const import DOMAIN
from .update_coordinator import AntistormUpdateCoordinator, AntistormData
from .entity import AntistormEntity


_LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class AntistormSensorDescriptionMixin:
    value_fn: Callable[[AntistormData], int]


@dataclass(frozen=True)
class AntistormSensorEntityDescription(SensorEntityDescription, AntistormSensorDescriptionMixin):
    has_entity_name = True


entity_descriptions = [
    AntistormSensorEntityDescription(
        key='storm_probability',
        translation_key='storm_probability',
        icon="mdi:weather-lightning",
        native_unit_of_measurement=' ',
        value_fn=lambda data: data.storm_probability,
    ),
    AntistormSensorEntityDescription(
        key='storm_time',
        translation_key='storm_time',
        icon="mdi:weather-lightning",
        native_unit_of_measurement=UnitOfTime.MINUTES,
        value_fn=lambda data: data.storm_time,
    ),
    AntistormSensorEntityDescription(
        key='precipitation_probability',
        translation_key='precipitation_probability',
        icon="mdi:weather-pouring",
        native_unit_of_measurement=' ',
        value_fn=lambda data: data.precipitation_probability,
    ),
    AntistormSensorEntityDescription(
        key='precipitation_time',
        translation_key='precipitation_time',
        icon="mdi:weather-pouring",
        native_unit_of_measurement=UnitOfTime.MINUTES,
        value_fn=lambda data: data.precipitation_time,
    )
]


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry,
                            async_add_entities: AddEntitiesCallback) -> bool:
    coordinator: AntistormUpdateCoordinator = hass.data[DOMAIN][config_entry.entry_id]
    entities = []
    for entity_description in entity_descriptions:
        entities.append(AntistormSensor(coordinator, config_entry, entity_description))
    async_add_entities(entities)
    return True


class AntistormSensor(AntistormEntity, SensorEntity):
    entity_description: AntistormSensorEntityDescription

    def __init__(self, coordinator: AntistormUpdateCoordinator, config_entry: ConfigEntry,
                 description: AntistormSensorEntityDescription) -> None:
        super().__init__(coordinator, config_entry)
        self.entity_description = description
        self._attr_unique_id = f"{DOMAIN}_{description.key}"
        self.entity_id = f"{S_DOMAIN}.{DOMAIN}_{self.city_id}_{description.key}"

    @property
    def unique_id(self) -> str:
        return f"{super().unique_id}_{self.entity_description.key}"

    @property
    def native_value(self) -> StateType:
        if self.get_data() is None:
            return None
        return self.entity_description.value_fn(self.get_data())
