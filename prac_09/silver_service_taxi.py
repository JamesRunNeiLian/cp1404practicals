from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialized version of a Car that includes fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Car but with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.get_fare()}"

    def __repr__(self):
        """Return a string like a Car but with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.get_fare()}"

    def get_fare(self):
        """Return the price for the SilverServiceTaxi trip."""
        return self.flagfall + super().get_fare()