
drop table if exists usepass;
    create table usepass(
        id integer primary key,
        surname text not null,
        firstname text not null,
        age integer not null,
        email text not null,
        password text not null
    )