from sqlalchemy.engine import Engine

from app.database import Base, engine

def init_db(database_engine: Engine = engine) -> None:
    Base.metadata.create_all(bind=database_engine)

def drop_db(database_engine: Engine = engine) -> None:
    Base.metadata.drop_all(bind=database_engine)

if __name__ == "__main__":
    init_db() # pragma: no cover