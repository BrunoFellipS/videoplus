from mhyt import yt_download


class DowloadVideo:
    def __init__(self, url, filename):
        self.url = url
        self.file_name = filename

    def dowload_mp4(self):
        yt_download(self.url, f"{self.file_name}.mp4")

    def dowload_mp3(self):
        try:
            yt_download(self.url, f"{self.file_name}.mp3", ismusic=True, codec=".mp3")
            result = "Arquivo baixado com sucesso!"
            return result

        except:
            result = "Arquivo baixado com sucesso!"
            return result


if __name__ == "__main__":
    dv = DowloadVideo(r"https://www.youtube.com/watch?v=lhkz7lucBBo", "boa-noite-bruno")
    dv.dowload_mp3()
