insert into genre(name)
values 
	('Alternative Rock'),
	('Nu Metal'),
	('Progressive Rock'),
	('Art Rock'),
	('Indie Rock');

insert into artist(name)
values 
	('Linkin Park'),
	('Muse'),
	('Aquarium'),
	('Splean');

insert into genres_artists(genre_id, artist_id)
values 
	(1,1),
	(1,2),
	(1,4),
	(2,1),
	(3,2),
	(3,4),
	(4,2),
	(4,3),
	(5,3),
	(5,4);

insert into album(name, year)
values 
	('Meteora', 2003),
	('A Thousands Suns', 2010),
	('The Resistance', 2010),
	('Black Holes and Revelations', 2006),
	('White Horse', 2008),
	('Pomegranate Album', 1998),
	('Sign of Fire', 2020);

insert into tracks(name, album_id, duration)
values 
('Somewhere I Belong', 1, 214),
('Session', 1, 144),
('Numb', 1, 188),
('Waiting for the End', 2, 232),
('The Catalyst', 2, 340),
('Wisdom, Justice and Love', 2, 99),
('Uprising', 3, 305),
('Resistance', 3, 347),
('Guiding Light', 3, 254),
('Knights of Cydonia', 4, 367),
('Map of the Problematique', 4, 214),
('The White Horse', 5, 155),
('Unspeakable', 5, 304),
('No Exit', 6, 221),
('God Is Tired to Love US', 6, 145),
('Maria and Juana', 6, 292),
('My Heart', 6, 246),
('My Name is Dust', 7, 206),
('Morning in Fields', 7, 232),
('Not Meant to Be', 7, 423);

insert into collections(name, year)
values 
('Unplugged', 2002),
('Thor', 2020),
('One More Light', 2017),
('Dream Team', 2020),
('Live at Rome Olympic Stadium', 2013);

insert into artists_albums(album_id, artist_id)
values 
(1,1),
(2,1),
(3,2),
(4,2),
(5,3),
(6,4),
(7,3);

insert into collections_tracks(track_id, collection_id)
values 
(5,5),
(10,5),
(12,5),
(14,5),
(16,1),
(17,1),
(13,2),
(2,3),
(3,3),
(7,4),
(9,4),
(10,4);

insert into tracks(name, album_id, duration)
values 
('myself', 7, 100),
('by myself', 7, 110),
('bemy self',7, 120),
('myself by', 7, 130),
('by myself by', 7, 140),
('beemy', 7, 150),
('premyne', 7, 160);

insert into tracks(name, album_id, duration)
values 
('own my', 7, 170),
('my', 7, 180),
('oh my god', 7, 190);

