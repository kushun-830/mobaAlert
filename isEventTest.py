import datetime

def isEventEnd(nowTime, eventDataSet):
    now_date = nowTime.date()
    now_hour = int(nowTime.strftime("%H"))
    if now_date == eventDataSet["endDay"] and now_hour >= 23:
        return True
    else:
        return False

def isRoundDay(now_date, eventDataSet):
    if now_date == eventDataSet["startDay"]:
        roundDay = "round_first"
    elif now_date == eventDataSet["endDay"]:
        roundDay = "round_last"
    else:
        roundDay = "round_ord"

    return roundDay

def isFeverOrRoundTest(nowTime, eventDataSet):
    now_date = nowTime.date()
    now_hour = int(nowTime.strftime("%H"))
    isFeverOrRound = ""

    roundDay = isRoundDay(now_date, eventDataSet)

    round_dict = eventDataSet["is_round"][0][roundDay][0]

    for i in range(len(round_dict)):
        round_start = int(round_dict[str(i)][:2])
        round_end = int(round_dict[str(i)][-2:])
        if round_start <= now_hour < round_end:
            isFeverOrRound = "ラウンド開催中！"
            if eventDataSet["is_round_only"]:
                isFeverOrRound += "！！"
            break
    if isFeverOrRound == "":
        isFeverOrRound = "インターバル"

    if "is_fever" in eventDataSet:
        if now_date == eventDataSet["startDay"]:
            feverDay = "fever_first"
        elif now_date == eventDataSet["endDay"]:
            feverDay = "fever_last"
        else:
            feverDay = "fever_ord"

        fever_dict = eventDataSet["is_fever"][0][feverDay][0]

        for i in range(len(fever_dict)):
            fever_start = int(fever_dict[str(i)][:2])
            fever_end = int(fever_dict[str(i)][-2:])
            if fever_start <= now_hour < fever_end:
                isFeverOrRound = "フィーバータイム！！！"
                break

    return isFeverOrRound

def isRoundEnd(nowTime, eventDataSet, roundPopupTime):
    if eventDataSet["eventTypeId"] == 16:   #JAM（ラウンド概念が無い）
        return False

    now_date = nowTime.date()
    judgeTime = int((nowTime + datetime.timedelta(minutes = roundPopupTime)).strftime("%H"))
    roundDay = isRoundDay(now_date, eventDataSet)
    round_dict = eventDataSet["is_round"][0][roundDay][0]
    isPopTime = False

    if eventDataSet["is_round_only"] or (roundDay != "round_first"):
        for i in range(len(round_dict)):
            round_end = int(round_dict[str(i)][-2:])
            if judgeTime == round_end:
                isPopTime = True
                break

    return isPopTime
