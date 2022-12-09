"""Red Hat status API"""

import aiohttp

_COMPONENTS_API = "https://status.redhat.com/api/v2/summary.json"


class RedHatStatus:
    async def summary(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(_COMPONENTS_API) as response:
                return await response.json()
