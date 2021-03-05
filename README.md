![stat](https://img.shields.io/github/downloads/CyberRex0/discord-mcbe-statbot/total)
![ver](https://img.shields.io/github/manifest-json/v/CyberRex0/discord-mcbe-statbot)
# discord-mcbe-statbot
Minecraft Bedrock Editionのサーバー情報をDiscordに表示するボットです

## 使い方
### ボットの準備
まずボットを使うためにはDiscordボットを作成する必要があります。

[こちらのページ](https://qiita.com/1ntegrale9/items/cb285053f2fa5d0cccdf)を参考にアカウントを作成してください。

その後トークンをconfig.pyの`bot_token`に入れます。

### Pythonのインストール
このボットはPythonで書かれているので、実行する環境にPythonをインストールしなければなりません。

#### Windows
[こちら](https://qiita.com/dr3mms/items/13e0977dba645ee667a8)を参考にバージョン3.8.5以降のものをインストールしてください。

#### Linux
Ubuntu/Debianの場合 `sudo apt update && sudo apt install python3.8 python3-pip`

### ライブラリのインストール
このボットが動作するのに必要なライブラリをインストールします。

Pythonのパッケージマネージャ「pip」を使います。

`python3 -m pip install discord.py mcipc`

と実行するだけでOKです。

### 設定ファイルを書く
ボットが動作するためには設定ファイルを書く必要があります。

config.pyがあるので、それを開いて書いてあるコメントに従って記述してください。

### ボットの起動
`python3 bot.py`

でOKです。
