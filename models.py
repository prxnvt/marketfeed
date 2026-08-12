from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass(frozen = True)
class Bar:
    symbol: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int
    def __post_init__(self) -> None:
        if not self.symbol.strip():
            raise ValueError("symbol is empty")
        if self.timestamp.tzinfo is None:
            raise ValueError("timestamp is not timezone-aware")
        if self.timestamp.utcoffset() != timedelta(0):
            raise ValueError("timestamp is not UTC")
        if self.open <= 0.0:
            raise ValueError("open is negative")
        if self.high <= 0.0:
            raise ValueError("high is negative")
        if self.low <= 0.0:
            raise ValueError("low is negative")
        if self.close <= 0.0:
            raise ValueError("close is negative")
        if self.volume < 0:
            raise ValueError("volume is negative")
        if self.high < self.low:
            raise ValueError("high is less than low")
        if self.high < self.open:
            raise ValueError("high is less than open")
        if self.high < self.close:
            raise  ValueError("high is less than close")
        if self.low > self.close:
            raise ValueError("low is higher than close")
        if self.low > self.open:
            raise ValueError("low is higher than open")

@dataclass(frozen = True)
class Quote:
    symbol: str
    timestamp: datetime
    bid: float
    ask: float
    bid_size: int
    ask_size: int
    def __post_init__(self) -> None:
        if not self.symbol.strip():
            raise ValueError("symbol is empty")
        if self.timestamp.tzinfo is None:
            raise ValueError("timestamp is not timezone-aware")
        if self.timestamp.utcoffset() != timedelta(0):
            raise ValueError("timestamp is not UTC")
        if self.bid <= 0.0:
            raise ValueError("bid is negative")
        if self.ask <= 0.0:
            raise ValueError("ask is negative")
        if self.bid_size < 0:
            raise ValueError("bid_size is negative")
        if self.ask_size < 0:
            raise ValueError("ask_size is negative")

        if self.ask < self.bid:
            raise ValueError("ask is less than bid")