from enum import Enum

from homeassistant.const import Platform

DOMAIN = "com_redhat_status"
DEFAULT_NAME = "Red Hat Status"
PLATFORMS = [Platform.SENSOR]


class StatusIndicatorSensor(Enum):
    NONE = "none"
    MINOR = "minor"
    MAJOR = "major"
    CRITICAL = "critical"
    MAINTENANCE = "maintenance"


class ComponentSensorStatus(Enum):
    OPERATIONAL = "operational"
    UNDER_MAINTENANCE = "under_maintenance"
    PARTIAL_OUTAGE = "partial_outage"
    MAJOR_OUTAGE = "major_outage"
