from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *

Base = declarative_base()
Session = sessionmaker()
engine=create_engine("mysql://root:sai@localhost:3306/sai",echo=True)
Base.metadata.create_all(engine)
session = Session.configure(bind=engine)
session = Session()

class AGENT(Base):
    __tablename__ = "AGENT"
    Agent_ID = Column(Integer,primary_key=True)
    Agent_Name = Column(String(30))
    Mobile_No = Column(Integer)
    Password = Column(String(35))

    def __init__(self,Agent_Name=None,Mobile_No=None,Password=None):
        self.Agent_Name = Agent_Name
        self.Mobile_No = Mobile_No
        self.Password = Password
        
    def display(self=None):
        dis=session.query(AGENT).all()
        for i in dis:
            print('Agent Name:',i.Agent_Name,'Mobile Number:',i.Mobile_No,'Password:',i.Password,'Agent Id:',i.Agent_ID)

    def insert(self=None):
        name = input("Enter the Agent Name : ")
        mn = input("Enter the Agent Mobile Number : ")
        p = input("Enter the Password : ")
        
        try:
            obj = AGENT(name, mn, p)
            session.add(obj)
            session.commit()
            
        except Exception:
            meta = MetaData()

            agent = Table(
                'AGENT', meta,
                Column('Agent_Id', Integer, primary_key=True),
                Column('Agent_Name', String(18)),
                Column('Mobile_No', Integer),
                Column('Password', String(18)),
            )
            meta.create_all(engine)
        obj = AGENT(name, mn, p)
        session.add(obj)
        session.commit()
        
    def login(self):
        log=session.query(AGENT).all()
        for i in log:
            if i.Agent_Name==self.Agent_Name and i.Password==self.Password:
                return [i.Agent_Name,i.Mobile_No,i.Password,i.Agent_ID]
