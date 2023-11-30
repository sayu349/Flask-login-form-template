# Flask-login-form-tempalte
## What is this?
- Flaskにおける、ログインフォームのテンプレートになります。
- ログインしなければ、サイト上の他のURLにアクセスできないような仕組みを作成できます。
    - 極めてセキュアで実用的！(と思いませんか…？)

## About file structures
### html files
- login_form.html
    - ログイン用テンプレート
- register_form.html
    - サインアップ用テンプレート
- base.html
    - ログアウトへのリンクを表示する
### Python files
- models.py
    - 認証用のモデル
- forms.py
    - ログイン用・サインアップ用フォームの作成
- app.py
    - 実行ファイル
- views.py
    - ログインが必要なビューの保護を行うファイル