# mobaAlert

# 概要
mobaAlert　Version 0.3.1  
最終更新：2021/01/28  
  
お試しで作ったデスクトップアプリです。  
モバマスのイベントラウンド終了前にポップアップして、ラウンド専用ドリンクの飲み忘れなどを低減します。　　
モバマスから逃げるな
  
  
# 使い方  
コードに興味が無い方は、mobaAlert_(version).zipのみダウンロードして解凍してください。  
解凍後フォルダ内のmobaAlert_(version).exeをダブルクリックします。  
起動しっぱなしにしておけば勝手に動きます。  
（個人的にはスタートアップアプリ化をおすすめします（アプリをつけ忘れたら元も子も無いので））  
  
# 機能
- 現在開催中のイベントの種類を表示します。  
- 現在のイベント状況（ラウンド開催中、フィーバー中（ドリームライブフェスティバル）、インターバル期間）を表示します。  
- ラウンド終了10分前に、「ラウンド終了10分前です。」とポップアップします。  
- 以上の機能が30秒ごとに実行されます（アプリの状態が30秒ごとに更新されます）。
  
# 今後のアップデート予定  
上から順に優先度が高いです  
- ポップアップの設定をユーザー側でいじれるようにする（Settingsの拡張） 
- カレンダーを実装して、走りたい日時などをあらかじめ設定できるようにする  
- イベント専用スタミナ（APとか）の管理ができるような機能？  
- Twitterでのリマインドとか……できたら……  
  
以下は妄想です  
- 実行ファイルのサイズがやけに大きくて起動が遅いことの改善  
- 常駐アプリ化  
#多分言語から変えた方が早そうです  
  
# 備考
- 今後の機能拡張に向けて、Settingsがあります。  
そのため、このアプリケーションと同じディレクトリに「Settings.ini」が（存在しない場合）作成されます。
- 任意の環境での動作を保証するものではありません。　　  
- アプリ作成の練習を兼ねているため、何があってもゆるして……  
  
# 更新履歴
- 2021/01/10　Version 0.1  
試しにリリース  
- 2021/01/10　Version 0.2  
21~22時のインターバルにポップアップが出てしまう不具合を修正  
- 2021/01/11 Version 0.2.1  
修正できていなかったため再修正  
- 2021/01/28　Version 0.3  
プロダクションマッチフェスティバルにおいて、その日の1つ目のラウンドでしかポップアップしてくれない不具合を修正  
- 2021/01/28　Version0.3.1  
ポップアップがウィンドウ最前面に表示されるように変更　※今後のSettings実装で選択できるようにする予定  
デフォルトの表示サイズを縮小  
  
---
copyright: (c) 2021 by うずらいも  
Twitter: shinymas_potato  
  
・このソースコードおよびアプリケーションのライセンスはLGPL3.0です。  
　https://www.gnu.org/licenses/lgpl-3.0.html   
  
  
・ライブラリ：requestsは、Apache2.0ライセンスで配布されている製作物です。  
　http://www.apache.org/licenses/LICENSE-2.0  
　https://requests.readthedocs.io  
  
・ライブラリ：PySimpleGUIは、LGPL3.0ライセンスで配布されている製作物です。  
　https://pysimplegui.readthedocs.io/en/latest/  
　  
・このソースコードおよびアプリケーションでは、デレマスボーダーbot様のAPIを利用しています。  
　https://pink-check.school/  
  
この場をお借りして、皆様に感謝申し上げます。
