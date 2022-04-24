CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS portfolio (
  username TEXT NOT NULL,
  fio TEXT NOT NULL,
  age INTEGER,
  profile_photo TEXT NOT NULL,
  proffesion TEXT NOT NULL,
  status TEXT NOT NULL,
  info TEXT NOT NULL,
);

CREATE TABLE IF NOT EXISTS contacts (
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    vk TEXT NOT NULL,
    ln TEXT NOT NULL,
    tg TEXT NOT NULL,
);

CREATE TABLE IF NOT EXISTS works (
    username TEXT NOT NULL,
    years TEXT NOT NULL,
    place TEXT NOT NULL,
    post TEXT NOT NULL,
);

CREATE TABLE IF NOT EXISTS awards (
    username TEXT NOT NULL,
    photo TEXT NOT NULL,
);

CREATE TABLE IF NOT EXISTS projects (
    username TEXT NOT NULL,
    photo TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    link TEXT NOT NULL,
);

CREATE TABLE IF NOT EXISTS main_skills (
    username TEXT NOT NULL,
    skill TEXT NOT NULL,
);

CREATE TABLE IF NOT EXISTS extra_skills (
    username TEXT NOT NULL,
    skill TEXT NOT NULL,
);

CREATE TABLE IF NOT EXISTS education (
    username TEXT NOT NULL,
    edu TEXT NOT NULL
);
