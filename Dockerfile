# ベースイメージとしてPythonを使用
FROM python:3.10-slim

# 作業ディレクトリを作成
WORKDIR /app

# 依存パッケージのリスト（requirements.txt）をコンテナにコピー
COPY requirements.txt /app/

# 依存パッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコンテナにコピー
COPY . /app

# アプリケーションの起動コマンド（仮のもの）
CMD ["python", "app.py"]
