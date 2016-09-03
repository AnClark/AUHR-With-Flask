from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
member = Table('member', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('Name', VARCHAR(length=64)),
    Column('Gender', VARCHAR(length=64)),
    Column('Mobile', VARCHAR(length=64)),
    Column('QQ', VARCHAR(length=64)),
    Column('Birthday', DATE),
    Column('Grade', VARCHAR(length=64)),
    Column('Faculty', VARCHAR(length=64)),
    Column('Class', VARCHAR(length=64)),
    Column('DormBuild', VARCHAR(length=64)),
    Column('Department', VARCHAR(length=64)),
    Column('GroupInDepart', VARCHAR(length=64)),
    Column('Occupation', VARCHAR(length=64)),
    Column('AUID', VARCHAR(length=64)),
    Column('ArrivalTime', DATE),
)

Admin = Table('Admin', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=64)),
    Column('nickname', String(length=80)),
    Column('password', String(length=1024)),
    Column('isPremiumUser', Boolean),
)

Member = Table('Member', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('Name', String(length=64)),
    Column('Gender', String(length=64)),
    Column('Mobile', String(length=64)),
    Column('QQ', String(length=64)),
    Column('Birthday', Date),
    Column('Grade', String(length=64)),
    Column('Faculty', String(length=64)),
    Column('Class', String(length=64)),
    Column('DormBuild', String(length=64)),
    Column('Department', String(length=64)),
    Column('GroupInDepart', String(length=64)),
    Column('Occupation', String(length=64)),
    Column('AUID', String(length=64)),
    Column('ArrivalTime', Date),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['member'].drop()
    post_meta.tables['Admin'].create()
    post_meta.tables['Member'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['member'].create()
    post_meta.tables['Admin'].drop()
    post_meta.tables['Member'].drop()
