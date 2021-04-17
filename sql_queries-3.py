import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS events_staging cascade;"
staging_songs_table_drop = "DROP TABLE IF EXISTS songplay_staging cascade;"
songplay_table_drop = "DROP TABLE IF EXISTS songplay cascade;"
user_table_drop = "DROP TABLE IF EXISTS user;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE events_staging
(
  id                    IDENTITY(0,1) PRIMARY KEY,
  artist                 VARCHAR NOT NULL,
  auth                   VARCHAR NOT NULL,
  first_name             VARCHAR NOT NULL,
  gender                 VARCHAR NOT NULL,
  item_session           INTEGER NOT NULL,
  last_name              VARCHAR NOT NULL,
  length                 VARCHAR NOT NULL,
  level                  VARCHAR NOT NULL,
  location               VARCHAR NOT NULL,
  method                 VARCHAR NOT NULL,
  page                   VARCHAR NOT NULL,
  registration           VARCHAR NOT NULL,
  session_id             INTEGER NOT NULL,
  song                   VARCHAR NOT NULL,
  status                 INTEGER NOT NULL,
  ts                     VARCHAR NOT NULL,
  user_agent             VARCHAR NOT NULL,
  user_id                INTEGER NOT NULL
);
""")

staging_songs_table_create = ("""
CREATE TABLE songplay_staging
(
  id                   IDENTITY(0,1) PRIMARY KEY,
  num_songs            INTEGER NOT NULL,
  artist_id            VARCHAR NOT NULL,
  artist_latitude      VARCHAR NOT NULL,
  artist_longitude     VARCHAR NOT NULL,
  artist_location      VARCHAR NOT NULL,
  artist_name          VARCHAR NOT NULL,
  song_id              VARCHAR NOT NULL,
  title                VARCHAR NOT NULL,
  duration             VARCHAR NOT NULL,
  year                 INTEGER NOT NULL,
);
""")

songplay_table_create = ("""
CREATE TABLE songplay 
(
  id                    IDENTITY(0,1) PRIMARY KEY,
  songplay_id           INTEGER NOT NULL,
  start_time            TIMESTAMP NOT NULL,
  user_id               INTEGER NOT NULL,
  level                 VARCHAR NOT NULL,
  song_id               VARCHAR NOT NULL,
  artist_id             VARCHAR NOT NULL,
  session_id            INTEGER NOT NULL,
  location              VARCHAR NOT NULL
  user_agent            VARCHAR NOT NULL
);
""")

user_table_create = ("""
CREATE TABLE user 
(
  id                IDENTITY(0,1) PRIMARY KEY,
  user_id           INTEGER NOT NULL,
  first_name        VARCHAR(25) NOT NULL,
  last_name         VARCHAR(25) NOT NULL,
  gender            VARCHAR(1) NOT NULL,
  level             VARCHAR(9) NOT NULL
);
""")

song_table_create = ("""
CREATE TABLE song 
(
  id                IDENTITY(0,1) PRIMARY KEY,
  song_id           VARCHAR NOT NULL,
  title             VARCHAR(25) NOT NULL,
  artist_id         VARCHAR NOT NULL,
  year              INTEGER NOT NULL,
  duration          INTEGER NOT NULL
);
""")

artist_table_create = ("""
CREATE TABLE artist 
(
  id                  IDENTITY(0,1) PRIMARY KEY,
  artist_id           VARCHAR NOT NULL,
  name                VARCHAR(25) NOT NULL,
  location            VARCHAR(25) NOT NULL,
  latitude            INTEGER ,
  longitude           INTEGER 
);
""")

time_table_create = ("""
CREATE TABLE time 
(
  id                   IDENTITY(0,1) PRIMARY KEY
  start_time           TIMESTAMP NOT NULL,
  hour                 INTEGER NOT NULL,
  day                  INTEGER NOT NULL,
  week                 INTEGER ,
  month                INTEGER 
  year                 INTEGER 
  weekday              INTEGER 
);
""")

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]

