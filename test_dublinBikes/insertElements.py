from database import db_session
from models import Static
s = Static('99', 'CITY QUAY', 'City Quay', '53.346637', '-6.246154', False, False)
db_session.add(s)
db_session.commit()