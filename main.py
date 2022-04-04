import playfunction as pf


def main():
    start_wars_song()


def start_wars_song():
    pf.set_song_speed(120)
    pf.play_note("G4", "half")
    pf.play_note("G4", "half")
    pf.play_note("G4", "half")
    pf.play_note("Eb4", "eighth_pointed")
    pf.play_note("Bb4", "sixteenth")

    pf.play_note("G4", "half")
    pf.play_note("Eb4", "eighth_pointed")
    pf.play_note("Bb4", "sixteenth")
    pf.play_note("G4", "full")

    pf.play_note("D5", "half")
    pf.play_note("D5", "half")
    pf.play_note("D5", "half")
    pf.play_note("G4", "eighth_pointed")
    pf.play_note("G4", "sixteenth")

    pf.play_note("F#4", "half")
    pf.play_note("D4", "eighth_pointed")
    pf.play_note("Bb4", "sixteenth")
    pf.play_note("G4", "full")

    pf.play_note("G5", "half")
    pf.play_note("G4", "eighth_pointed")
    pf.play_note("G4", "sixteenth")
    pf.play_note("G5", "half")
    pf.play_note("F#5", "eighth")
    pf.play_note("F5", "eighth")

    pf.play_note("E5", "half")
    pf.play_note("F#4", "half")
    pf.play_note("C#5", "half")
    pf.play_note("C5", "eighth_pointed")
    pf.play_note("B4", "sixteenth")

    pf.play_note("B4", "half")
    pf.play_note("Eb4", "half")
    pf.play_note("F#4", "half")
    pf.play_note("Eb4", "eighth_pointed")
    pf.play_note("F#4", "sixteenth")

    pf.play_note("Bb4", "half")
    pf.play_note("G4", "eighth_pointed")
    pf.play_note("B4", "sixteenth")
    pf.play_note("D5", "full")

    print("Star Wars song is competed.")


def song2():
    pf.set_song_speed(76)
    pf.pause("", "full")



if __name__ == "__main__":
    main()