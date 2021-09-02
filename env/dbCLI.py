import DbOperations as dbOps
import argparse

parser = argparse.ArgumentParser(description="Database Methods CLI")
parser.add_argument("op", choices=["create", "delete", "restart"])
args = parser.parse_args()

if args.op == "create":
    dbOps.createDb()
elif args.op == "delete":
    dbOps.deleteDb()
elif args.op == "restart":
    dbOps.restartDb()
