from datetime import timedelta
import logging

import async_timeout

from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed
)

_LOGGER = logging.getLogger(__name__)


class Coordinator(DataUpdateCoordinator):
    """Red Hat status update coordinator"""

    def __init__(self, hass, api):
        super().__init__(
            hass,
            _LOGGER,
            name="Red Hat status coordinator",
            update_interval=timedelta(seconds=30)
        )
        self.api = api

    async def _async_update_data(self):
        async with async_timeout.timeout(10):
            summary = await self.api.summary()
            data = {
                'components': {}
            }
            for component in summary['components']:
                data['components'][component['id']] = component

            return data
