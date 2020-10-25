from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import Base, TodoItem

engine = create_engine("sqlite:///tasks.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
s = Session()


for desc in ("read a book", "flairing", "wash dishes", "dinner"):
	t = TodoItem(desc)
	s.add(t)

s.commit()