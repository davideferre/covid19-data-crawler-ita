from generic_day import GenericDay


class ProvinceDay(GenericDay):
    """Class representing a single province day data."""

    def __init__(self, data):
        self._measurement_name = "province"
        self._skip_keys = ["note", "data", "codice_nuts_1",
                           "codice_nuts_2", "codice_nuts_3"]
        self._tag_keys = ["stato", "codice_regione", "denominazione_regione",
                          "codice_provincia", "denominazione_provincia", "sigla_provincia", "lat", "long"]
        super().__init__(data)

    def writeData(self):
        return super().writeData()
