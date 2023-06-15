insert into genre(name)
values ('Alternative Rock');

insert into genre(name)
values ('Nu Metal');

insert into genre(name)
values ('Progressive Rock');

insert into genre(name)
values ('Art Rock');

insert into genre(name)
values ('Indie Rock');

insert into artist(name)
values ('Linkin Park');

insert into artist(name)
values ('Muse');

insert into artist(name)
values ('Aquarium');

insert into artist(name)
values ('Splean');

insert into genres_artists(genre_id, artist_id)
values (1,1);

insert into genres_artists(genre_id, artist_id)
values (1,2);

insert into genres_artists(genre_id, artist_id)
values (1,1);

insert into genres_artists(genre_id, artist_id)
values (1,4);

insert into genres_artists(genre_id, artist_id)
values (2,1);

insert into genres_artists(genre_id, artist_id)
values (3,2);

insert into genres_artists(genre_id, artist_id)
values (3,4);

insert into genres_artists(genre_id, artist_id)
values (4,2);

insert into genres_artists(genre_id, artist_id)
values (4,3);

insert into genres_artists(genre_id, artist_id)
values (5,3);

insert into genres_artists(genre_id, artist_id)
values (5,4);

insert into album(name, year)
values ('Meteora', 2003);

insert into album(name, year)
values ('A Thousands Suns', 2010);

insert into album(name, year)
values ('The Resistance', 2010);

insert into album(name, year)
values ('Black Holes and Revelations', 2006);

insert into album(name, year)
values ('White Horse', 2008);

insert into album(name, year)
values ('Pomegranate Album', 1998);

insert into album(name, year)
values ('Sign of Fire', 2020);

insert into tracks(name, album_id, duration)
values ('Somewhere I Belong', 1, 214);

insert into tracks(name, album_id, duration)
values ('Session', 1, 144);

insert into tracks(name, album_id, duration)
values ('Numb', 1, 188);

insert into tracks(name, album_id, duration)
values ('Waiting for the End', 2, 232);

insert into tracks(name, album_id, duration)
values ('The Catalyst', 2, 340);

insert into tracks(name, album_id, duration)
values ('Wisdom, Justice and Love', 2, 99);

insert into tracks(name, album_id, duration)
values ('Uprising', 3, 305);

insert into tracks(name, album_id, duration)
values ('Resistance', 3, 347);

insert into tracks(name, album_id, duration)
values ('Guiding Light', 3, 254);

insert into tracks(name, album_id, duration)
values ('Knights of Cydonia', 4, 367);

insert into tracks(name, album_id, duration)
values ('Map of the Problematique', 4, 214);

insert into tracks(name, album_id, duration)
values ('The White Horse', 5, 155);

insert into tracks(name, album_id, duration)
values ('Unspeakable', 5, 304);

insert into tracks(name, album_id, duration)
values ('No Exit', 6, 221);

insert into tracks(name, album_id, duration)
values ('God Is Tired to Love US', 6, 145);

insert into tracks(name, album_id, duration)
values ('Maria and Juana', 6, 292);

insert into tracks(name, album_id, duration)
values ('My Heart', 6, 246);

insert into tracks(name, album_id, duration)
values ('My Name is Dust', 7, 206);

insert into tracks(name, album_id, duration)
values ('Morning in Fields', 7, 232);

insert into tracks(name, album_id, duration)
values ('Not Meant to Be', 7, 423);

insert into collections(name, year)
values ('Unplugged', 2002);

insert into collections(name, year)
values ('Thor', 2020);

insert into collections(name, year)
values ('One More Light', 2017);

insert into collections(name, year)
values ('Dream Team', 2020);

insert into collections(name, year)
values ('Live at Rome Olympic Stadium', 2013);

insert into artists_albums(album_id, artist_id)
values (1,1);

insert into artists_albums(album_id, artist_id)
values (2,1);

insert into artists_albums(album_id, artist_id)
values (3,2);

insert into artists_albums(album_id, artist_id)
values (4,2);

insert into artists_albums(album_id, artist_id)
values (5,3);

insert into artists_albums(album_id, artist_id)
values (6,4);

insert into artists_albums(album_id, artist_id)
values (7,3);

insert into collections_tracks(track_id, collection_id)
values (5,5);

insert into collections_tracks(track_id, collection_id)
values (10,5);

insert into collections_tracks(track_id, collection_id)
values (12,5);

insert into collections_tracks(track_id, collection_id)
values (14,5);

insert into collections_tracks(track_id, collection_id)
values (16,1);

insert into collections_tracks(track_id, collection_id)
values (17,1);

insert into collections_tracks(track_id, collection_id)
values (13,2);

insert into collections_tracks(track_id, collection_id)
values (2,3);

insert into collections_tracks(track_id, collection_id)
values (3,3);

insert into collections_tracks(track_id, collection_id)
values (7,4);

insert into collections_tracks(track_id, collection_id)
values (9,4);

insert into collections_tracks(track_id, collection_id)
values (10,4);
