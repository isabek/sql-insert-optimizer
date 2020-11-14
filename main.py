import argparse
import os

import sys

from optimizer import Optimizer


def main():
    parser = argparse.ArgumentParser(description="SQL Insert Optimizer")
    parser.add_argument("-sql", help="Location of the SQL file", required=True)
    parser.add_argument("-batch", help="Batch size", required=False, default=500, type=int)
    args = parser.parse_args()

    sql_file = os.path.join(os.path.dirname(os.path.realpath('__file__')), args.sql)

    if not os.access(sql_file, os.F_OK):
        print("%s file is missing." % sql_file)
        sys.exit()

    if not os.access(sql_file, os.R_OK):
        print("%s file is not readable." % sql_file)
        sys.exit()

    output_sql_dir = os.path.dirname(sql_file)

    optimizer = Optimizer(sql_file=sql_file, output_sql_dir=output_sql_dir, batch=args.batch)
    optimizer.optimize()


if __name__ == "__main__":
    main()
