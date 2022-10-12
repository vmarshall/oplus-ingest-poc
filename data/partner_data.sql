create table patient_data (
    id int not null auto_increment,
    name varchar(255) not null,
    primary key (id)
);

create table doctor_note (
    id int not null auto_increment,
    name varchar(255) not null,
    primary key (id)
    body = varchar(255) not null

);

create table patient_doctor_note (
    patient_id int not null,
    doctor_note_id int not null,
    primary key (patient_id, doctor_note_id),
    foreign key (patient_id) references patient_data(id),
    foreign key (doctor_note_id) references doctor_note(id)
);