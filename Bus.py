from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
import Tickets
Base = declarative_base()

engine=create_engine('mysql://root:sai@localhost:3306/sai',echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker()
session = Session.configure(bind=engine)
session = Session()

class BUS(Base):
    __tablename__ = "BUS"
    Bus_ID = Column(Integer, Sequence('seq_bus_id', start=5001),primary_key=True )
    Bus_Name = Column(String(30))
    From = Column(String(25))
    To = Column(String(35))
    Total_Seat = Column(Integer)
    Price = Column(Integer)


    def __init__(self,Bus_Name=None,From=None,To=None,Total_Seat=None,Price=None):
        self.Bus_Name = Bus_Name
        self.From = From
        self.To = To
        self.Total_Seat = Total_Seat
        self.Price = Price
    def display(self):
        dis=session.query(BUS).all()
        for i in dis:
            print(i.Bus_Name,i.From,i.To,i.Total_Seat,i.Price,i.Bus_ID)

    def wherebusid(self,tbid):
        dis=session.query(BUS).filter_by(Bus_ID=tbid).all()
        for i in dis:
            print(i.Bus_Name, i.From, i.To, i.Total_Seat)
    
    def booking(self,nooftickets,tbid,tagid):
        dis = session.query(BUS).filter_by(Bus_ID=tbid).all()
        t=dis[0]
        tc=t.Total_Seat
        price=t.Price
        
        if(nooftickets<=tc):
            tc-=nooftickets
            print("Total fare :", price * nooftickets)
            confirmation = input("Confirm Total tickets[Y/N] : ")
            if (confirmation in ['Y','y']):
                session.query(BUS).filter_by(Bus_ID=tbid).update({BUS.Total_Seat:tc})
                obj=Tickets.TICKETS(tagid,t.Bus_Name,t.From,t.To,nooftickets,price*nooftickets)
                session.add(obj)
                print(tagid, t.Bus_Name, t.From, t.To, nooftickets, price * nooftickets)

            else:
                print("Thank you!!!")
        else:
            print("Tickets Not Available")
        session.commit()
        
    #To insert the values
    def insert(self=None):
        a=input("Enter the Bus Name : ")
        b=input("Enter the Bus Starting Point : ")
        c=input("Enter the Bus Destination : ")
        d=int(input("Enter the Total No of Seats : "))
        e=eval(input("Enter the Price : "))
        
        try:
            obj = BUS(a,b,c,d,e)
            session.add(obj)
            session.commit()
            
        except Exception:
            meta = MetaData()
            Bus = Table(
                'BUS', meta,
                Column('Bus_Id', Integer, primary_key=True),
                Column('Bus_Name', String(18)),
                Column('From', String(27)),
                Column('To', String(27)),
                Column('Total_Seat', Integer),
                Column('Price', Integer),
            )
            meta.create_all(engine)
        obj = BUS(a, b, c, d, e)
        session.add(obj)
        session.commit()
