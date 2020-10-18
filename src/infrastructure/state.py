import services.data_services as svc

from data.apartments import Apartment
from data.users import User

active_account: User = None
active_apartment: Apartment = None


def reload_account():
    """
    will reload the active_account and set it in the state, currently not used
    @return:
    """
    global active_account
    if not active_account:
        return

    active_account = svc.find_account_by_email(active_account.email)
    pass


def reload_apartment():
    global active_apartment
    global active_account

    if not active_apartment:
        if active_account:
            if active_account.favorite_apartment:
                active_apartment = svc.get_apartment(active_account.favorite_apartment)
        return

    active_apartment = svc.get_apartment(active_apartment.id)
