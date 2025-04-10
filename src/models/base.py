from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
  pass

class Ticket(Base):
  __tablename__ = "tickets"
  id: Mapped[str] = mapped_column(String, primary_key=True)
  title: Mapped[str] = mapped_column(String)
  description: Mapped[str] = mapped_column(String)
  area: Mapped[str] = mapped_column(String)  

class Technician(Base):
  __tablename__ = "technician"
  id: Mapped[str] = mapped_column(String, primary_key=True)
  name: Mapped[str] = mapped_column(String)
  area: Mapped[str] = mapped_column(String)
  email: Mapped[str] = mapped_column(String)

class Area(Base):
  __tablename__ = "area"
  id: Mapped[str] = mapped_column(String, primary_key=True)
  name: Mapped[str] = mapped_column(String)
  description: Mapped[str] = mapped_column(String)

#add relation between area and technicians