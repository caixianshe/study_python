# 案例 输入身高 判断是否需要买票
money_tip = 10
print("欢迎来到动物园")
stature = int(input("请输入你的身高，单位厘米"))
if stature > 120:
    print(f"您的身高超过120厘米需要购票{money_tip}元")
else:
    print("您可以免费畅游")
