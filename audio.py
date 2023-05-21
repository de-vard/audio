from moviepy.editor import concatenate_audioclips, AudioFileClip

import os


class AudioFiles:

    def __init__(self, directory_audi_folder, split_up='break.mp3', folder_root='audi_folder/'):
        self.directory_audi_folder = directory_audi_folder
        self.split_up = split_up
        self.folder_root = folder_root

    def merge_audio_files(self):
        list_audio = []
        list_files = os.listdir(self.directory_audi_folder)  # получаем список всех файлов из папки
        for audio in list_files:
            print('Добавляем музыку')
            print(f'{self.folder_root}{audio}')
            list_audio.append(AudioFileClip(f'{self.folder_root}{audio}'))
            list_audio.append(AudioFileClip(self.split_up))

        final_audio = concatenate_audioclips(list_audio)  # обьединяем, контактинируем адио файлы
        final_audio.write_audiofile('finished_result/output.mp3')  # записываем готовыый аудиофайл в папку


f = AudioFiles('audi_folder')
f.merge_audio_files()
