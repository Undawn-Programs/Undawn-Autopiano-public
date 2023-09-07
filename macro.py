import mido
import pyautogui
import time
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--file", type=str, help="Path to midi file to play", dest='path')
parser.add_argument("--pitch", type=int, default=0, help="Pitch modulation to add", dest="pt_mod")
args = parser.parse_args()

def map_piano_note_to_key(note):
    piano_G = ['f1', 'f2', 'f3']
    piano_keymap = ['q', '1', 'w', '2', 'e', 'r', '3', 't', '4', 'y', '5',
              'u', 'i', '6', 'o', '7', 'p', '[', '8', ']', '9', '\\', '0','-', '=']
    if not(36 <= msg.note <= 96):
        return '', ''
    
    if 36 <= note <= 59:
        change_G = piano_G[0]
        baseline = 36
    elif 60 <= note <= 83:
        change_G = piano_G[1]
        baseline = 60
    else:
        change_G = piano_G[2]
        baseline = 84
    return change_G, piano_keymap[note-baseline]

midi = mido.MidiFile(args.path)
print(f"MIDI File parsed.")
time.sleep(5)
curr_pitch = 'f2'
pyautogui.press(curr_pitch)
pyautogui.PAUSE = 0
for msg in midi.play():
    if msg.type == 'note_on' and msg.velocity != 0:
            pitch, key = map_piano_note_to_key(msg.note+args.pt_mod)
            if curr_pitch != pitch:
                pyautogui.press(pitch)
                curr_pitch = pitch
            pyautogui.press(key)
