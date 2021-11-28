drop if exists users
drop if exists answers

create table if not exists users (
id_user int primary key,
first_name varchar(20) not null,
second_name varchar(20) not null,
city varchar(20) not null,
age int not null
);

create table if not exists answers (
id_test int primary key,
type_test int not null check(type_test > 0 and type_test < 4),
first_quest varchar(250) not null,
second_quest varchar(250) not null,
third_quest varchar(250) not null,
fourth_quest varchar(250) not null,
fifth_quest varchar(250) not null,
sixth_quest varchar(500),
seventh_quest varchar(500),
eighth_quest varchar(500),
constraint fk1 foreign key(id_test)
	references users(id_user) on delete cascade on update cascade
);