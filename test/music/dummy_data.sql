BEGIN;
INSERT INTO music_artist(name,pid) values('Rosalinda', 'ARD4C1I1187FB4B0C3');
INSERT INTO music_album(title) values('Bricks');
INSERT INTO music_genre(title) values('Rock');
COMMIT;

BEGIN;
SELECT @artist_id:=id from music_artist limit 1;
SELECT @album_id:=id from music_album limit 1;
INSERT INTO music_song(title, lyrics, pid, artist_id, album_id) values('Paranoid','Finished with my woman...','SOIVZWT12A6D4F3DA9', @artist_id, @album_id);
COMMIT;

