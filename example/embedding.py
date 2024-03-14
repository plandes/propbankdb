#!/usr/bin/env python


def main():
    from zensols.propbankdb import Roleset, Database, ApplicationFactory
    db: Database = ApplicationFactory.get_database()
    rs: Roleset = db.roleset_stash['see.01']
    # print out the rule set, the number of roles it has, and embedding shape
    print(rs, len(rs.roles), rs.embedding.shape)


if (__name__ == '__main__'):
    main()
