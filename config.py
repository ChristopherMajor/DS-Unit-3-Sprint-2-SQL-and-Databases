"""configuration settings and environment variables defined here
"""

import toml
import __main__
from pathlib import Path
from typing import TypeVar

ConfigurationObject = TypeVar("ConfigurationObject")

_cfg = toml.load("env.toml")

# Using classes to store our configuration settings
class Config:
    # nifty thing learned to me by an OG
    BASE_DIR = str(Path(__main__.__file__))


class Postgres(Config):

    PG_CFG = _cfg["postgres"]["credentials"]
    TABLE_NAME = _cfg["postgres"]["exampleTable"]["name"]
    SCHEMA = _cfg["postgres"]["exampleTable"]["schema"]


class SqLite(Config):
    PATH = _cfg["sqlite3"]["path"]


# Typehinting once considered extra razzle for your dazzle, now seems
# you get shunned for not incorporating it into your code
def load_config(context: str = None) -> ConfigurationObject:
    """Loads the specificed config class
    
    Keyword Arguments:
        context {str} -- The config requested either "postgres" "sqlite"
        or "base"
        (default: {None})
    
    Returns:
        ConfigurationObject -- class with config / env as attributes
    """

    available = {"base": Config(), "postgres": Postgres(), "sqlite": SqLite()}

    if available.keys().__contains__(context):
        return available[context]
    else:
        raise (ValueError, f"{context} not a valid context")
