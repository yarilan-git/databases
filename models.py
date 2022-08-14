"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Song(db.Model):
    """Song."""

    __tablename__ = 'song'

    id          = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    title       = db.Column(db.Text, nullable=False, unique=True)
    artist      = db.Column(db.Text, nullable=False)

    @classmethod
    def get_song_info(self, id):
        return Song.query.get(id)

    @classmethod
    def get_songs_not_on_list(self, list_id):
        return db.session.query(Song.id, Song.title).outerjoin(PlaylistSong).outerjoin(Playlist).filter((Playlist.id != list_id)|(Playlist.id.is_(None))).all()

    def __repr__(self):
        return f"id: {self.id}, title: {self.title}, artist: {self.artist}"

class Playlist(db.Model):
    """Playlist."""

    __tablename__ = 'playlist'

    id          = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    name        = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text, nullable = False)
    songs       = db.relationship('Song', secondary='playlist_song', backref='playlists')

    @classmethod
    def get_list_info(self, id):
        return Playlist.query.get(id)

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, description: {self.description}"





class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = 'playlist_song'
    id            = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    playlist_id   = db.Column(db.Integer, db.ForeignKey('playlist.id'))
    song_id       = db.Column(db.Integer, db.ForeignKey('song.id'))

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
