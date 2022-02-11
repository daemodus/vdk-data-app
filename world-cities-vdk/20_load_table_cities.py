# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import logging

import pandas as pd
from vdk.api.job_input import IJobInput

log = logging.getLogger(__name__)


def run(job_input: IJobInput):
    """
    Function named `run` is required in order for a python script to be recognized as a Data Job Python step and executed.

    VDK provides to every python step an object - job_input - that has methods for:

    * executing queries to OLAP Database;
    * ingesting data into a database;
    * processing data into a database.
    See IJobInput documentation for more details.
    """
    log.info(f"Starting job step {__name__}")
    df = pd.read_csv('world-cities-vdk/source/worldcities.csv')

    df_dict = df.to_dict(orient='records')
    for row in range(0, len(df_dict)):
        job_input.send_object_for_ingestion(payload=df_dict[row],
                                            destination_table="cities")
