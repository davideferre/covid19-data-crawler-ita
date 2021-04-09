from day_generic import DayGeneric


class DayRegion(DayGeneric):
    """Class representing a single region day data."""

    def __init__(self, data):
        self._measurement_name = "region"
        self._skip_keys = ["note", "note_casi", "note_test", "data",
                           "casi_da_sospetto_diagnostico", "casi_da_screening", "codice_nuts_1", "codice_nuts_2"]
        self._tag_keys = ["stato", "codice_regione", "denominazione_regione", "lat", "long"]
        super().__init__(data)

    def writeData(self):
        return super().writeData()
