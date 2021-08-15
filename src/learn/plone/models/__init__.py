from sqlalchemy.orm import registry
from sqlalchemy_mixins import AllFeaturesMixin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_mixin
from sqlalchemy.orm import declared_attr
import sqlalchemy as sa

import configparser
import os


class AlembicNotFoundError(Exception):
    pass


class SqlalchemyUrlEmpty(Exception):
    pass


# registry
mapper_registry = registry()
Base = mapper_registry.generate_base()



# Mixin
@declarative_mixin
class BaseMixin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # __table_args__ = {"mysql_engine": "InnoDB"}
    __table_args__ = {'extend_existing': True}
    __mapper_args__ = {"always_refresh": True}
    id = sa.Column(sa.Integer, primary_key=True)


class BaseModel(Base, BaseMixin, AllFeaturesMixin):
    __abstract__ = True


# For using sqlalchemy-mixins
CURRENT_DIR = os.path.dirname(__file__)
alembic_path = os.path.abspath(CURRENT_DIR + "/../alembic.ini")
config = configparser.ConfigParser()
config.read(alembic_path)

if not config:
    raise AlembicNotFoundError("File: [alembic.ini] not found! Please check your file path.")

sqlString = config.get("alembic", "sqlalchemy.url")
if not sqlString:
    raise SqlalchemyUrlEmpty("[alembic] sqlalchemy.url not have value!")

db = create_engine(sqlString, echo=True)
session = sessionmaker(bind=db)

BaseModel.set_session(session())
