CREATE TABLE IF NOT EXISTS cadastro (
    id       INTEGER PRIMARY KEY AUTOINCREMENT
                     NOT NULL,
    name     TEXT,
    email            NOT NULL
                     UNIQUE,
    password         NOT NULL
);
