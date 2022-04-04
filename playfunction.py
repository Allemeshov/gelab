# include your files
import functionDictionary as fD
import noteDictionary as nD

# now include system libraries
# include the pyvisa library
import pyvisa


from time import sleep  # the sleep function is needed for the timing

# before you can play any note, you need to connect your device:
rm = pyvisa.ResourceManager()
device = rm.open_resource('USB0::0x0957::0x2607::MY59003075::0::INSTR')
device.write("OUTP1:LOAD 33")
device.write("OUTP2:LOAD 33")
# set your device timeout to 1 sec:
device.timeout = 1000

piece_speed = 100


# playNote function
# parameters: note, noteDuration, pieceSpeed (default 100), function
def play_note(note, note_duration, function="noise"):
    # you can use the following dictionary to calculate the duration of a note
    duration_dictionary = {
        "full": 2,
        "half": 1,
        "half_pointed": 1.5,
        "eighth": 0.5,
        "eighth_pointed": 0.75,
        "sixteenth": 0.25
    }
    # to play a note you now can call the functionDictionary
    # and the noteDictionary from your files
    # you only have to add the Magnitude and the Offset at the end
    device.write("SOUR1:APPL:" + fD.funDict[function] + " " + nD.noteDict[note] + ", 30mVpp, 0V")
    device.write("SOUR2:APPL:" + fD.funDict[function] + " " + nD.noteDict[note] + ", 30mVpp, 0V")
    # turn on the outputs
    device.write("OUTP1 ON")
    device.write("OUTP2 ON")

    # calculate the duration of the note
    # wait for this duration
    duration = 60 * duration_dictionary[note_duration] / piece_speed

    # sleep for the calculated duration
    sleep(duration)

    # turn off the outputs
    device.write("OUTP1 OFF")
    device.write("OUTP2 OFF")

    # 0.05s break to get a little time between the notes
    sleep(0.05)


# def pause(pause_type):


def set_song_speed(speed):
    global piece_speed
    piece_speed = speed
