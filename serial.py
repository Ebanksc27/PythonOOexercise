"""Python serial number generator."""

class SerialGenerator:
    """ Machine to create unique incrementing serial numbers.
        Attributes:
        start (int): The starting number for the serial generator.

        Methods:
        generate: Generate the next sequential number.
        
        Reset: Reset the number back to the original start number. 
    """
    def __init__(self, start):
        """
        Initialize the SerialGenerator object with a start number.

        Args:
            start (int): The starting number for the serial generator.
        """
        self.start = start
        self.current = start

    def generate(self):
        """
        Generate the next sequential number.

        Returns:
            int: The next sequential number.
        """
        number = self.current
        self.current += 1
        return number
    
    def reset(self):
        """
        Reset the number back to the original start number.
        """
        self.current = self.start

        serial = SerialGenerator(start=100)

        print(serial.generate())  # Output: 100
        print(serial.generate())  # Output: 101
        print(serial.generate())  # Output: 102

        serial.reset()

        print(serial.generate())  # Output: 100


