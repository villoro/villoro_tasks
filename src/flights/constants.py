"""
    Constants and config vars
"""

PATH_VFLIGHTS = "/Aplicaciones/vflights"
PATH_HISTORY = f"{PATH_VFLIGHTS}/history"

FILE_AIRPORTS = f"{PATH_VFLIGHTS}/airports.xlsx"
FILE_FLIGHTS = f"{PATH_VFLIGHTS}/data.xlsx"
FILE_FLIGHTS_DAY = PATH_HISTORY + "/{date:%Y_%m}/{date:%Y_%m_%d}.parquet"

COL_PRICE = "Price"
COL_DIRECT = "Direct"
COL_QUOTE_DATE = "Quote_date"
COL_DATE = "Date"
COL_CARRIER = "Carrier"
COL_ORIGIN = "Origin"
COL_DESTINATION = "Destination"
COL_INSTERTED = "Inserted"

COL_RENAMES = {"MinPrice": COL_PRICE, "QuoteDateTime": COL_QUOTE_DATE, "DepartureDate": COL_DATE}

COLS_INDEX = [
    COL_DATE,
    COL_QUOTE_DATE,
    COL_ORIGIN,
    COL_DESTINATION,
    COL_DIRECT,
    COL_CARRIER,
    COL_PRICE,
]
