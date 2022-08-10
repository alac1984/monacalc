# type: ignore[valid-type]
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class SchoolDB(Base):
    __tablename__ = "tb_school"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    contracts = relationship(
        "ContractDB", back_populates="school", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"SchoolDB(id={self.id}, name={self.name})"


class ContractDB(Base):
    __tablename__ = "tb_contract"

    id = Column(Integer, primary_key=True)
    school_id = Column(ForeignKey("tb_school.id"), nullable=False)
    mat = Column(String, nullable=False)
    start = Column(Date, nullable=False)
    end = Column(Date, nullable=False)
    work_hours = Column(Integer, nullable=False)

    school = relationship("SchoolDB", back_populates="contracts")

    def __repr__(self):
        return (
            f"ContractDB(id={self.id}, school={self.school.name}, start="
            f"{self.start}, end={self.end}, work_hours={self.work_hours})"
        )
