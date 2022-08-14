from flask import Flask, redirect, flash, render_template
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    try:
        playlist = Playlist.get_list_info(playlist_id)
    except:
        flash("Faild getting playlist info from the database!")
    return render_template('playlist.html', title='Playlist', playlist=playlist)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to db and redirect to list-of-playlists
    """

    playlist_form=PlaylistForm()
    if playlist_form.validate_on_submit():
        pl = Playlist(name=playlist_form.name.data,
                      description=playlist_form.description.data)
        try:
           db.session.add(pl)
           db.session.commit()
        except IntegrityError:
           flash("The playlist name already exists! Try another name.")
        return redirect('/')
    else:
        return render_template('new_playlist.html', title='Add a playlist', playlist_form=playlist_form)

##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""
    song=Song.get_song_info(song_id)
    return render_template('song.html', title='Song info', song=song)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """

    new_song_form=SongForm()
    if new_song_form.validate_on_submit():
        song = Song(title=new_song_form.title.data,
                    artist=new_song_form.artist.data)
        try:
           db.session.add(song)
           db.session.commit()
           return redirect('/songs')
        except IntegrityError:
            flash("This song title already exists!")
            return render_template('new_song.html', title='Add a song', new_song_form=new_song_form)
    else:
        return render_template('new_song.html', title='Add a song', new_song_form=new_song_form)


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist
    form.song.choices = Song.get_songs_not_on_list(playlist_id)

    if form.validate_on_submit():
        play_list_song = PlaylistSong(playlist_id=playlist_id,
                                      song_id=form.song.data)
        db.session.add(play_list_song)
        db.session.commit()
        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html",
                             playlist=playlist,
                             form=form)





