use db;

CREATE TABLE messageapi(
    msg_id int not null AUTO_INCREMENT,
    msg_text varchar(500) NOT NULL,
    PRIMARY KEY (msg_id)
);

INSERT INTO messageapi(msg_text)
VALUES ("Ola, Inoa!");