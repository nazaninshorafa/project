CREATE DATABASE ai_website;

USE ai_website;

CREATE TABLE images (
    image_id INT ,
    title VARCHAR(255),
    tags VARCHAR(255),
    description VARCHAR(255),
    category VARCHAR(255) NOT NULL ,
    PRIMARY KEY (image_id)
);

CREATE TABLE photographers (
    photographer_code INT ,
    photographer_name VARCHAR(255),
    photographer_email VARCHAR(255)
);

CREATE TABLE articles (
    article_id INT ,
    content VARCHAR(255),
    keywords VARCHAR(255),
    title VARCHAR(255),
    category VARCHAR(255) NOT NULL ,
    PRIMARY KEY (article_id)
);

CREATE TABLE writers (
    writer_code INT ,
    writer_name VARCHAR(255),
    writer_email VARCHAR(255),
    photographer_code INT,
    FOREIGN KEY (photographer_code) REFERENCES photographers(photographer_code)
);
