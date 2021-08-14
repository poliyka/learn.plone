# -*- coding: utf-8 -*-
from learn.plone import _
from plone import api
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.sqlalchemy.engine import Engine
from learn.plone.models.user import User, Address
from learn.plone.models.store import Store, Tag

from sqlalchemy.orm import aliased
from sqlalchemy import select, insert, update, delete
import sqlalchemy as sa

class Alchemy(BrowserView):

    def insert_data(self, session):
        # 2.0
        stmt = (
            insert(User).
            values(name="new", fullname="hello", nickname="world").
            returning(f"{User.id}+{User.name}").
            label("user_id_name")
        )
        aaa = session.execute(stmt)
        import pdb; pdb.set_trace()

        # 1.0
        ed_user = User(name="ed", fullname="Ed Jones", nickname="edsnickname")
        session.add(ed_user)
        session.add_all(
            [
                User(name="wendy", fullname="Wendy Williams", nickname="windy"),
                User(name="mary", fullname="Mary Contrary", nickname="mary"),
                User(name="fred", fullname="Fred Flintstone", nickname="freddy"),
            ]
        )
        session.commit()

    def update_data(self, session):
        # 2.0
        # multiple
        stmt = (
            update(User).
            where(User.name == "new").
            values({
                "fullname": "update_name",
            })
        )
        session.execute(stmt)
        import pdb; pdb.set_trace()

        # 1.0
        # multiple
        session.query(User).filter(User.name == "ed").update(
            {
                "fullname": "ed Andy",
            }
        )
        session.commit()

        # single
        ed_user = session.query(User).filter(User.name == "ed").first()
        ed_user.fullname = "Ed test"
        session.commit()

    def __call__(self):
        """
        類似sqlalchemy-mixins的使用方式
        https://github.com/absent1706/sqlalchemy-mixins
        """
        engine = Engine()

        self.insert_data(engine.session)
        # self.update_data(engine.session)
        # self.delete_data(engine.session)
        # self.base_use(engine.db)
        # self.session_search(engine.session)
        # self.aliased_search(engine.session)
        # self.query_filter(engine.session)
        # self.many_to_one(engine.session)
        # self.many_to_many(engine.session)
        # self.one_to_many(engine.session)
        # self.one_to_one(engine.session)

        engine.session.close()
        return "done"
