drop table if exists answers;
drop table if exists users;

create table if not exists users (
id_user serial primary key,
first_name varchar(20) not null,
second_name varchar(20) not null,
city varchar(20) not null,
age int not null
);

create table if not exists answers (
id_test serial primary key,
ttype int not null check(ttype > 0 and ttype < 4),
q1 varchar(250) not null,
q2 varchar(250) not null,
q3 varchar(250) not null,
q4 varchar(250) not null,
q5 varchar(250) not null,
q6 varchar(3000),
q7 varchar(3000),
q8 varchar(3000),
constraint fk1 foreign key(id_test)
	references users(id_user) on delete cascade on update cascade
);

INSERT INTO users (first_name, second_name, city, age)
VALUES ('Test', 'Test', 'Test', 1)