from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import exc
Base = declarative_base()

Session = sessionmaker()
engine=create_engine("mysql://root:sai@localhost:3306/sai",echo=True)
Base.metadata.create_all(engine)
session = Session.configure(bind=engine)
session = Session()

class TICKETS(Base):
    __tablename__ = "TICKETS"
    Id=Column(Integer,primary_key=True)
    Agent_ID = Column(Integer)
    Bus_Name = Column(String(30))
    From = Column(String(25))
    To = Column(String(35))
    No_of_tickets_booked = Column(Integer)
    Total_fare = Column(Integer)

    def __init__(self,Agent_ID=None,Bus_Name=None,From=None,To=None,No_of_tickets_booked=None,Total_fare=None):
        self.Agent_ID = Agent_ID
        self.Bus_Name = Bus_Name
        self.From = From
        self.To = To
        self.No_of_tickets_booked = No_of_tickets_booked
        self.Total_fare = Total_fare
    def reversedisplay(self):
        dis = session.query(TICKETS).all()
        for i in reversed(dis):
            print(i.Agent_ID, i.Bus_Name, i.From, i.To, i.No_of_tickets_booked, i.Total_fare)

    def display(self):
        dis=session.query(TICKETS).all()
        for i in dis:
            print(i.Agent_ID,i.Bus_Name,i.From,i.To,i.No_of_tickets_booked,i.Total_fare)

    def insert(self):
        a=input("Enter the Agent ID : ")
        b=input("Enter the Bus Name : ")
        c=input("Enter the Bus Starting Point : ")
        d=input("Enter the Bus Destination : ")
        e=int(input("Enter the No of Tickets booked : "))
        
        try:
            obj = TICKETS(a,b,c,d,e)
            session.add(obj)
            obj.display()
            session.commit()
            
        except Exception:
            meta = MetaData()
            ticket = Table(
                'TICKETS', meta,
                Column('Id', Integer, primary_key=True),
                Column('Agent_ID', Integer),
                Column('Bus_Name', String(18)),
                Column('From', String(27)),
                Column('To', String(27)),
                Column('No_of_tickets_booked', Integer),
                Column('Total_fare', Integer),
            )
            meta.create_all(engine)
        obj = TICKETS(a, b, c, d, e)
        session.add(obj)
        obj.display()
        session.commit()
