## Gemeente-deler

### API

#### `/datasets`

Return available datasets with metadata. Metadata is just the name right now, but may contain formatting hints etcetera later.

    GET /api/datasets

Response

    [
      {
          "id": "count_2014",
          "name": "Bevolking 2014"
      },
      {
          "id": "count_2015",
          "name": "Bevolking 2015"
      },

      ...

#### `/api/gemeentes`

Returns all available gemeentes.

    GET /api/gemeentes

Response

    {
      "results": [
        {
            "id": 0,
            "name": "Aa en Hunze"
        },
        {
            "id": 1,
            "name": "Aalburg"
        },

     ...

#### `/api/similar`

Returns similar gemeentes based on a target and given categories.

    POST /api/similar

    {
    	"gemeente_id": 9,
    	"categories": ["aantal_verdachten"]
    }

Response

    {
      "results": {
        "113": {
            "aantal_verdachten": 2150.0,
            "count_2014": 199326.5,
            "count_2015": 200644.0,
            "regio": "Groningen (gemeente)",
            "toename_bevolking": 0.0066097584,
            "uitgaven_ov": 149000.0
        },
        "18": {
            "aantal_verdachten": 2110.0,
            "count_2014": 151558.0,
            "count_2015": 153055.5,
            "regio": "Arnhem",

    ...
