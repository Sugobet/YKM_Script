# -*- encoding:utf-8 -*-
import os
import uiautomator2
# import cv2


ip = "192.168.1.7"


if __name__ == "__main__":
    # os.system("adb tcpip 5555")
    os.system(f"adb connect {ip}")
    try:
        r = uiautomator2.connect()
    except Exception as err:
        print("\a", "uiautomator2连接失败，请检查adb是否连接正常(wifi/usb)", "\n", f"error:{err}")
        os._exit(-1)

    os.system("adb shell am start -n com.tencent.mm/.ui.LauncherUI")    # 启动微信进入主界面
    print("进入微信")
    # in wechat, click:我-收藏-粤康码
    r.xpath('//*[@resource-id="com.tencent.mm:id/czl"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click_exists()
    print("我")
    r.xpath('//*[@text="收藏"]').click_exists()
    print("收藏")
    r.xpath('//*[@resource-id="com.tencent.mm:id/bwt"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').click()
    print("粤康码")

    r.xpath('//*[@resource-id="com.tencent.mm:id/doz"]').click_exists()    # 登录验证->确定
    print("登录验证确定")
    # 同意协议
    r.xpath('//*[@text="我同意广东省政务服务数据管理局使用我所提交的信息用于快捷登录。查看"]').click_exists()
    print("同意协议")
    r.xpath('//*[@text="开始登录"]').click()     # 开始登录
    print("开始登录")
    r.xpath('//*[@resource-id="com.tencent.mm:id/cny"]').click_exists()    # 已阅读并同意
    r.xpath('//*[@resource-id="com.tencent.mm:id/f0b"]').click()    # 同意授权
    print("已阅读并登录")
    # 输入密码
    print("输入密码")
    r.click(0.834, 0.739)
    r.click(0.497, 0.739)
    r.click(0.161, 0.741)
    r.click(0.834, 0.739)
    r.click(0.493, 0.81)
    r.click(0.493, 0.81)
    # 本人填报
    r.xpath('//android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]').click_exists()
    print("本人填报")
    # 直接提交
    r.xpath('//*[@resource-id="com.tencent.mm:id/doz"]').click_exists()
    print("直接提交")
    # 关闭小程序
    r.xpath('//*[@resource-id="com.tencent.mm:id/d8"]').click_exists()
    os.system("adb shell input keyevent 3")     # 返回桌面
    print("关闭小程序并返回桌面")
    input("\a程序执行完毕, ENTER键退出")
