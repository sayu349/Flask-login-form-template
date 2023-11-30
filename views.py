from flask import render_template, redirect, url_for, flash
from app import app
from models import db
from models import db, User
from forms import  LoginForm, SignUpForm
from flask_login import login_user, logout_user, login_required

# ==================================================
# ルーティング
# ==================================================

# ログイン（Form使用）
@app.route("/", methods=["GET", "POST"])
def login():
    # Formインスタンス生成
    form = LoginForm()
    # POSTかつ入力フォーマットに沿っている場合のみ、True
    if form.validate_on_submit():
        # データ入力取得
        username = form.username.data
        password = form.password.data
        # 対象User取得
        user = User.query.filter_by(username=username).first()
        # 認証判定
        if user is not None and user.check_password(password):
            # 成功
            # 引数として渡されたuserオブジェクトを使用して、ユーザーをログイン状態にする
            login_user(user)
            # 画面遷移
            return redirect(url_for("index"))
        # 失敗
        flash("認証不備です")
    # GET時
    # 画面遷移
    return render_template("login_form.html", form=form)

# ログアウト
@app.route("/logout")
@login_required
def logout():
    # 現在ログインしているユーザーをログアウトする
    logout_user()
    # フラッシュメッセージ
    flash("ログアウトしました")
    # 画面遷移
    return redirect(url_for("login"))

# サインアップ（Form使用）
@app.route("/register", methods=["GET", "POST"])
def register():
    # Formインスタンス生成
    form = SignUpForm()
    if form.validate_on_submit():
        # データ入力取得
        username = form.username.data
        password = form.password.data
        # モデルを生成
        user = User(username=username)
        # パスワードハッシュ化
        user.set_password(password)
        # 登録処理
        db.session.add(user)
        db.session.commit()
        # フラッシュメッセージ
        flash("ユーザー登録しました")
        # 画面遷移
        return redirect(url_for("login"))
    # GET時
    # 画面遷移
    return render_template("register_form.html", form=form)

# 一覧
@app.route("/home")
# "login_required"を付けることで、不正なアクセスを防止する
@login_required
def index():
    return render_template("index.html")