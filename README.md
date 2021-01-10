# mobaAlert
mobaAlert

モバマスイベントアラート　Version 0.1


お試しで作ったデスクトップアプリです。
モバマスから逃げるな


●使い方
　mobaAlert.exeをダブルクリックします。
　起動しっぱなしにしておけば勝手に動きます。


●機能
・現在開催中のイベントの種類を表示します。

・現在のイベント状況（ラウンド開催中、フィーバー中（ドリームライブフェスティバル）、インターバル期間）を表示します。

・ラウンド終了10分前に、「ラウンド終了10分前です。」とポップアップします。

・以上の機能が30秒ごとに実行されます（アプリの状態が30秒ごとに更新されます）。


●今後のアップデート予定
・カレンダーを実装して、走りたい日時などをあらかじめ設定できるようにする
・ポップアップの設定をユーザー側でいじれるようにする（Settingsの拡張）
・Twitterでのリマインドとか……できたら……


●備考
・今後の機能拡張に向けて、Settingsがあります。
　そのため、このアプリケーションと同じディレクトリに「Settings.ini」が（存在しない場合）作成されます。
・変な挙動したら教えて下さい。アプリ作成の練習とか兼ねてるのでゆるして……


●更新履歴
・2021/01/10　Version 0.1
　Version 0.1　として友人にリリース



"""

copyright: (c) 2021 by うずらいも
mail: worldpm@hotmail.co.jp
Twitter: shinymas_potato

・このソースコードおよびアプリケーションのライセンスはLGPL3.0です。
　https://www.gnu.org/licenses/lgpl-3.0.html
・このアプリケーションのソースコードはgithub（かどこか）で公開される予定です。


・ライブラリ：requestsは、Apache2.0ライセンスで配布されている製作物です。
　http://www.apache.org/licenses/LICENSE-2.0
　https://requests.readthedocs.io

・ライブラリ：PySimpleGUIは、LGPL3.0ライセンスで配布されている製作物です。
　https://pysimplegui.readthedocs.io/en/latest/
　
・このソースコードおよびアプリケーションでは、デレマスボーダーbot様のAPIを利用しています。
　https://pink-check.school/

この場をお借りして、皆様に感謝申し上げます。
　
"""
