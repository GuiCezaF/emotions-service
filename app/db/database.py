from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings import envs

DATABASE_URL = envs("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    pool_size=10,         # número máximo de conexões persistentes
    max_overflow=20,      # número máximo de conexões extras que podem ser criadas além do pool
    pool_timeout=30,      # tempo de espera para pegar uma conexão
    pool_recycle=1800,    # recicla a conexão após X segundos
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
