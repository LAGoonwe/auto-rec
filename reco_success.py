# coding=utf-8

""""识别成功的循环处理类"""
from time import sleep
from log import Log
import reco_fail


class reco_success:

    # 识别成功的继续识别处理方法
    def co_reco(self, sn):
        try:
            while sn.exists:
                Log.logger.info("Song recognition succeeded!")
                Log.logger.info("The Song's Name is %s", sn.get_text())
                self.music(description="转到上一层级").click()  #
                start_rec = self.music.xpath('//android.widget.TextView[contains(@text, "点击重新识别")]')
                restart_rec = self.music.xpath('//android.widget.TextView[contains(@text, "点击识别音乐")]')
                if start_rec.exists or restart_rec.exists:
                    self.music.xpath('//*[@resource-id="com.netease.cloudmusic:id/waveView"]').click()
                    Log.logger.info("Start to recognize music...")
                    sleep(20)
                    sn = self.music.xpath('//*[@resource-id="com.netease.cloudmusic:id/songName"]')
                    if sn.exists:
                        pass
                    else:
                        reco_fail.reco_fail.re_reco(self, sn=sn)
        except Exception as e:
            Log.logger.info(e)
            exit()
