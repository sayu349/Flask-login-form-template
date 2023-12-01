from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Flask-SQLAlchemyの生成
db = SQLAlchemy()

# ==================================================
# モデル
# ==================================================

class User(UserMixin, db.Model):
    # テーブル名
    __tablename__ = 'users'
    # ID（PK）
    id = db.Column(db.Integer, primary_key=True)
    # ユーザー名
    username = db.Column(db.String(50), unique=True, nullable=False)
    # パスワード
    password = db.Column(db.String(120), nullable=False)
    # パスワードをハッシュ化して設定する
    def set_password(self, password):
        # generate_password_hash: 引数で取得した平文パスワードをハッシュ化する
        # "user.password"に入力される
        self.password = generate_password_hash(password)
    # 入力したパスワードとハッシュ化されたパスワードの比較
    def check_password(self, password):
        return check_password_hash(self.password, password)