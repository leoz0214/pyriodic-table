class PyriodicTableException(Exception):
    """
    Base class for all pyriodic_table exceptions.
    """
    pass

class ElementDoesNotExist(PyriodicTableException):
    """
    Chemical element does not exist (or remains undiscovered).
    """
    pass