"""Red hat status page integration with home assistant"""

from .const import (
    DOMAIN,
    PLATFORMS,
    ComponentSensorStatus
)

from .api import RedHatStatus
from .coordinator import Coordinator


async def async_setup_entry(hass, entry) -> bool:
    """Set up from a config entry."""
    api = RedHatStatus()
    coordinator = Coordinator(hass, api)

    hass.data[DOMAIN] = {
        'coordinator': coordinator
    }

    await coordinator.async_config_entry_first_refresh()
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass, entry) -> bool:
    hass.data.pop(DOMAIN)
    return True
