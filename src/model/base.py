# coding: utf-8
"""
基础数据表
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from hmac import compare_digest

from werkzeug.security import generate_password_hash, check_password_hash

from .. import db
from ..tool import get_age


class AdminUser(db.Model):
    """管理员用户表"""
    __tablename__ = "admin_user"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, comment="ID")
    account = db.Column(db.String(32), unique=True, nullable=False, server_default="", comment="登录账号")
    _password = db.Column("password", db.String(256), nullable=False, server_default="", comment="登录密码")
    nickname = db.Column(db.String(32), nullable=False, server_default="", comment="昵称")
    avatar_url = db.Column(db.String(256), nullable=False, server_default="", comment="头像URL")
    mail = db.Column(db.String(32), nullable=False, server_default="", comment="邮箱")
    gender = db.Column(db.SmallInteger, nullable=False, server_default="0", comment="性别，0未知，1男性，2女性")
    remark = db.Column(db.String(256), nullable=False, server_default="", comment="备注")
    status = db.Column(db.SmallInteger, nullable=False, server_default="1", comment="状态，0无效，1有效")
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP"),
                            comment="创建时间")
    update_time = db.Column(db.DateTime, nullable=False,
                            server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment="更新时间")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_pwd):
        self._password = generate_password_hash(raw_pwd)

    def check_password(self, password, is_hash=False):
        if is_hash:
            return compare_digest(self.password, password)
        return check_password_hash(self.password, password)

    @property
    def age(self):
        return get_age(self.birthday)
