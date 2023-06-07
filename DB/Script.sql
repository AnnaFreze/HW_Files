create table if not exists Genre (
	id SERIAL primary key,
	name VARCHAR(40) not null
); 

create table if not exists Artist (
	id SERIAL primary key,
	name VARCHAR(60) not null
);

create table if not exists Genres_Artists (
	genre_id INTEGER references Genre(id),
	artist_id INTEGER references Artist(id),
	constraint pk primary key (genre_id, artist_id)
);

create table if not exists Album (
	id SERIAL primary key,
	name VARCHAR(60) not null,
	year INTEGER
	);
	
create table if not exists Artists_Albums (
	album_id INTEGER references Album(id),
	artist_id INTEGER references Artist(id),
	constraint pk2 primary key (album_id, artist_id)
	);
	
create table if not exists Tracks (
	id SERIAL primary key,
	name VARCHAR(60) not null,
	duration TIME not null,
	album_id INTEGER not null references Album(id)
	);

create table if not exists Collections (
	id SERIAL primary key,
	name VARCHAR(60) not null,
	year INTEGER
	);

create table if not exists Collections_Tracks (
	track_id INTEGER references Tracks(id),
	collection_id INTEGER references Collections(id),
	constraint pk3 primary key (track_id, collection_id)
	);
	