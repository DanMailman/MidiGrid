# tMidiPlayer.py: MIDI Player Class
from sys import exit            # Exits Program
from random import choice       # Returns single randomly selected sequence item
from signal import SIGINT       # User Interrupt Signal Ctrl-C
from signal import signal       # register signal handler
from time import sleep          # Suspends execution for the given number of seconds
from kInstr import INSTR_NAMES  # Dictionary mapping ints to strings
from kNote import NOTE_NAMES    # Dictionary mapping ints to strings
from pygame import midi
from sys import stdout          # Output stream
write = stdout.write            # Buffer stdout contents for write
flush = stdout.flush            # Immediately write stdout contents


class tMidiPlayer:
    """
    tMidiPlayer: Manage MIDI output for playing notes with adjustable latency, utilizing pygame's midi module.

    This class encapsulates functionality for initializing the MIDI system, creating a MIDI output port,
    and providing methods for playing and stopping MIDI notes. The LATENCY attribute is used to
    configure the delay between issuing MIDI commands and their execution, thus affecting the
    responsiveness of MIDI playback.

    Attributes:
        LATENCY (int): Latency in milliseconds, intended to adjust the responsiveness of MIDI message processing.
        output (pygame.midi.Output): The MIDI output port for sending MIDI messages.

    Methods:
        __init__(output_id=0): Initializes the tMidiPlayer with a specified MIDI output port.
        __del__(): Destroys the tMidiPlayer object.
        On(instrument, note, volume=127): Plays a MIDI note with the specified instrument and volume.
        Off(instrument, note, volume=127): Stops a MIDI note with the specified instrument.
    """
    LATENCY = 1  # Latency in milliseconds
    def __init__(self, output_id: int = 0) -> None:
        # __init__(): Constructor
        # Implementation: pygame.midi method calls
        midi.quit()
        midi.init()
        self.output = midi.Output(output_id, latency=tMidiPlayer.LATENCY)  # Get MIDI output w/ specified latency
    def On(self, instrument: int, note: int, volume: int = 127) -> None:
        # On(): Turns on a MIDI note with the specified instrument and volume.
        # Implementation: pygame.midi method calls
        print(f"On(): Instrument {INSTR_NAMES[instrument]}, Note {NOTE_NAMES[note]}, Volume {volume}")
        self.output.set_instrument(instrument)
        self.output.note_on(note, volume)
    def Off(self, instrument: int, note: int, volume: int = 127) -> None:
        # Off(): Turns off a MIDI note.
        # Implementation:  pygame.midi method calls
        print(f"Off(): Instrument {INSTR_NAMES[instrument]}, Note {NOTE_NAMES[note]}, Volume {volume}")
        self.output.set_instrument(instrument)
        self.output.note_off(note, volume)
    def __del__(self):
        # __del__(): Ensures proper cleanup by closing the MIDI output and quitting the MIDI system.
        # Implementation: pygame.midi method calls
        # print('tMidiPlayer: Destructor called.')
        if hasattr(self, 'output') and self.output:
            try:
                self.output.close()
            except Exception as e:
                print(f"Error occurred while closing MIDI output: {e}")
        midi.quit()
    @staticmethod
    def main():
        signal(SIGINT, lambda signum, frame: (write("\nExiting gracefully...\n"),
                                              flush(),
                                              exit(0)))
        oMidiPlayer = tMidiPlayer(1)  # Assuming MIDI device ID 1 is correct
        vNotes = list(NOTE_NAMES.keys())
        vInstruments = list(INSTR_NAMES.keys())
        while True:
            nNote = choice(vNotes)
            nInstr = choice(vInstruments)
            # Print instrument and note selection and flush output
            write(f"Playing: {NOTE_NAMES[nNote]}, Instrument: {INSTR_NAMES[nInstr]} - ON ")
            flush()
            try:
                oMidiPlayer.On(nInstr, nNote)
                sleep(1)  # Play note for 1 second
                write("OFF\n")
                flush()
                oMidiPlayer.Off(nInstr, nNote)
            except Exception as e:
                print(f"Error handling MIDI output: {e}")
                break  # Optional: Break the loop on error, or you could continue depending on your use case.
        del oMidiPlayer
if __name__ == "__main__":
    tMidiPlayer.main()
