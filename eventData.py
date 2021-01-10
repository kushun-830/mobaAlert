import datetime

def eventData(nowEvent):
    eventID = nowEvent["eventTypeId"]
    eventName = nowEvent["eventTypeName"]
    startDay = datetime.datetime.fromisoformat(nowEvent["detail"][0]["beginDateTime"]).date()
    endDay = datetime.datetime.fromisoformat(nowEvent["detail"][0]["endDateTime"]).date()
    eventDataSet = \
        {
            "eventTypeId": eventID,
            "eventName": eventName,
            "startDay": startDay,
            "endDay": endDay,
            "is_round":
                [{
                    "round_first": [{"0": "15-24"}],
                    "round_ord": [{"0": "00-21", "1": "22-24"}],
                    "round_last": [{"0": "00-23"}]
                }],
            "is_round_only" : False
        }

    if eventID == 1 or eventID == 7 or eventID == 8 or eventID == 11 or eventID == 12 or eventID == 15 or eventID == 17:
        #時間によるフィーバーが無いイベント
        #専用アイテムが存在して、20分に1回、6まで回復するイベント
        #ツアー、アイチャレ、アイロワ
        updateData = \
            {
                "recoveryTime" : 120
            }

    elif eventID == 3:
        #ドリフ
        updateData = \
            {
                "recoveryTime": 120,
                "is_fever" :
                    [{
                        "fever_first": [{"0": "15-16", "1": "19-21", "2": "22-24"}],
                        "fever_ord": [{"0": "07-09", "1": "12-13", "2": "19-21"}],
                        "fever_last": [{"0": "07-09", "1": "12-13", "2": "18-19", "3": "21-23"}]
                    }]
             }

    elif eventID == 5:
        #ぷちコレ
        updateData = \
            {
                "is_round" :
                    [{
                        "round_first": [{"0": "15-16", "1": "19-20", "2": "21-23"}],
                        "round_ord": [{"0": "12-13", "1": "19-20", "2": "21-23"}],
                        "round_last": [{"0": "12-13", "1": "19-20", "2": "21-23"}]
                    }],
                "is_round_only" : True

            }

    elif eventID == 6 or eventID == 10:
        #プロフェス
        updateData = \
            {
                "is_round":
                    [{
                        "round_first": [{"0" : "15-17", "1" : "20-22"}],
                        "round_ord": [{"0" : "12-13", "1" : "17-19", "2" : "21-23"}],
                        "round_last": [{"0" : "20-23"}]
                    }],
                "is_round_only" : True

            }

    elif eventID == 16:
        #JAM
        updateData = \
            {
                "recoveryTime": 120,
                "is_round":
                    [{
                        "round_first": [{"0": "15-24"}],
                        "round_ord": [{"0": "00-24"}],
                        "round_last": [{"0": "00-23"}]
                    }]

            }
    else:
        #アイプロと非対応のイベント（テンプレを更新する必要がないイベント）
        updateData = {}

    eventDataSet.update(updateData)

    return eventDataSet



#eventID
#ここから
#1: ツアー
#2: アイプロ
#3: ドリフ
#4: アイバラ
#5: ぷちコレ
#6: プロフェス
#7: アイチャレ
#8: アイロワ
#9: TBS
#10: プロフェスS
#11: アニバアイプロ
#12: ツアーカーニバル
#13: TBS オールスターSP
#14: 復刻アイプロ
#15: 復刻アイチャレ
#16: JAM
#17: 復刻ツアーカーニバル
#ここまで