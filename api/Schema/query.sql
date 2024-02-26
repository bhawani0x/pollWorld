show databases;
create database pollworld;



CREATE TABLE pollworld.User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    mobile_number VARCHAR(15) NOT NULL,
    dob DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    created_at DATETIME DEFAULT null,
    updated_at DATETIME DEFAULT null
);

select * from pollworld.User;

CREATE TABLE pollworld.Categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    topic VARCHAR(100) NOT NULL
);

select * from pollworld.Categories;