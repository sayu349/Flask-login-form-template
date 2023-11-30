from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError
from models import User

# ログイン用入力クラス
class LoginForm(FlaskForm):
    username = StringField('ユーザー名：',
                           validators=[DataRequired('ユーザー名は必須入力です')])
    # パスワード：パスワード入力
    password = PasswordField('パスワード: ',
                             validators=[Length(4, 10,
                                    'パスワードの長さは4文字以上10文字以内です')])
    # ボタン
    submit = SubmitField('ログイン')

    # カスタムバリデータ
    # 英数字と記号が含まれているかチェックする
    def validate_password(self, password):
        """
        ※: any()はTrue or Falseを返す
        条件1 :英字が少なくとも1文字含まれているか
        条件2: 数字が少なくとも1文字含まれているか
        条件3: 特定の記号が少なくとも1文字含まれているか
        """
        if not (any(c.isalpha() for c in password.data) and \
            any(c.isdigit() for c in password.data) and \
            any(c in '!@#$%^&*()' for c in password.data)):
            raise ValidationError('パスワードには【英数字と記号：!@#$%^&*()】を含める必要があります')

# サインアップ用入力クラス
class SignUpForm(LoginForm):
    # ボタン
    submit = SubmitField('サインアップ')

    # カスタムバリデータ
    def validate_username(self, username):
        # ユーザー名が既に使用されていないか
        user = User.query.filter_by(username=username.data).first()
        # userがNoneでない場合に実行される
        if user:
            raise ValidationError('そのユーザー名は既に使用されています')