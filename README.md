[![HACS Default][hacs_shield]][hacs]
[![GitHub Latest Release][releases_shield]][latest_release]
[![GitHub All Releases][downloads_total_shield]][releases]
[![Buy me a coffee][buy_me_a_coffee_shield]][buy_me_a_coffee]
[![PayPal.Me][paypal_me_shield]][paypal_me]


[hacs_shield]: https://img.shields.io/static/v1.svg?label=HACS&message=Default&style=popout&color=green&labelColor=41bdf5&logo=HomeAssistantCommunityStore&logoColor=white
[hacs]: https://hacs.xyz/docs/default_repositories

[latest_release]: https://github.com/PiotrMachowski/Home-Assistant-custom-components-Antistorm/releases/latest
[releases_shield]: https://img.shields.io/github/release/PiotrMachowski/Home-Assistant-custom-components-Antistorm.svg?style=popout

[releases]: https://github.com/PiotrMachowski/Home-Assistant-custom-components-Antistorm/releases
[downloads_total_shield]: https://img.shields.io/github/downloads/PiotrMachowski/Home-Assistant-custom-components-Antistorm/total

[buy_me_a_coffee_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy_me_a_coffee]: https://www.buymeacoffee.com/PiotrMachowski

[paypal_me_shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&logo=paypal
[paypal_me]: https://paypal.me/PiMachowski


# Antistorm sensor

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

### Using [HACS](https://hacs.xyz/) (recommended)

This integration can be installed using HACS.
To do it search for `Antistorm` in *Integrations* section.

### Manual

To install this integration manually you have to download [*antistorm.zip*](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Antistorm/releases/latest/download/antistorm.zip) extract its contents to `config/custom_components/antistorm` directory:
```bash
mkdir -p custom_components/antistorm
cd custom_components/antistorm
wget https://github.com/PiotrMachowski/Home-Assistant-custom-components-Antistorm/releases/latest/download/antistorm.zip
unzip antistorm.zip
rm antistorm.zip
```


## FAQ

* **How to get value for `station_id`?**

  To find out `station_id` use widget code generator available at page [*Antistorm.eu*](https://antistorm.eu/deweloperzy.php).

<a href="https://www.buymeacoffee.com/PiotrMachowski" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
<a href="https://paypal.me/PiMachowski" target="_blank"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_37x23.jpg" border="0" alt="PayPal Logo" style="height: auto !important;width: auto !important;"></a>
