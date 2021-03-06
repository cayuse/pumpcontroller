__author__ = 'kutenai'

import os
import json
import re
import MySQLdb
from time import strftime

from DBConnection import *

class DBDitch(DBConnUser):

    def __init__(self,connection):
        super(DBDitch,self).__init__(connection)

        self.setTableNames()

    def setTableNames(self):

        self.ditchLog = "level_log"

    def clearLog(self):
        """
        Just delete all from the current tables.
        """
        curs = self.getCursor()
        curs.execute("delete from %s" % self.ditchLog)
        curs.execute("alter table %s AUTO_INCREMENT=1" % self.compTable)

    def insertLogEntry(self,ditchlvl,sumplvl,ditchin, sumpin, pumpOn, northOn, southOn):

        sql = """
            insert into %s
            (
                timestamp,
                ditchlvl,
                sumplvl,
                ditch_inches,
                sump_inches,
                pump_on,
                north_on,
                south_on
            ) values (
                now(), %d, %d, %f, %f, %d, %d, %d
            );

            """ % (self.ditchLog,
                   ditchlvl, sumplvl, ditchin, sumpin, pumpOn, northOn, southOn
                )

        curs = self.getCursor()
        curs.execute(sql)
        self.conn.commit()

def main():

    # Left over.. could put some test code here.
    pass


if __name__ == '__main__':
    main()
