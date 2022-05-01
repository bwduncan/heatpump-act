import datetime

from .device_infos import DeviceInfos

# --------------------------------------------------------------------------------
class OctopusGo:
    @staticmethod
    def power_will_be_cheap_for_next_fifteen_minutes(
        calculation_moment: datetime.datetime,
        device_infos: DeviceInfos,
    ) -> bool:
        # Yep, just a boolean on the simple tariff

        return datetime.time(0, 30) < calculation_moment.time() < datetime.time(4, 15)
