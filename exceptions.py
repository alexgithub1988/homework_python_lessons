class SpravochnikError(Exception):
    pass

class ContactNotFoundError(SpravochnikError):
    pass

class InvalidContactDataError(SpravochnikError):
    pass