import yt_dlp
import os

def download_video(url):
    try:
        # Установим параметры для скачивания видео с субтитрами
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Выбор лучшего видео и аудио
            'outtmpl': '%(title)s.%(ext)s',  # Имя файла
            'retries': 10,  # Повторные попытки при неудаче
            'socket_timeout': 120,  # Увеличенный таймаут
            'writesubtitles': True,  # Скачивание субтитров
            'subtitleslangs': ['en'],  # Английские субтитры
            'embedsubtitles': True,  # Внедрение субтитров в видео
            'merge_output_format': 'mp4',  # Объединение в MP4
            'postprocessors': [{
                'key': 'FFmpegEmbedSubtitle',  # Внедрение субтитров
            }]
        }
        
        # Скачиваем видео
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = ydl.prepare_filename(info_dict)
            video_title = video_title.rsplit('.', 1)[0] + '.mp4'  # Присваиваем имя файла с расширением .mp4

        print(f"Видео '{video_title}' успешно скачано!")

        # Команда для передачи видео по SSH
        ssh_command = f"scp '{video_title}' username@your_ip:/your/directory/"
        os.system(ssh_command)
        print(f"Видео передано по SSH на удаленный компьютер.")
    
    except Exception as e:
        print(f"Ошибка при скачивании: {e}")

if __name__ == "__main__":
    video_url = input("Введите URL видео YouTube: ")
    download_video(video_url)
