import pyupbit

access = "ric34KuOgvz8q2mcCsScBtsyRgRcWHwQ7ZEsgYT0"          # 본인 값으로 변경
secret = "CTrlrxSQpMoYxx4xm2OixOGPWPHIgAHVsDUf8BGH"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회