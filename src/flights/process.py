import pandas as pd
from tqdm import tqdm

import global_utilities as gu
from global_utilities.log import log

from . import constants as c
from .rapidapi import query_pair


def get_airports_pairs():
    """ Get a set of all airports combinations """

    dbx = gu.dropbox.get_dbx_connector(c.VAR_DROPBOX_TOKEN)
    df_airports = gu.dropbox.read_excel(dbx, c.FILE_AIRPORTS)

    out = set()
    for _, row in df_airports.iterrows():
        out.add((row[c.COL_ORIGIN], row[c.COL_DESTINATION]))
        out.add((row[c.COL_DESTINATION], row[c.COL_ORIGIN]))

    log.info("Airports retrived from dropbox")

    return out


def retrive_all_flights():
    """ Get a dataframe with all flights """

    dfs = []
    for origin, dest in tqdm(get_airports_pairs()):
        df = query_pair(origin, dest)

        if df is not None:
            dfs.append(df)

    if dfs:
        return pd.concat(dfs).reset_index(drop=True)
    else:
        log.error(f"There are no flights")


def main(mdate):

    # Get history
    dbx = gu.dropbox.get_dbx_connector(c.VAR_DROPBOX_TOKEN)
    df_history = gu.dropbox.read_excel(dbx, c.FILE_FLIGHTS)

    # Get new data
    df = retrive_all_flights()

    # Merge data
    log.info("Merging flights history")
    df_out = pd.concat([df_history, df]).drop_duplicates(c.COLS_INDEX)

    # Store data
    gu.dropbox.write_excel(dbx, df, c.FILE_FLIGHTS, index=False)
    log.info("Flights exported to dropbox")


if __name__ == "__main__":
    main()