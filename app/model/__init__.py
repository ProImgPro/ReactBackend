# # coding: utf-8
# # from app.extensions import db
# # from sqlalchemy import and_, or_
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:////‪C:\\Users\\BootAI\\Downloads\\test.db')
# Base = declarative_base()
# Base.metadata.bind = engine
# from sqlalchemy.orm import sessionmaker
# DBSession = sessionmaker()
# DBSession.bind = engine
# session = DBSession()
#
#
#
# class Qa(Base):
#     __tablename__ = 'qa'
#
#     id = db.Column(db.Integer, primary_key=True, unique=True)
#     questions = db.Column(db.Text, nullable=False)
#     a = db.Column(db.Text, nullable=False)
#     b = db.Column(db.Text, nullable=False)
#     c = db.Column(db.Text, nullable=False)
#     d = db.Column(db.Text, nullable=False)
#     answer = db.Column(db.Text, nullable=False)
#     description = db.Column(db.Text, nullable=False)
#
#     @classmethod
#     def get_data(cls):
#         """
#         Given name, return role id
#         Parameters
#         ----------
#         name:
#
#         Returns
#         -------
#         adviser user object
#         """
#         results = db.session.query(qa).first()
#         return results
#
# engine = create_engine('sqlite:///sqlalchemy_example.db')
