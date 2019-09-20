# coding=utf-8

""""识别失败循环处理类"""
from time import sleep
from reco_success import reco_success

from log import Log


class reco_fail:
    def re_reco(self, sn):
        while not sn.exists:
            # 如果页面中存在听歌识曲字样，说明未识别到结果且还在听歌识曲界面中，输出调试信息，开始识别歌曲
            if self.music(text="听歌识曲").exists():
                start_rec = self.music.xpath('//android.widget.TextView[contains(@text, "点击重新识别")]')
                restart_rec = self.music.xpath('//android.widget.TextView[contains(@text, "点击识别音乐")]')
                if start_rec.exists or restart_rec.exists:
                    self.music.xpath('//*[@resource-id="com.netease.cloudmusic:id/waveView"]').click()
                    Log.logger.info("Song not recognized, re-recognizing...")
                    sleep(20)
                    sn = self.music.xpath('//*[@resource-id="com.netease.cloudmusic:id/songName"]')
            else:  # 当前页面不是听歌识曲页面，则重新进入
                up_button = self.music.xpath('//*[@resource-id="com.netease.cloudmusic:id/toolbar"]/android.widget'
                                             '.FrameLayout[1]')
                if up_button.exists:
                    up_button.click()
                    self.music.xpath('//*[@resource-id="com.netease.cloudmusic:id/mainDrawerTabIndentify"]').click()
                    Log.logger.info("Song not recognized, re-recognizing...")
                    sleep(20)
                    sn = self.music.xpath('//*[@resource-id="com.netease.cloudmusic:id/songName"]')

            # 如果歌曲再次识别不成功
            if not sn.exists:
                pass
            # 如果识别成功了，则进入成功循环判断体
            else:
                reco_success.co_reco(self, sn=sn)
