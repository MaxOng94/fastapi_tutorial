# =================================
# standard imports
from pathlib import Path

import yaml

# declarative is the base class that every sub class is doing to inherit from
# =================================
env_path = (Path(__file__) / ".." / "env.yaml").resolve()

parameter_dict = {}
with open(env_path) as f:
    docs = yaml.load_all(f, Loader=yaml.FullLoader)
    for doc in docs:
        for k, v in doc.items():
            parameter_dict[k] = v

# engine = create_engine(DATABASE_URL)
# sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# Base = declarative_base()

# def get_db():
#     db = sessionlocal()
#     try:
#         yield db
#     except:
#         db.close()


class Settings:
    # add type hints
    # PROJECT_NAME:str must be str type, will give error if
    # incompatible type
    PROJECT_NAME: str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"
    POSTGRES_USER: str = parameter_dict["POSTGRES_USER"]
    POSTGRES_PWD: str = parameter_dict["POSTGRES_PWD"]
    POSTGRES_DB: str = parameter_dict["POSTGRES_DB"]
    POSTGRES_HOST: str = parameter_dict["POSTGRES_HOST"]
    POSTGRES_PORT: str = parameter_dict["POSTGRES_PORT"]
    DB_CONNECTION_STRING: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PWD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
