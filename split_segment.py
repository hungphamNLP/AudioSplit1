
from utils import read_frames_from_file,convert_audio
from scipy.io import wavfile
import argparse
import os

## convert file '''
# tyle file mp3,...
# rate=16k
# tyle:wav
# '''

# def convert_file(path,newpath):
#     convert_audio(path,newpath)
from audio import AudioFile


allow_tags = {"speech", "male", "female", "noisy_speech", "music"}
segment_backend='vad'

def Split_VAD(audio_file,path_folder,sample_rate=16000):
    audio_file = AudioFile(audio_file)
    for (start, end, audio, tag) in audio_file.split(backend='vad', classify=True):
        if tag not in allow_tags:
            continue
        elif tag == 'music':
            continue
        elif tag == 'background':
            continue
        else:
            wavfile.write(str(path_folder)+'/'+str(end)+'.wav',sample_rate,audio)
            

def main(audio_file,new_audio_file,folder_save_file_split):
    # convert to wav ()

    convert_audio(audio_file,new_audio_file)
    # luu file da tach
    Split_VAD(new_audio_file,folder_save_file_split)

if __name__ =='__main__':
    # main('quangnam.wav','file_new.wav','Audio_path')

    parser = argparse.ArgumentParser()
    parser.add_argument('--file_audio',type=str,required=True,help="Choose a file audio to split with .mp3,.wav")
    parser.add_argument('--file_audio_new',type=str,required=True,help='file audio convert to normalize')
    parser.add_argument('--folder_split_file',type=str,required=True,help='folder save file wav')
    
    args = parser.parse_args()
    os.mkdir(args.folder_split_file)

    main(args.file_audio,args.file_audio_new,args.folder_split_file)
    

    
