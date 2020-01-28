from datetime import date

import luigi

from global_utilities.luigi import StandardTask
from global_utilities.log import log


class MoneyLoverTask(StandardTask):
    module = "money_lover"
    priority = 80


class FlightsTask(StandardTask):
    module = "flights"
    priority = 50


class DoAllTask(luigi.WrapperTask):
    mdate = luigi.DateParameter(default=date.today())

    def requires(self):
        yield MoneyLoverTask(self.mdate)
        yield FlightsTask(self.mdate)


if __name__ == "__main__":

    log.info("Starting vtasks")
    luigi.build([DoAllTask()])

    log.info("End of vtasks")
