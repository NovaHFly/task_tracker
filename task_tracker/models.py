from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum
from typing import Any, Final, Self, TypedDict


class _TaskDict(TypedDict):
    id: int
    description: str
    status: str
    createdAt: str
    updatedAt: str


class StatusEnum(StrEnum):
    """Enum for possible task statuses."""

    TO_DO = 'todo'
    IN_PROGRESS = 'in-progress'
    DONE = 'done'


@dataclass
class Task:
    """Some task to do."""

    id: Final[int]
    description: str
    status: StatusEnum = field(default=StatusEnum.TO_DO)
    createdAt: Final[datetime] = field(default_factory=datetime.now)
    updatedAt: datetime = field(default_factory=datetime.now)

    def __setattr__(self, name: str, value: Any) -> None:
        if name in ('description', 'status'):
            self.updatedAt = datetime.now()
        super().__setattr__(name, value)

    def to_dict(self) -> _TaskDict:  # noqa: D102
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status.name,
            'createdAt': self.createdAt.isoformat(),
            'updatedAt': self.updatedAt.isoformat(),
        }

    @classmethod
    def from_dict(cls, dict_: _TaskDict) -> Self:  # noqa: D102
        try:
            return cls(
                **{
                    'id': dict_['id'],
                    'description': dict_['description'],
                    'status': getattr(StatusEnum, dict_['status']),
                    'createdAt': datetime.fromisoformat(dict_['createdAt']),
                    'updatedAt': datetime.fromisoformat(dict_['updatedAt']),
                },
            )
        except (TypeError, ValueError, KeyError, AttributeError):
            raise ValueError(
                'Invalid json dict format or data types for'
                f' Task dataclass: {dict_}'
            )
