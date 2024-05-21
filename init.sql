CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Auth123';

CREATE DATABASE AuthService;
GRANT ALL PRIVILEGES ON AuthService.* TO 'auth_user'@'localhost';

USE AuthService;

CREATE TABLE `user` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO `user` (email, password) VALUES ('ojiamboloc@gmail.com', 'Admin123');


-- //basic authentication
-- username
-- password
