from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Tuple

    from sqlalchemy.orm import Session

    MOCK_CONFIG_TYPE = List[Tuple[str, List]]


class ModelMocker:
    _base = None
    _mock_config: MOCK_CONFIG_TYPE = None

    def __init__(self, session: Session, base, mock_config: MOCK_CONFIG_TYPE):
        self._session: Session = session
        self._base = base
        self._mock_config = mock_config

    def get_model_class_with_table_name(self, table_name: str):
        for mapper in self._base.registry.mappers:
            cls = mapper.class_
            if cls.__tablename__ == table_name:
                return cls

    def create_all(self):
        for model_config in self._mock_config:
            table_name, data = model_config
            model_class = self.get_model_class_with_table_name(table_name)
            if model_class:
                for datum in data:
                    instance = model_class(**datum)
                    self._session.add(instance)
        self._session.commit()
