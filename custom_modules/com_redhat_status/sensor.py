from homeassistant.core import callback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity
)
from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity
)

from .const import (
    ComponentSensorStatus,
    DOMAIN
)


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN]['coordinator']

    async_add_entities(
        StatusComponentSensor(
            coordinator,
            coordinator.data['components'][component_id]
        ) for _idx, component_id in enumerate(coordinator.data['components'])
    )


class StatusComponentSensor(CoordinatorEntity, SensorEntity):

    def __init__(self, coordinator, component):
        super().__init__(coordinator)
        self.component = component

    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            identifiers={
                (DOMAIN, self.unique_id)
            },
            name=self.component["name"],
            manufacturer="Red Hat",
            entry_type=DeviceEntryType.SERVICE,
            via_device=(DOMAIN, self.component["group_id"]) if self.component["group_id"] else None,
        )

    @property
    def device_class(self):
        return "enum" # SensorDeviceClass.ENUM

    @property
    def options(self):
        options = [status.value for status in ComponentSensorStatus]
        return options

    @property
    def name(self):
        return self.get_name(self.component)

    @property
    def unique_id(self):
        return self.component['id']

    @property
    def native_value(self):
        return self.component['status']

    def get_name(self, component):
        components = self.coordinator.data['components']
        if component['group_id'] and component['group_id'] in components:
            return self.get_name(components[component['group_id']]) + ' > ' + component['name']
        return component['name']

    @callback
    def _handle_coordinator_update(self) -> None:
        component = self.coordinator.data['components'][self.component['id']]
        self.component = component
        self.async_write_ha_state()
