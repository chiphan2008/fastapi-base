from fastapi import HTTPException, Depends

from app.models import User
from app.services.user import UserService
from app.schemas.user import UserCreateRequest
from app.helpers.enums import UserRole
from app.core.config import settings
from app.core.security import verify_password, get_password_hash
from app.db.base import engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5433/postgres', pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
session = SessionLocal()
session.rollback()
session.commit()

# superuser
try:
    new_user = User(
        full_name='Admin',
        hashed_password=get_password_hash(settings.FIRST_SUPERUSER_PASSWORD),
        email=settings.FIRST_SUPERUSER,
        is_active = True,
        role = 'admin'
    )
    session.add(new_user)
    session.commit()
except:
    print('Admin is already exists')

