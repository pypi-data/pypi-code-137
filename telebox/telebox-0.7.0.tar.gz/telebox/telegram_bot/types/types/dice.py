from dataclasses import dataclass

from telebox.telegram_bot.types.type import Type


@dataclass(unsafe_hash=True)
class Dice(Type):
    emoji: str
    value: int
