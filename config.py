# config.py

import os
from dataclasses import dataclass

@dataclass
class Config:
    # API
    BLOCKCYPHER_BASE_URL: str = os.getenv(
        "BLOCKCYPHER_BASE_URL",
        "https://api.blockcypher.com/v1/eth/main"
    )

    # Optional API key (если захочешь расширять)
    API_KEY: str = os.getenv("API_KEY", "")

    # App settings
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", 10))
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"


# instance (чтобы удобно импортить)
config = Config()
