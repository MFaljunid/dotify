import pandas as pd
from sqlalchemy.sql import func

from dotify.database import session
from dotify.models import TopSong


class RatingsMatrix:

    def __init__(self, n_top_songs=1000000):
        self.n_top_songs = n_top_songs
        self.R_ui = self._build_R_ui()

    def _build_R_ui(self):
        top_songs = session.query(
            TopSong.country_id,
            TopSong.song_id,
            func.sum(TopSong.streams).label('total_streams'))\
        .group_by(TopSong.country_id, TopSong.song_id)\
        .limit(self.n_top_songs)\
        .all()

        return pd.DataFrame(top_songs).pivot(
            'country_id', 'song_id', 'total_streams').fillna(0).astype(float)
