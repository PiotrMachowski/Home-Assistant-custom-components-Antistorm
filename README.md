# Antistorm sensor

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

This sensor uses official API to get storm warnings from [*Antistorm*](https://antistorm.eu/). For more precise explanation of parameters visit [*Antistorm.eu*](https://antistorm.eu/deweloperzy.php).

## Configuration options

| Key | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `False` | `Antistorm` | Name of sensor |
| `station_id` | `positive int` | `True` | - | ID of monitored station |
| `monitored_conditions` | `list` | `True` | - | List of conditions to monitor |

### Possible monitored conditions

#### Binary sensor
| Key | Description |
| --- | --- | 
| `storm_alarm` | Status of storm alarm |
| `rain_alarm` | Status of rain alarm |
| `storm_active` | Active storm |

#### Sensor
| Key | Description |
| --- | --- | 
| `storm_probability` | Probability of storm |
| `storm_time` | Estimated time until storm |
| `rain_probability` | Probability of rain |
| `rain_time` | Estimated time until rain |

## Example usage

```
binary_sensor:
  - platform: antistorm
    station_id: 408
    monitored_conditions:
      - 'storm_alarm'
      - 'rain_alarm'
      - 'storm_active'
```

```
sensor:
  - platform: antistorm
    station_id: 408
    monitored_conditions:
      - 'storm_probability'
      - 'storm_time'
      - 'rain_probability'
      - 'rain_time'
```

## Installation

Download [*binary_sensor.py*](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Antistorm/raw/master/custom_components/antistorm/binary_sensor.py), [*sensor.py*](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Antistorm/raw/master/custom_components/antistorm/sensor.py) and [*manifest.json*](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Antistorm/raw/master/custom_components/antistorm/manifest.json) to `config/custom_components/antistorm` directory:
```bash
mkdir -p custom_components/antistorm
cd custom_components/antistorm
wget https://github.com/PiotrMachowski/Home-Assistant-custom-components-Antistorm/raw/master/custom_components/antistorm/binary_sensor.py
wget https://github.com/PiotrMachowski/Home-Assistant-custom-components-Antistorm/raw/master/custom_components/antistorm/sensor.py
wget https://github.com/PiotrMachowski/Home-Assistant-custom-components-Antistorm/raw/master/custom_components/antistorm/manifest.json
```

## FAQ

* **How to get value for `station_id`?**

  To find out `station_id` use widget code generator available at page [*Antistorm.eu*](https://antistorm.eu/deweloperzy.php).

<a href="https://www.buymeacoffee.com/PiotrMachowski" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
