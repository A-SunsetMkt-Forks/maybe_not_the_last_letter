# 用于处理Web资源文件的降低质量
# 在Web输出的game文件夹内执行
# 图片压缩效果不佳
import os

from PIL import Image
from pydub import AudioSegment

# 配置
# 压缩图像
modify_image = False
# 压缩音频
modify_audio = True
# 图片质量
image_quality = 30
# 音频质量
audio_quality = 32000


def reduce_image_quality(path):
    for item in os.listdir(path):
        s = os.path.join(path, item)
        if os.path.isfile(s):
            print(s)
            if s.endswith('.jpg') or s.endswith('.jpeg'):
                try:
                    image = Image.open(s)
                    image.save(s, "JPEG", quality=image_quality)
                except:
                    pass
            if s.endswith('.png'):
                try:
                    image = Image.open(s)
                    image.save(s, "PNG", quality=image_quality)
                except:
                    pass
        elif os.path.isdir(s):
            reduce_image_quality(s)


def reduce_audio_quality(path):
    for item in os.listdir(path):
        s = os.path.join(path, item)
        if os.path.isfile(s):
            print(s)
            if s.endswith('.ogg'):
                try:
                    sound = AudioSegment.from_ogg(s)
                    sound = sound.set_frame_rate(audio_quality)
                    sound.export(s, format="ogg")
                except:
                    pass
            if s.endswith(".mp3"):
                try:
                    sound = AudioSegment.from_mp3(s)
                    sound = sound.set_frame_rate(audio_quality)
                    sound.export(s, format="mp3")
                except:
                    pass
        elif os.path.isdir(s):
            reduce_audio_quality(s)


if __name__ == "__main__":
    # 检查是否在game文件夹内
    if os.getcwd().endswith('game'):
        if modify_image:
            reduce_image_quality("images")
        if modify_audio:
            reduce_audio_quality("audio")
    else:
        print("请在game文件夹内执行")
