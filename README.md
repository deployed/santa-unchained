# Santa Unchained

[![CI](https://github.com/deployed/santa-unchained/actions/workflows/backend.yml/badge.svg)](https://github.com/deployed/santa-unchained/actions)

Repository prepared for backend workshop with AGH Kernel.

# Prerequisites

- [Python3.10](https://www.python.org/downloads/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Local Development

First create postgresql database:

```sql
create user santa_unchained with createdb;
alter user santa_unchained password 'santa_unchained';
create database santa_unchained owner santa_unchained;
```
Now you can setup virtualenv and django:
```bash
virtualenv venv
source venv/bin/activate
make bootstrap
```

Default users in fixtures:

| Username | Password  |
|----------|-----------|
| admin    | admin321! |
| santa    | admin321! |
| elf      | admin321! |
