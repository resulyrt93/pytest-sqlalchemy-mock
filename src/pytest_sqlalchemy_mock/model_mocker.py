from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import (
        List,
        Tuple,
    )

    from sqlalchemy import Table
    from sqlalchemy.orm import Session

    MOCK_CONFIG_TYPE = List[Tuple[str, List]]


class ModelMocker:
    _base = None
    _mock_config: MOCK_CONFIG_TYPE = None

    def __init__(self, session: Session, base, mock_config: MOCK_CONFIG_TYPE):
        self._session: Session = session
        self._base = base
        self._mock_config = mock_config

    def get_table_by_name(self, table_name: str) -> Table:
        return self._base.metadata.tables.get(table_name)

    def create_all(self):
        for model_config in self._mock_config:
            table_name, data = model_config
            table = self.get_table_by_name(table_name)

            if table is not None:
                for datum in data:
                    instance = table.insert().values(**datum)
                    self._session.execute(instance)
