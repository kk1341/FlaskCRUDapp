from flask import Flask


# create_app関数を作成する
# これを作ることで、簡単に開発環境やステージング環境、本番環境など環境を切り替えることができる
# ユニットテストがしやすくなるというメリットがある
def create_app():
    # Flaskインスタンス生成
    app = Flask(__name__)

    # crudパッケージからviewsをimportする
    from apps.crud import views as crud_views

    # register_blueprintを使いviewsのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app
