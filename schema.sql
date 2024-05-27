CREATE TABLE IF NOT EXISTS cadastros (
    id       INTEGER PRIMARY KEY AUTOINCREMENT
                     NOT NULL,
    name     TEXT,
    email            NOT NULL
                     UNIQUE,
    password         NOT NULL
);
