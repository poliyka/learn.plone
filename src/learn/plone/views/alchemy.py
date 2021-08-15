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

import threading


class Alchemy(BrowserView):
    def insert_data(self, session):
        # 2.0
        stmt = insert(User).values(name="new", fullname="hello", nickname="world")
        session.execute(stmt)

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
            update(User)
            .where(User.name == "new")
            .values(
                {
                    "fullname": "update_name",
                }
            )
        )

        session.execute(stmt)

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

    def transaction_data(self, session):
        stmt = select([User.age], User.name == "new")
        age = session.execute(stmt).scalars().first()
        print("age: " + str(age))
        stmt = (
            update(User)
            .where(User.name == "new")
            .values(
                {
                    "age": age + 1,
                }
            )
        )

        session.execute(stmt)
        session.commit()


    def select_data(self, session):
        # Get all User Object
        session.execute(select(User)).scalars().all()

        # query in ids
        stmt = select([User.name], User.id.in_([1, 2, 3, 4]))
        select_result = session.execute(stmt).scalars().all()

        # list emits a deprecation warning
        stmt = select([User.name, User.identity])

        # Return the first element.
        print(session.execute(stmt).scalars().all())

        # Return all element.
        print(session.execute(stmt).mappings().all())

        # Use case set new label
        case_clause = sa.case(
            [(User.id == 3, "three"), (User.id == 7, "seven")],
            else_="neither three nor seven",
        ).label("newLabel")
        stmt = select(User, case_clause)
        print(session.execute(stmt).mappings().all())

    def __call__(self):
        """
        1.0 與 2.0 使用ORM方式的差異
        https://docs.sqlalchemy.org/en/14/changelog/migration_20.html#migration-orm-usage
        類似sqlalchemy-mixins的使用方式
        https://github.com/absent1706/sqlalchemy-mixins
        """
        engine = Engine()

        """
        摘要:[SQL] 使用 交易隔離等級 鎖定 Table 動作
            隔離層級分為四種
            READ UNCOMMITTED : 完全沒有隔離效果，可能讀取其他交易進行中尚未被COMMIT的資料。
            READ COMMITTED : 不允許讀取尚未COMMIT的資料，因為尚未被COMMITTED的資料可能隨時會再變。
            REPEATABLE READ : 在查詢中所讀取的資料會被鎖定，以免被其他使用者更改或刪除，以保證在交易中每次都可以讀到相同的資料。但是，仍然允許其他使用者對資料表的新增資料作業。
            SERIALIZABLE : 在查詢中所讀取的資料會被鎖定，以免被其他使用者更改或刪除，以保證在交易中每次都可以讀到相同的資料。但是，仍然允許其他使用者對資料表的新增資料作業。
        """
        hard_session = engine.Session(bind=engine.db.execution_options(isolation_level='READ COMMITTED'))

        # self.insert_data(engine.session())
        # self.update_data(engine.session())
        def sum_data():
            self.transaction_data(hard_session)

        t1 = threading.Thread(target=sum_data)
        t2 = threading.Thread(target=sum_data)
        # t3 = threading.Thread(target=sum_data)

        t1.start()
        t2.start()
        # t3.start()

        t1.join()
        t2.join()
        # t3.join()

        # self.select_data(engine.session)
        # self.delete_data(engine.session)
        # self.base_use(engine.db)
        # self.session_search(engine.session)
        # self.aliased_search(engine.session)
        # self.query_filter(engine.session)
        # self.many_to_one(engine.session)
        # self.many_to_many(engine.session)
        # self.one_to_many(engine.session)
        # self.one_to_one(engine.session)
        hard_session.close()
        # engine.session.close()
        return "done"
