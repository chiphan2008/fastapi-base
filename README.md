![alt text](logo-teal.png "FastAPI")

# FASTAPI BASE

## Introduction
FastAPI Base
Modules: CRUD User, Login, Register, pytest, migration

## Source Library
- [FastAPI](https://fastapi.tiangolo.com/)
- [Postgresql(>=12)](https://www.postgresql.org/)
- Alembic
- API Login
- API CRUD User, API Get Me & API Update Me
- Pagination
- Authen/Authorize with JWT
- Permission_required & Login_required
- Logging
- Pytest

## Installation dev
Create screct key
`openssl rand -hex 32`
$ cp env.example .env       // Update

**Option 1:**
- Clone Project
- Install Postgresql & Create Database
- `pip3 install -r requirements.txt`
- Port: 8000
```
// Create postgresql Databases via CLI (Ubuntu 20.04)
$ sudo -u postgres psql
# CREATE DATABASE fastapi_base;
# CREATE USER db_user WITH PASSWORD 'secret123';
# GRANT ALL PRIVILEGES ON DATABASE fastapi_base TO db_user;

// Clone project & run
$ git clone https://github.com/playgroundvina/fastapi-base
$ cd fastapi-base
$ virtualenv -p python3.8 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ cp env.example .env       // Update
$ alembic upgrade head
$ uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
**Option 2:** Using Docker & Docker Compose
- Clone Project
- Run docker-compose
```
$ git clone https://github.com/playgroundvina/fastapi-base
$ cd fastapi-base
$ DOCKER_BUILDKIT=1 docker build -t fastapi-base:latest .
$ docker-compose up -d
```


## Installation production
Comming soon

## Project structure
```
.  
├── alembic  
│   ├── versions    // migration files
│   └── env.py  
├── app  
│   ├── api         // api
│   ├── core        // file config load ,env & function verify JWT access-token  
│   ├── db          // DB session config
│   ├── helpers     // Helper function login_manager, paging  
│   ├── models      // Database model
│   ├── schemas     // Pydantic Schema  
│   ├── services    // CRUD 
│   └── main.py     // Project main
├── tests  
│   ├── api         // api test
│   ├── faker       // faker data
│   ├── .env        // config DB test  
│   └── conftest.py // pytest config 
├── .gitignore  
├── alembic.ini  
├── docker-compose.yaml  
├── Dockerfile  
├── env.example  
├── logging.ini     // logging  
├── postgresql.conf // postgresql use when run docker-compose  
├── pytest.ini      // pytest file setup   
├── README.md  
└── requirements.txt    // libs
```

## Migration

**File migration - SAMPLE**
```
# alembic/versions/f9a075ca46e9_.py

...
def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_full_name'), 'user', ['full_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_full_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
...
```

## Guide: Create model and migration
Link [CREATE_DB_GUIDE.md](./document/CREATE_DB_GUIDE.md)