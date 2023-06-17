select name, duration from tracks
where duration = (select max(duration) from tracks);

select name, duration from tracks
where duration >= 210;

select name from collections
where year between 2018 and 2020;

select name from artist
where name not like '% %';

select name from tracks
where name ilike 'my %' 
or name ilike '% my %'
or name ilike '% my'
or name ilike 'my';

select name, count(artist_id) from genres_artists ga
left join genre g on ga.genre_id = g.id
group by g.name;

select count(t.id) from tracks t
left join album a on a.id = t.album_id
where a.year between 2019 and 2020;

select a.name, avg(t.duration) track_d from tracks t
join album a on a.id = t.album_id
group by a.name;

select a.name from artist a
join artists_albums aa on aa.artist_id = a.id
join album al on al.id = aa.album_id
where a.name != (select a.name from artist a
join artists_albums aa on aa.artist_id = a.id
join album al on al.id = aa.album_id where al.year = 2020)
group by a.id;

select c.name from collections c
join collections_tracks ct on c.id = collection_id
join tracks t on t.id = track_id
join album al on al.id = t.album_id
join artists_albums aa ON aa.album_id = al.id
join artist a on a.id = aa.artist_id
where a.name = 'Linkin Park'
group by c.name;



