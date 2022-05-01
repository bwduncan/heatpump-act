import datetime
import os
from typing import Optional

from .device_infos import DeviceInfos
from .last_time_stamp import LastTimeStamp


class StateChange:
    @staticmethod
    def last_state_change():
        observations_file = os.path.join("/", "state", "observations", "values.txt")
        with open(observations_file, encoding="utf-8") as observations:
            lines = observations.readlines()
            column_index = lines[0].split("\t").index("OperationMode")
            latest_value = lines[-1].split("\t")[column_index]
            for line in reversed(lines):
                parts = line.split("\t")
                previous_value = parts[column_index]
                if previous_value != latest_value:
                    return datetime.datetime.strptime(parts[0][:19], "%Y-%m-%dT%H:%M:%S")
        raise Exception(f"Unable to find a change from {latest_value}")

    @staticmethod
    def last_heating(device_infos: DeviceInfos) -> Optional[datetime.datetime]:

        for device_info in reversed(device_infos):
            if device_info.get("HeatPumpFrequency"):
                if "LastTimeStamp" in device_info:
                    return LastTimeStamp.last_time_stamp_in_utc(device_info)

        return None
