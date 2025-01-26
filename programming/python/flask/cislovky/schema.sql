DROP TABLE IF EXISTS cislovky;

CREATE TABLE cislovky (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cs TEXT UNIQUE NOT NULL,
  en TEXT UNIQUE NOT NULL,
  rome TEXT UNIQUE NOT NULL
);

INSERT INTO cislovky (cs, en, rome) VALUES
('jedna', 'one', 'I'),
('dva', 'two', 'II'),
('tři', 'three', 'III'),
('čtyři', 'four', 'IV');