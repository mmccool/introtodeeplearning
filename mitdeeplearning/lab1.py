import os
import regex as re
import subprocess
import urllib
import numpy as np
import tensorflow as tf

from IPython.display import Audio


cwd = os.path.dirname(__file__)

def load_training_data():
    with open(os.path.join(cwd, "data", "irish.abc"), "r") as f:
        text = f.read()
    songs = extract_song_snippet(text)
    return songs

def extract_song_snippet(text):
    pattern = '(^|\n\n)(.*?)\n\n'
    search_results = re.findall(pattern, text, overlapped=True, flags=re.DOTALL)
    songs = [song[1] for song in search_results]
    print("Found {} songs in text".format(len(songs)))
    return songs

def save_song_to_abc(song, filename="tmp"):
    save_name = "{}.abc".format(filename)
    with open(save_name, "w") as f:
        f.write(song)
    return filename

def abc2wav(file_basename):
    abc_file = "{}.abc".format(file_basename)
    path_to_tool = os.path.join(cwd, 'bin', 'abc2wav')
    cmd = "{} {}".format(path_to_tool, abc_file)
    return os.system(cmd)

def abc2midi(file_basename):
    abc_file = "{}.abc".format(file_basename)
    path_to_tool = os.path.join(cwd, 'bin', 'abc2mid.sh')
    cmd = "{} {}".format(path_to_tool, abc_file)
    return os.system(cmd)

def play_wav(file_basename):
    wav_file = "{}.wav".format(file_basename)
    # change this to a download link
    # return Audio(wav_file)
    print("Download the wav file: ",wav_file)

def play_midi(file_basename):
    midi_file = "{}.mid".format(file_basename)
    print("Download the midi file: ",midi_file)

def play_song(song, filename="tmp"):
    basename = save_song_to_abc(song,filename)
    # ret = abc2wav(basename)
    ret = abc2midi(basename)
    if ret == 0: # success
        # return play_wav(basename)
        return play_midi(basename)
    return None

def play_generated_song(generated_text):
    songs = extract_song_snippet(generated_text)
    if len(songs) == 0:
        print("No valid songs found in generated text. Try training the \
            model longer or increasing the amount of generated music to \
            ensure complete songs are generated!")

    for song in songs:
        play_song(song)
    print("None of the songs were valid, try training longer to improve \
        syntax.")

def test_batch_func_types(func, args):
    ret = func(*args)
    assert len(ret) == 2, "[FAIL] get_batch must return two arguments (input and label)"
    assert type(ret[0]) == np.ndarray, "[FAIL] test_batch_func_types: x is not np.array"
    assert type(ret[1]) == np.ndarray, "[FAIL] test_batch_func_types: y is not np.array"
    print("[PASS] test_batch_func_types")
    return True

def test_batch_func_shapes(func, args):
    dataset, seq_length, batch_size = args
    x, y = func(*args)
    correct = (batch_size, seq_length)
    assert x.shape == correct, "[FAIL] test_batch_func_shapes: x {} is not correct shape {}".format(x.shape, correct)
    assert y.shape == correct, "[FAIL] test_batch_func_shapes: y {} is not correct shape {}".format(y.shape, correct)
    print("[PASS] test_batch_func_shapes")
    return True

def test_batch_func_next_step(func, args):
    x, y = func(*args)
    assert (x[:,1:] == y[:,:-1]).all(), "[FAIL] test_batch_func_next_step: x_{t} must equal y_{t-1} for all t"
    print("[PASS] test_batch_func_next_step")
    return True

def test_custom_dense_layer_output(layer, x_input, y):
    # compute correct answer (inputs are random)
    Wcheck = layer.W.numpy()
    bcheck = layer.b.numpy()
    zcheck = np.add(np.matmul(x_input.numpy(),Wcheck),bcheck)
    true_y = 1.0/(1.0+np.exp(-zcheck))
    print("True y:",true_y)
    # This is no longer correct
    # true_y = np.array([[0.2697859,  0.45750418, 0.66536945]],dtype='float32')
    assert tf.shape(y).numpy().tolist() == list(true_y.shape), "[FAIL] output is of incorrect shape. expected {} but got {}".format(true_y.shape, y.numpy().shape)
    np.testing.assert_almost_equal(y.numpy(), true_y, decimal=7, err_msg="[FAIL] output is of incorrect value. expected {} but got {}".format(true_y, y.numpy()), verbose=True)
    print("[PASS] test_custom_dense_layer_output")
    return True
