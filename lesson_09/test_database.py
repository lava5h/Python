import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Подключение к базе данных
DATABASE_URL = "mysql+pymysql://root:@localhost/test"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)

SessionLocal = sessionmaker(bind=engine)

# Тест на создание пользователя
def test_create_user():
    session = SessionLocal()
    new_user = User(name="Иван", email="ivan@example.com")
    session.add(new_user)
    session.commit()

    user = session.query(User).filter_by(email="ivan@example.com").first()
    assert user is not None
    assert user.name == "Иван"

    session.close()

# Тест на редактирование пользователя
def test_update_user():
    session = SessionLocal()
    user = session.query(User).filter_by(email="ivan@example.com").first()
    user.name = "Пётр"
    session.commit()

    updated_user = session.query(User).filter_by(email="ivan@example.com").first()
    assert updated_user.name == "Пётр"

    session.close()

# Тест на удаление пользователя
def test_delete_user():
    session = SessionLocal()
    user = session.query(User).filter_by(email="ivan@example.com").first()
    session.delete(user)
    session.commit()

    deleted_user = session.query(User).filter_by(email="ivan@example.com").first()
    assert deleted_user is None

    session.close()
