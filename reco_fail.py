# coding=utf-8

""""识别失败循环处理类"""
from time import sleep
from reco_success import reco_success

from log import Log


class reco_fail:
    def re_reco(self, sn):
        try:
            while not sn.exists:
                # 如果页面中存在听歌识曲字样，说明未识别到结果且还在听歌识曲界面中
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

                if not sn.exists:
                    pass
                else:
                    reco_success.co_reco(self, sn=sn)
        except Exception as e:
            Log.logger.info(e)
            exit()
