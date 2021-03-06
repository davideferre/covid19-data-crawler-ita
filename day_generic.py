from datetime import datetime
from influxdb import InfluxDBClient


class DayGeneric:
    """Class representing a single generic day data."""

    _point_struct = None
    _tags_struct = None
    _skip_keys = []
    _tag_keys = []
    _measurement_name = ""
    _influx_host = 'localhost'
    _influx_port = 8086
    _influx_db = 'dati'

    def __init__(self, data):
        today_obj = datetime.strptime(data['data'], '%Y-%m-%dT%H:%M:%S')
        today = today_obj.astimezone().isoformat()
        self._point_struct = {
            "measurement": self._measurement_name,
            "tags": {},
            "fields": {},
            "time": today
        }
        for key in data.keys():
            if key not in self._skip_keys and data[key] is not None:
                if key in self._tag_keys:
                    self._point_struct['tags'][key] = str(data[key])
                else:
                    self._point_struct['fields'][key] = float(data[key])

    def writeData(self):
        client = InfluxDBClient(host=self._influx_host, port=self._influx_port)
        client.switch_database(self._influx_db)
        points = [self._point_struct]
        try:
            result = client.write_points(points)
            client.close()
        except Exception as e:
            print(e)
            result = False
        return result
