from flask import Flask
from flask_migrate import Migrate
from models import db, User
from flask_login import LoginManager

# ==================================================
# Flask
# ==================================================
app = Flask(__name__)
# 設定ファイル読み込み
app.config.from_object("config.Config")
# dbとFlaskとの紐づけ
db.init_app(app)
# マイグレーションとの紐づけ（Flaskとdb）
migrate = Migrate(app, db)

# LoginManagerインスタンス
login_manager = LoginManager()
# LoginManagerとFlaskとの紐づけ
login_manager.init_app(app)
# ログインが必要なページにアクセスしようとしたときに表示されるメッセージを変更
login_manager.login_message = "認証していません：ログインしてください"
# 未認証のユーザーがアクセスしようとした際に
# リダイレクトされる関数名を設定する
login_manager.login_view = "login"

# 入力されたuser_idを元に、データベースから探し出す
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# viewsのインポート
from views import *

# ==================================================
# 実行
# ==================================================
if __name__ == "__main__":
    app.run()