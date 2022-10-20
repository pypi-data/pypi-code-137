import pandas as pd
import talib

from declafe import ColLike
from declafe.feature_gen.quadri.QuadriFeature import QuadriFeature

__all__ = ["CDLIDENTICAL3CROWSFeature"]


class CDLIDENTICAL3CROWSFeature(QuadriFeature):

  def __init__(
      self,
      open: ColLike,
      high: ColLike,
      low: ColLike,
      close: ColLike,
  ):
    super().__init__(open, high, low, close)

  def quadrigen(self, col1: pd.Series, col2: pd.Series, col3: pd.Series,
                col4: pd.Series) -> pd.Series:
    return talib.CDLIDENTICAL3CROWS(
        col1,
        col2,
        col3,
        col4,
    )

  def _feature_name(self) -> str:
    return f"CDLIDENTICAL3CROWS_{self.col1}_{self.col2}_{self.col3}_{self.col4}"
