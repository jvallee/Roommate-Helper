import datetime
from typing import List
from data.tasks import Task
from data.users import User
from data.apartments import Apartment
from infrastructure.util import error_msg


def create_account(name: str, email: str, password: str) -> User:
    """
    creates a User and stores to the database
    @param name: name of person for account to create
    @param email: email of person for account to create
    @param password: password of person for account to create
    @return: the created account
    """
    user = User()
    user.name = name
    user.email = email.strip().lower()
    user.password = password
    user.save()

    return user


def create_apartment(apartment_name: str, occupants: List[str], user: User):
    account = find_account_by_email(user.email)
    apartment = Apartment()
    apartment.apartmentName = apartment_name
    apartment.occupants = occupants
    apartment.user_ids = str(account.id)
    apartment.save()

    account.apartment_ids.append(apartment.id)
    if account.favorite_apartment is None:
        account.favorite_apartment = str(apartment.id)

    account.save()
    print("apartment created")
    return apartment


def find_account_by_email(email: str):
    """
    queries the database and returns the user associated with the email
    @param email: email we want to find in database
    @return:
    """
    user: User = User.objects().filter(email=email.strip().lower()).first()
    return user


def get_apartment(apartment_id):
    """

    @param apartment_id: name of apartment to get
    @return: apartment
    """
    apartment = Apartment.objects().filter(id=apartment_id).first()
    if apartment is None:  # TODO: Throw an error here
        print("Should not be here apartmentid = ", apartment_id)
        apartment = Apartment().objects().first()
    return apartment


def get_user_apartments(user: User):
    """

    @param user: user we want apartments of
    @return: apartment
    """
    apartments = []
    query = Apartment.objects(id__in=user.apartment_ids)
    apartments = list(query)

    return apartments


def apartment_exist():
    """
    check and sees if a apartment is in the database
    @return:
    """
    project = Apartment.objects().first()
    return project is not None


def add_task_to_apartment(apartment_id: str, task_name: str, assigned_to: str, period_length: int = None):
    """
    add a task to an apartment
    @return:
    """
    print(f"apartment_id = {apartment_id}")
    apartment = Apartment.objects().filter(id=apartment_id).first()
    print(apartment.apartmentName)
    if not apartment:
        error_msg("apartment not found, system error")
        return None
    task = create_task(task_name, assigned_to, period_length)
    print(f"task = {task}")
    old_tasks = apartment.tasks
    tasks = []
    if not old_tasks:
        tasks.append(task)
    else:
        old_tasks.append(task)
        tasks = old_tasks
    apartment.tasks = tasks
    print("apartment.tasks = ", apartment.tasks)
    apartment.save()
    print("task saved")
    return task


def add_occupant_to_apartment(occupant: str, apartment_id: Apartment):
    apartment = get_apartment(apartment_id)
    if apartment.occupants is None:
        apartment.occupants = [occupant]
    else:
        apartment.occupants.append(occupant)
    apartment.save()


def create_task(task_name: str, assigned_to: str, period_length: int = None):
    task = Task()
    task.name = task_name
    task.assignedTo = assigned_to
    task.periodLengthInDays = period_length
    task.lastCompleted = task.lastCompleted = datetime.datetime.now()

    if period_length:
        task.nextDue = task.lastCompleted + datetime.timedelta(days=int(period_length))
    return task


def delete_task(task: Task, apartment_id):
    apartment = Apartment.objects.filter(id=apartment_id).first()
    if not task and not apartment:
        error_msg('Could not find Apartment or Task')
        return False

    else:
        Apartment.objects(id=apartment_id).update_one(pull__tasks=task)
        return True
