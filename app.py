# from langchain.llms import OpenAI

# # OpenAI APIキーを設定
# openai_api_key = "DUMMY"

# # LLMのインスタンスを作成
# llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

# # テキスト生成
# response = llm("AIペットSNSのコンセプトを教えてください。")

# print(f"LLMからの応答: {response}")




# import faiss
# import numpy as np

# # FAISSインデックスの作成
# dimension = 5  # ベクトルの次元数
# index = faiss.IndexFlatL2(dimension)  # L2距離でベクトル検索

# # サンプルデータの作成（5次元のベクトル）
# vectors = np.array([[1.0, 2.0, 3.0, 4.0, 5.0],
#                     [5.0, 4.0, 3.0, 2.0, 1.0],
#                     [2.0, 3.0, 4.0, 5.0, 6.0]], dtype='float32')

# # インデックスにデータを追加
# index.add(vectors)

# # 検索するクエリベクトル（5次元）
# query_vector = np.array([[1.0, 2.0, 3.0, 4.0, 5.0]], dtype='float32')

# # 検索の実行（上位2つを取得）
# distances, indices = index.search(query_vector, 2)

# print(f"検索結果のインデックス: {indices}")
# print(f"検索結果の距離: {distances}")




# from langchain.llms import OpenAI

# # OpenAI APIキーを設定
# openai_api_key = "DUMMY"

# # LLMのインスタンスを作成
# llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

# # ユーザーの発言を取得する
# user_input = input("あなた: ")

# # AIペットの応答を生成する
# response = llm(f"ユーザーが言いました: {user_input}. AIペットとして返答してください。")

# # AIペットの応答を表示する
# print(f"AIペット: {response}")




# from langchain.llms import OpenAI

# # OpenAI APIキーを設定
# openai_api_key = "DUMMY"

# # LLMのインスタンスを作成
# llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

# # ユーザーの発言を取得する
# user_input = input("あなた: ")

# # 応答しないキーワードのリスト
# ignore_keywords = ["独り言", "考え中", "つぶやき"]

# # 応答するかどうかを判断
# should_respond = not any(keyword in user_input for keyword in ignore_keywords)

# if should_respond:
#     # AIペットの応答を生成する
#     response = llm(f"ユーザーが言いました: {user_input}. AIペットとして返答してください。")
#     print(f"AIペット: {response}")
# else:
#     print("AIペットは介入しませんでした。")




# from langchain.llms import OpenAI
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import ConversationChain

# # OpenAI APIキーを設定
# openai_api_key = "DUMMY"

# # LLMのインスタンスを作成
# llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

# # 会話の履歴を保持するためのメモリ
# memory = ConversationBufferMemory()

# # 会話チェーンを作成
# conversation = ConversationChain(
#     llm=llm,
#     memory=memory
# )

# while True:
#     # ユーザーの発言を取得
#     user_input = input("あなた: ")

#     # "終了" というキーワードで会話を終了
#     if user_input.lower() == "終了":
#         print("会話を終了します。")
#         break

#     # AIペットの応答を生成
#     response = conversation.run(input=user_input)

#     # AIペットの応答を表示
#     print(f"AIペット: {response}")





# from flask import Flask, request, jsonify, render_template
# from langchain.llms import OpenAI
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import ConversationChain
# import os

# app = Flask(__name__, template_folder='.')

# # OpenAI APIキーを設定
# openai_api_key = "DUMMY"

# # LLMのインスタンスを作成
# llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

# # 会話の履歴を保持するためのメモリ
# memory = ConversationBufferMemory()

# # 会話チェーンを作成
# conversation = ConversationChain(
#     llm=llm,
#     memory=memory
# )

# # フロントエンドのindex.htmlを返すルート
# @app.route('/')
# def index():
#     return render_template('index.html')

# # チャットAPI
# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.json
#     user_input = data.get("user_input")
#     response = conversation.run(input=user_input)
#     return jsonify({"response": response})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)





# from flask import Flask, request, jsonify, render_template
# # from langchain.llms import OpenAI
# from langchain_community.chat_models import ChatOpenAI
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import ConversationChain
# import os

# app = Flask(__name__, template_folder='.')

# # OpenAI APIキーを設定
# openai_api_key = "DUMMY"

# # LLMのインスタンスを作成
# # llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
# llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7, openai_api_key=openai_api_key)

# # 会話の履歴を保持するためのメモリ
# memory = ConversationBufferMemory()

# # 会話チェーンを作成
# conversation = ConversationChain(
#     llm=llm,
#     memory=memory
# )

# # フロントエンドのindex.htmlを返すルート
# @app.route('/')
# def index():
#     return render_template('index.html')

# # チャットAPI
# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.json
#     user_input = data.get("user_input")
#     response = conversation.run(input=user_input)
#     return jsonify({"response": response})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)










"""
概要    : AI×SNSのチャット画面のプロトタイプ
使用方法:（例）
    * DockerDesktop起動
    * PowerShell管理者起動して下記コマンド
	*   cd C:\html\PROJECT\ai-sns-demo
	*   docker-compose up --build
	* ブラウザで下記URL
	*   http://localhost:5000/
メモ:
    * 動的なAIキャラ設定追加
	* デバッグ追加
	* ユーザIDごとのAI会話チェーン
	* GitHub管理開始
"""
import json
from flask import Flask, flash, get_flashed_messages, request, jsonify, session, redirect, url_for, render_template
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
from langchain.chains import ConversationChain
from langchain.callbacks import get_openai_callback
import os

# フレームワークはFlaskを使用
app = Flask(__name__, template_folder='.')

# セッション生成用暗号化キー
app.secret_key = os.urandom(24)  # ランダムに生成されたバイト列を使用

# OpenAI API設定
openai_api_key = os.getenv("OPENAI_API_KEY", "dummy_key")   # OpenAI APIキー（デフォルトOPENAI_API_KEYは、docker-compose.ymlで指定）
openai_model_name = "gpt-4o"                                # OpenAI モデル
openai_temperature = 0.2                                    # OpenAI ランダム性（0～2.0。高いほどランダムな回答となる）

# ユーザマスタ（仮）
# （ユーザID:ユーザ名）
user_mst = {
    "0001":"加藤",
    "0002":"武田",
    "0003":"上杉"
}

# AIユニット特性（初期値）
ai_unit_traits = {
    "tone": "丁寧語",
    "personality": "優しい、丁寧、誠実",
    "humor": "なし",
    "learning_support": "ON",  # 学習サポート機能のオン/オフ
    "other_instructions": ""  # その他の指示
}

# グローバルなデバッグ情報
debug_info = {}

# LangChainのLLMインスタンスを作成
llm = ChatOpenAI(model_name=openai_model_name, temperature=openai_temperature, openai_api_key=openai_api_key)

# # 会話の履歴を保持するためのメモリ
# memory = ConversationBufferMemory()
# # 会話チェーンを作成
# conversation = ConversationChain(
#     llm=llm,
#     memory=memory
# )

# 各ユーザごとの会話履歴とチェーンを管理するための辞書
user_chains = {}


#==================================================================================================
# 関数定義
#==================================================================================================

# 各ユーザごとのConversationChainインスタンスを取得
def get_user_chain(user_id):
    if user_id not in user_chains:
        # 初回ユーザは新しいConversationBufferMemoryを作成（※会話履歴を保持するメモリ）
        memory = ConversationBufferMemory()
        # 会話チェーンを作成
        conversation = ConversationChain(
            llm=llm,
            memory=memory
        )
        # チェーン管理辞書に保持
        user_chains[user_id] = conversation
    return user_chains[user_id]

# デバッグ情報 追加
def add_debug(key, value):
    global debug_info
    debug_info[key] = value

# デバッグ情報 全リセット
def reset_debug():
    global debug_info
    debug_info = {}

# デバッグ情報 取得
def get_debug():
    return debug_info


#==================================================================================================
# ルーティング処理
#==================================================================================================

# フロントエンドのindex.htmlを返すルート
@app.route('/')
def index():
    user_id   = session.get('user_id', None)
    user_name = session.get('user_name', None)
    
    if user_id and user_name:
        return render_template('index.html', user_id=user_id, user_name=user_name)
    else:
        # ログインしていない場合はログイン画面へリダイレクト
        return render_template('login.html')

# ログイン画面の表示
@app.route('/login', methods=['GET'])
def login_page():
    # フラッシュメッセージを取得
    flash_messages = get_flashed_messages(with_categories=True)
    return render_template('login.html', flash_messages=flash_messages)

# ログイン処理
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user_id = data.get('user_id')

    # ユーザIDがユーザマスタに存在するか確認
    if user_id in user_mst:
        # 「ユーザID」と「名前」をセッションに保存
        session['user_id'] = user_id
        session['user_name'] = user_mst[user_id]
        return jsonify({"success": True})
    else:
        # エラーメッセージとともにログイン画面に戻す
        # return render_template('login.html', error="ユーザIDが正しくありません。")
        return jsonify({"success": False, "error": "※ユーザID、または、パスワードが正しくありません"})

# ログアウト処理
@app.route('/logout')
def logout():
    session.clear()
    flash("※ログアウトしました", "msg")  # メッセージをフラッシュ
    return redirect(url_for('login'))

# チャットAPI
@app.route('/chat', methods=['POST'])
def chat():
    reset_debug()  # リクエストごとにデバッグ情報をリセット

    user_id = session.get('user_id', None)
    add_debug("user_id", user_id)
    
    if user_id is None:
        # ログインしていない場合はエラー
        return jsonify({"error": "ログインしてください"}), 403

    data = request.json
    user_input = data.get("user_input")
    
	# クライアントから送信されたAIキャラ設定を取得し、デフォルト値とマージ
    ai_settings = data.get("ai_settings", {})
    
    # デフォルトのAIユニット特性を使用し、リクエストで送られてこなかった項目はデフォルトを維持
    tone = ai_settings.get("tone", ai_unit_traits["tone"])
    personality = ai_settings.get("personality", ai_unit_traits["personality"])
    humor = ai_settings.get("humor", ai_unit_traits["humor"])
    learning_support = ai_settings.get("learning_support", ai_unit_traits["learning_support"])
    other_instructions = ai_settings.get("other_instructions", ai_unit_traits["other_instructions"])

	# プロンプトテンプレートを動的に生成
    prompt_template = f"""
    あなたはユーザのサポートをするAIユニットです。過去に指示したあなたの特性は一度すべて忘れて、これからは以下の特性に従って、ユーザーに返答してください。
    - 口調: {tone}
    - 性格: {personality}
    - ユーモア: {humor}
    - 学習サポート機能: {learning_support}

    その他の指示: {other_instructions}
	*AIユニット自身は自分の特性については一切発言してはいけません
	*チャットなのであまり長い文章にならないように注意してください
	*回答が500文字よりも長くなる場合のみ、一度途中までを回答して、その場合は続きを回答するか否かをユーザに確認してください
	*ユーザーが「はい」「いいえ」「続き」「お願い」「もっと」「詳しく教えて」のような、会話の文脈が想定されるような言い方を最後の文章で発言した場合は、過去の会話履歴を参照して、適切な回答をするようにしてください。

    ユーザーの発言に基づいて返答してください: {user_input}
    """

    # ユーザIDに対応した会話チェーンを取得
    conversation = get_user_chain(user_id)

	# ConversationChainを使用して、履歴とカスタムプロンプトを反映
	# [MEMO:]★★★ただし、このやり方だと、AIユニットへの性格指示なども毎回発言の内容をmemoryに記憶してしまう。本当は、memoryには、user_inputだけを記憶していきたいんだけど。（あるいはAIユニットの性格記憶は初回のみ）
    # response = conversation.run(input=prompt_template)
    # トークン使用量をトラッキングするためにコールバックを使用
    with get_openai_callback() as cb:
        response = conversation.run(input=prompt_template)
        # トークン数に関するデバッグ情報を追加
        add_debug("total_tokens（総トークン数）", cb.total_tokens)
        add_debug("prompt_tokens（送信プロンプトトークン数）", cb.prompt_tokens)
        add_debug("completion_tokens（生成回答トークン数）", cb.completion_tokens)
        add_debug("total_cost（総コスト＄）", cb.total_cost)

    # # 応答全体をデバッグ情報として保存
    # add_debug("response_full", json.dumps(response, indent=2, ensure_ascii=False))

    # # トークン使用量を取得 (OpenAI APIのレスポンスに含まれている場合)
    # if hasattr(response, 'usage'):
    #     token_usage = response.usage
    #     add_debug("prompt_tokens", token_usage['prompt_tokens'])
    #     add_debug("completion_tokens", token_usage['completion_tokens'])
    #     add_debug("total_tokens", token_usage['total_tokens'])

	# デバッグ情報（※順番は保証されない）
    add_debug("process_id", os.getpid())    # プロセスID
    # add_debug("memory", str(memory))
    add_debug("memory", str(conversation.memory))
    add_debug("prompt_template", prompt_template)
    add_debug("user_input", user_input)
    add_debug("session", dict(session))

    return jsonify({
        "response": response,
        "debug_info": get_debug()  # 全デバッグ情報も返す
    })
#   return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
