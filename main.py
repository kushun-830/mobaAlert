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

    debug = False

    def time_import():
        if debug:
            return datetime.datetime(2021,1,27,10,55)  #デバッグ用
        else:
            return datetime.datetime.now()

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
        eventDataSet = {}
        eventName = "インターバル期間"
        isFeverOrRound = ""
    else:
        eventDataSet = eventData.eventData(nowEvent)
        eventName = eventDataSet["eventName"]
        isFeverOrRound = isEventTest.isFeverOrRoundTest(nowTime, eventDataSet)
        nowEvent = {}

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
    timeout_time = 1000 * 10    #10秒
    roundPopup_settings = True
    roundPopup = roundPopup_settings
    roundPopupTime = 10
    isIntervel = False

    if debug:
        diff = 0
    else:
        timeout_time *= 3

    #イベント待ち
    while True:
        if debug:
            diff += 60
        appliEvent, appliValues = window.read(timeout = timeout_time, timeout_key = "timeout")
        print(" イベント:", appliEvent , ", 値:", appliValues)    #デバッグ用

        if appliEvent == "timeout":
            nowTime = time_import()
            if debug:
                nowTime += datetime.timedelta(minutes = diff) #デバッグ用
            updateTime = nowTime.isoformat(timespec = "seconds").replace("T", " ")
            print(nowTime)  # デバッグ用

            if eventDataSet == {} and (int(nowTime.strftime("%H")) < 15 or int(nowTime.strftime("%H")) >= 23):
                window["update"].update("更新：" + updateTime)
                continue
            elif eventDataSet == {}:
                nowEvent = data_import(nowTime)
                eventDataSet = eventData.eventData(nowEvent)
                eventName = eventDataSet["eventName"]
                nowEvent = {}

            if eventDataSet != {}:
                isFeverOrRound = isEventTest.isFeverOrRoundTest(nowTime, eventDataSet)
                window["isFeverOrRound"].set_size(size = (len(isFeverOrRound) * 3, None))
                window["isFeverOrRound"].update(isFeverOrRound)

                if roundPopup and isFeverOrRound != "インターバル":
                    isRoundEnd = isEventTest.isRoundEnd(nowTime, eventDataSet, roundPopupTime)
                    if isRoundEnd:
                        sg.popup("ラウンド終了" + str(roundPopupTime) + "分前です")
                        roundPopup = False

                if isFeverOrRound == "インターバル":
                    roundPopup = roundPopup_settings

                if isEventTest.isEventEnd(nowTime, eventDataSet):
                    eventName = "インターバル期間"
                    eventDataSet = {}
                    roundPopup = roundPopup_settings

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