from django.db import models, IntegrityError, DataError


class Employee(models.Model):
    """
        This class represents an employee. \n
        Attributes:
        -----------
        param name: Describes name of the employee
        type name: str max_length=20
        param surname: Describes last name of the employee
        type surname: str max_length=20
        param patronymic: Describes middle name of the employee
        type patronymic: str max_length=20

    """

    name = models.CharField(blank=True, max_length=20)
    surname = models.CharField(blank=True, max_length=20)
    patronymic = models.CharField(blank=True, max_length=20)

    def __str__(self):
        """
        Magic method is redefined to show all information about employee.
        :return: employee id, employee name, employee surname, employee patronymic
        """
        return str(self.to_dict())[1:-1]

    def __repr__(self):
        """
        This magic method is redefined to show class and id of employee object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'

    @staticmethod
    def get_by_id(author_id):
        """
        :param author_id: SERIAL: the id of a employee to be found in the DB
        :return: employee object or None if a user with such ID does not exist
        """
        try:
            user = employee.objects.get(id=author_id)
            return user
        except employee.DoesNotExist:
            pass
            # LOGGER.error("User does not exist")

    @staticmethod
    def delete_by_id(author_id):
        """
        :param author_id: an id of a employee to be deleted
        :type author_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """

        try:
            employee = employee.objects.get(id=author_id)
            employee.delete()
            return True
        except employee.DoesNotExist:
            # LOGGER.error("User does not exist")
            pass
        return False

    @staticmethod
    def create(name, surname, patronymic):
        """
        param name: Describes name of the employee
        type name: str max_length=20
        param surname: Describes surname of the employee
        type surname: str max_length=20
        param patronymic: Describes patronymic of the employee
        type patronymic: str max_length=20
        :return: a new employee object which is also written into the DB
        """
        employee = employee(name=name, surname=surname, patronymic=patronymic)
        try:
            employee.save()
            return employee
        except (IntegrityError, AttributeError, DataError):
            # LOGGER.error("Wrong attributes or relational integrity error")
            pass

    def to_dict(self):
        """
        :return: employee id, employee name, employee surname, employee patronymic
        :Example:
        | {
        |   'id': 8,
        |   'name': 'fn',
        |   'surname': 'mn',
        |   'patronymic': 'ln',
        | }
        """

        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'patronymic': self.patronymic
        }

    def update(self,
               name=None,
               surname=None,
               patronymic=None):
        """
        Updates employee in the database with the specified parameters.\n
        param name: Describes name of the employee
        type name: str max_length=20
        param surname: Describes surname of the employee
        type surname: str max_length=20
        param patronymic: Describes patronymic of the employee
        type patronymic: str max_length=20
        :return: None
        """

        if name:
            self.name = name
        if surname:
            self.surname = surname
        if patronymic:
            self.patronymic = patronymic
        try:
            from django.db import transaction
            with transaction.atomic():
                self.save()
        except:
            pass

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all authors
        """
        all_users = employee.objects.all()
        return all_users
    
    def surname_initials(self):
        """
        returns surname initials.
        """
        patronymic_is_not_empty = self.patronymic and self.patronymic.strip()
        patronymic  = f"{self.patronymic[0]}." if patronymic_is_not_empty else ""
        return f"{self.surname} {self.name[0]}.{patronymic}".format(**vars())

