# coding=utf-8

import unittest
import uiautomator2 as u2
from reco_fail import reco_fail
from reco_success import reco_success
from log import Log
from time import sleep


class MusicRecognizeTest(unittest.TestCase):

    def setUp(self):
        Log.create_log_file()  # 创建日志
        Log.logger.info("Start Recognize music testing")

        self.device = u2.connect("10.242.212.220")  # 与设备端连接
        self.device.healthcheck()  # 设备健康检查，准备工作检查
        Log.logger.info("Device ID is: %s", self.device.serial)

        screen = self.device.info
        if not screen["screenOn"]:  # 屏幕状态：黑屏
            Log.logger.info("Device Status: screen off")
            self.device.unlock()  # 解锁设备
        else:  # 屏幕状态：亮屏
            Log.logger.info("Device Status: screen on")

        self.music = self.device.session("com.netease.cloudmusic")  # 打开网易云音乐
        sleep(10)  # 休眠十秒，保证启动页及广告跳过

        if self.music(text="听歌识曲").exists():
            Log.logger.info("Start to recognize music")
        else:
            up_button = self.music.xpath('//*[@resource-id="com.netease.cloudmusic:id/toolbar"]/android.widget'
                                         '.FrameLayout[1]')
            if up_button.exists:
                up_button.click()
                self.music.xpath('//*[@resource-id="com.netease.cloudmusic:id/mainDrawerTabIndentify"]').click()

    def runTest(self):
        Log.logger.info("Start to recognize music...")
        sleep(20)  # 听歌识曲按钮点入直接开始20s识别
        sn = self.music.xpath('//*[@resource-id="com.netease.cloudmusic:id/songName"]')

        """识别失败重新识别的循环判断体"""
        reco_fail.re_reco(self, sn=sn)

        """"识别成功继续识别的循环判断体"""
        reco_success.co_reco(self, sn=sn)

    def tearDown(self) -> None:
        Log.logger.info("Test End")
        self.device.app_stop("com.netease.cloumusic")  # 关闭网易云音乐


if __name__ == '__main__':
    unittest.main()
