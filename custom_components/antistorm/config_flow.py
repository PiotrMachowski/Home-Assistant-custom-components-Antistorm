"""Config flow to configure Antistorm integration."""

import logging

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from homeassistant.data_entry_flow import FlowResult

from .connector import AntistormConnector
from .const import CONF_CITY_ID, CONF_CITY_NAME, DOMAIN

_LOGGER = logging.getLogger(__name__)


class AntistormFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def get_city_details(self, city_name: str) -> tuple[int, str] | None:
        city_id = await self.hass.async_add_executor_job(AntistormConnector.get_city_id, city_name)
        if city_id is None:
            return None
        city_name = (await self.hass.async_add_executor_job(lambda: AntistormConnector(city_id).get_data())).city
        return city_id, city_name

    async def async_step_user(self, user_input=None) -> FlowResult:
        errors = {}
        usr_city_name = ""
        if user_input is not None:
            usr_city_name = user_input[CONF_CITY_NAME].strip()
            details = await self.get_city_details(usr_city_name)
            if details is not None:
                city_id = details[0]
                city_name = details[1]
                return self.async_create_entry(
                    title=city_name,
                    data={
                        CONF_CITY_ID: city_id,
                        CONF_NAME: city_name
                    },
                )
            else:
                errors[CONF_CITY_NAME] = "city_not_found"
        schema = vol.Schema({
            vol.Required(CONF_CITY_NAME, default=usr_city_name): str,
        })
        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
