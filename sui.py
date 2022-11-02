
""" Main Class """
class Sui():

    """ Constructor """
    def __init__(self) -> None:
        # Define photo and sound variables
        self.PhotoPath = "lib/photo.jpg"
        self.SoundPath = "lib/sound.mp3"

    """ Photo Function """
    def suiphoto(self):
        # Import module(s)
        from os import system
        # Open the photo
        system(f"start {self.PhotoPath}")

    """ Sound Function """
    def suisound(self):
        # Import module(s)
        from playsound import playsound
        # Play the sound
        playsound(self.SoundPath)

    """ Main Function """
    def main(self):
        # Import module(s)
        from pathlib import Path
        # Check if the photo and sound exist
        if ( Path(self.SoundPath).exists() == True and Path(self.PhotoPath).exists() == True ):
            # Import module(s)
            from threading import Thread
            from time import sleep
            # Create an infinite loop
            while ( self.PhotoPath ):
                # Wait for 0.1 seconds
                sleep(0.3)
                # Open photo with a background process
                Thread(target = Sui.suiphoto, args = [Sui()], daemon = True).start()
                # Open sound with a background process
                Thread(target = Sui.suisound, args = [Sui()], daemon = True).start()

# Initial Call
Sui.main(Sui())