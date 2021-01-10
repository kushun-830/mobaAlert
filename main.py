"""
copyright: (c) 2021 by うずらいも
Twitter: shinymas_potato

・このソースコードおよびアプリケーションのライセンスはLGPL3.0です。
　https://www.gnu.org/licenses/lgpl-3.0.html
・このアプリケーションのソースコードはgithubで公開されています。
　https://github.com/kushun-830/mobaAlert


・ライブラリ：requestsは、Apache2.0ライセンスで配布されている製作物です。
　http://www.apache.org/licenses/LICENSE-2.0
　https://requests.readthedocs.io

・ライブラリ：PySimpleGUIは、LGPL3.0ライセンスで配布されている製作物です。
　https://pysimplegui.readthedocs.io/en/latest/
　
・このソースコードおよびアプリケーションでは、デレマスボーダーbot様のAPIを利用しています。
　https://pink-check.school/

この場をお借りして、皆様に感謝申し上げます。
"""

#coding: utf-8
import eventData
import isEventTest
import localSettings
import subPopup #今後実装予定

if __name__ == '__main__':
    import PySimpleGUI as sg
    import requests
    import datetime

    def time_import():
        #nowtime = datetime.datetime(2020,12,26,15,48,40)  #ぷちコレ #デバッグ用
        #nowtime = datetime.datetime(2020,12,31,14,59)  #イベントが存在しない時間 #開始直前 #デバッグ用
        #nowtime = datetime.datetime(2020,12,31,15,48,50)  #ドリフ開催（フィーバー）期間 #デバッグ用
        #nowtime = datetime.datetime(2020,12,31,13,20)  #ドリフ開催（非フィーバー）期間 #デバッグ用
        #nowtime = datetime.datetime(2021,1,10,20,58,50)  #デバッグ用
        #nowtime = datetime.datetime(2021,1,8,20,30)  #イベント終了直前 #デバッグ用
        nowtime = datetime.datetime.now()
        return nowtime #現在時刻を返す

    def data_import(now):
        url = "https://pink-check.school/api/v2/events/?time=" + now.isoformat()
        res = requests.get(url)
        data = res.json()
        if data["totalCount"] == 0:
            return {}
        else:
            return data["content"][0] #イベント情報を返す

    #初期設定のロード
    localSettings = localSettings.loadSettings()

    nowTime = time_import()
    nowEvent = data_import(nowTime)
    if nowEvent == {}:
        eventName = "インターバル期間"
        eventFlag = False
        eventDataSet = {}
        isFeverOrRound = ""
    else:
        eventFlag = True
        eventDataSet = eventData.eventData(nowEvent)
        nowEvent = {}
        eventName = eventDataSet["eventName"]
        isFeverOrRound = isEventTest.isFeverOrRoundTest(nowTime, eventDataSet)

    #レイアウト作成
    layout = \
        [
            #メニューバー
            [sg.MenuBar([["&File", ["&Settings", "---", "&Quit"]]],
                        key = "menu")],

            #レイアウト
            [sg.Text("現在開催中のイベント： ", key = "eventLabel")],
            [sg.Text(eventName, key = "eventName",
                     font = 20, text_color = localSettings["eventColor"], size = (len(eventName) * 3, 1))],
            [sg.Text(isFeverOrRound, key = "isFeverOrRound",
                     font = 20, text_color = localSettings["feverColor"], size = (len(isFeverOrRound) * 3, 1))],
            [sg.Text("更新：" + (nowTime.isoformat(timespec = "seconds")).replace("T", " "), key = "update")]
        ]

    #ウィンドウ表示
    window = sg.Window("モバマスイベントアラート", layout, resizable = True)

    #定数設定
    timeout_time = 1000 * 10 * 3
    roundPopup = True
    roundPopupTime = 10
    #i = 0

    #イベント待ち
    while True:
        #i += 0.5
        appliEvent, appliValues = window.read(timeout = timeout_time, timeout_key = "timeout")
        print(" イベント:", appliEvent , ", 値:", appliValues)    #デバッグ用

        if appliEvent == "timeout":
            nowTime = time_import() #+ datetime.timedelta(minutes = i) #デバッグ用 #iを適当に置けば定数時刻からずらしていける
            updateTime = nowTime.isoformat(timespec = "seconds").replace("T", " ")
            print(nowTime)  # デバッグ用

            if eventFlag == False and (int(nowTime.strftime("%H")) < 15 or int(nowTime.strftime("%H")) >= 23):
                window["update"].update("更新：" + updateTime)
                continue
            elif eventFlag == False:
                eventFlag = True
                nowEvent = data_import(nowTime)
                eventDataSet = eventData.eventData(nowEvent)
                nowEvent = {}
                eventName = eventDataSet["eventName"]

            if eventFlag:
                isFeverOrRound = isEventTest.isFeverOrRoundTest(nowTime, eventDataSet)
                window["isFeverOrRound"].set_size(size = (len(isFeverOrRound) * 3, None))
                window["isFeverOrRound"].update(isFeverOrRound)

                if roundPopup and isFeverOrRound != "インターバル":
                    isRoundEnd = isEventTest.isRoundEnd(nowTime, eventDataSet, roundPopupTime)
                    if isRoundEnd:
                        sg.popup("ラウンド終了" + str(roundPopupTime) + "分前です")
                        roundPopup = False
                elif isFeverOrRound != "インターバル":
                    roundPopup = True

                if isEventTest.isEventEnd(nowTime, eventDataSet):
                    eventName = "インターバル期間"
                    eventDataSet = {}
                    eventFlag = False
                    roundPopup = True

            window["eventName"].set_size(size = (len(eventName) * 3, None))
            window["eventName"].update(eventName)
            window["update"].update("更新：" + updateTime)

        if appliValues != None:
            if appliValues["menu"] == "Settings":
                res_pop = sg.popup("今後実装予定です")

            if appliValues["menu"] == "Quit":
                break

        elif appliEvent == None:
            break

    # 終了処理
    window.close()