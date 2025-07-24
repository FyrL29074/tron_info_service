from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone


Base = declarative_base()

class WalletInfo(Base):
    __tablename__ = "wallet"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, unique=True, index=True)
    balance = Column(Float)
    bandwidth = Column(Integer)
    energy = Column(Integer)
    timestamp = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
