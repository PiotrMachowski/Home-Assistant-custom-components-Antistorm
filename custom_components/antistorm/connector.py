import logging
import requests

from .const import API_URL, GET_CITY_URL

_LOGGER = logging.getLogger(__name__)


class AntistormData:
    def __init__(self, m: str, p_b: int, t_b: int, a_b: int, p_o: int, t_o: int, a_o: int, s: int) -> None:
        self.city = m
        self.storm_probability = p_b
        self.storm_time = t_b
        self.storm_alarm = a_b == 1
        self.storm_active = s == 1
        self.precipitation_probability = p_o
        self.precipitation_time = t_o
        self.precipitation_alarm = a_o == 1


class AntistormConnector:
    def __init__(self, city_id: int) -> None:
        self._city_id = city_id

    def get_data(self) -> AntistormData:
        response = requests.get(f"{API_URL}{self._city_id}")
        response.encoding = 'utf-8'
        if response.status_code != 200:
            raise Exception(f"Error ({response.status_code}) getting Antistorm data: {response.text}")
        data = AntistormData(**response.json())
        return data

    @staticmethod
    def get_city_id(city_name: str) -> int | None:
        response = requests.post(GET_CITY_URL, data={"miasto": city_name})
        if response.status_code != 200 or response.text == "-1":
            return None
        return int(response.text)
