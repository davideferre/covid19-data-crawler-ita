from day_generic import DayGeneric


class DayNation(DayGeneric):
    """Class representing a single nation day data."""

    def __init__(self, data):
        self._measurement_name = "nation"
        self._skip_keys = ["note", "note_casi", "note_test", "data",
                           "casi_da_sospetto_diagnostico", "casi_da_screening"]
        self._tag_keys = ["stato"]
        super().__init__(data)

    def writeData(self):
        return super().writeData()
