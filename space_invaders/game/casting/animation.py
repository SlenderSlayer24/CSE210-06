import time
from constants import *


class Animation:
    """An animation."""
    
    def __init__(self, images, rate = 6, delay = 0):
        """Constructs a new Animation."""
        self._delay = delay
        self._images = images
        self._rate = rate
        self._index = 0
        self._frame = 0
        self._start = time.time()
        
    def get_delay(self):
        """Gets the delay between animation cycles.
        
        Returns:
            A number representing the delay in seconds.
        """
        return self._delay

    
    def get_images(self):
        """Gets the images that make up the animation.
        
        Returns:
            A list of strings containing the image names.
        """
        return self._images

    def get_rate(self):
        """Gets the rate of animation in frames.
        
        Returns:
            The rate of animation in frames.
        """
        return self._rate