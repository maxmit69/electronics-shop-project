class InstantiateCSVError(Exception):
    """ Класс исключения InstantiateCSVError
    """

    def __init__(self, *args) -> None:
        self.message = args[0] if args else None
