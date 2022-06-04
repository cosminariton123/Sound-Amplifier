import matplotlib.pyplot as plt
import numpy as np
import librosa
import copy
import soundfile

def load_song(song_path):
    y = librosa.load(song_path)
    data = y[0]
    sample_rate = y[1]

    return np.array(data), sample_rate

def dump_song(song_path, song, sample_rate):
    soundfile.write(song_path, song, sample_rate)

def plot_song(figure, title, y):
    plt.figure(figure)

    x = np.linspace(0, len(y), len(y))

    print(len(x))
    print(len(y))


    plt.plot(x, y)
    plt.ylim((-3, 3))
    plt.title(title)

def amplify(ammount, song):
    new_song = copy.deepcopy(song)
    new_song *= ammount

    return new_song
    
def main():
    song_path = "File.wav"
    original_song, original_sample_rate = load_song(song_path)
    amplified_song = amplify(6, original_song)
    plot_song(1, "Original",  original_song)
    plot_song(2, "Amplified",  amplified_song)
    dump_song(song_path.split(".")[0] + "_amplified." + song_path.split(".")[1], amplified_song, original_sample_rate)
    plt.show()

if __name__ == '__main__':
    main()