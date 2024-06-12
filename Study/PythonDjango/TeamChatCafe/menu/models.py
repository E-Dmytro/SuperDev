from django.db import models, IntegrityError, DataError

from employee.models import Employee

class Menu(models.Model):
    """
        This class represents an employee. \n
        Attributes:
        -----------
        param name: Describes name of the menu
        type name: str max_length=128
        param description: Describes description of the menu
        type description: str
        param count: Describes count of the menu
        type count: int default=10
        param authors: list of Authors
        type authors: list->employee
    """

    name = models.CharField(blank=True, max_length=128)
    description = models.TextField(blank=True)
    count = models.IntegerField(default=10)
    authors = models.ManyToManyField(Employee, related_name='books')

    def __str__(self):
        """
        Magic method is redefined to show all information about Menu.
        :return: menu id, menu name, menu description, menu count, menu authors
        """
        return str(self.to_dict())[1:-1]

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Menu object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'

    @staticmethod
    def get_by_id(book_id):
        """
        :param book_id: SERIAL: the id of a Menu to be found in the DB
        :return: menu object or None if a menu with such ID does not exist
        """
        try:
            user = Menu.objects.get(pk=book_id)
            return user
        except Menu.DoesNotExist:
            pass
            # LOGGER.error("User does not exist")

    @staticmethod
    def delete_by_id(book_id):
        """
        :param book_id: an id of a menu to be deleted
        :type book_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """

        try:
            menu = Menu.objects.get(id=book_id)
            menu.delete()
            return True
        except Menu.DoesNotExist:
            # LOGGER.error("User does not exist")
            pass
        return False

    @staticmethod
    def create(name, description, count=10, authors=None):
        """
        param name: Describes name of the menu
        type name: str max_length=128
        param description: Describes description of the menu
        type description: str
        param count: Describes count of the menu
        type count: int default=10
        param authors: list of Authors
        type authors: list->employee
        :return: a new menu object which is also written into the DB
        """
        menu = Menu(name=name, description=description, count=count)
        try:
            menu.save()
            if authors is not None:
                for employee in authors:
                    menu.authors.add(employee)
            menu.save()
            return menu
        except (IntegrityError, AttributeError, DataError):
            # LOGGER.error("Wrong attributes or relational integrity error")
            pass

    def to_dict(self):
        """
        :return: menu id, menu name, menu description, menu count, menu authors
        :Example:
        | {
        |   'id': 8,
        |   'name': 'django menu',
        |   'description': 'bla bla bla',
        |   'count': 10',
        |   'authors': []
        | }
        """

        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'count': self.count,
            'authors': [employee.id for employee in self.authors.all()]
        }

    def update(self, name=None, description=None, count=None):
        """
        Updates menu in the database with the specified parameters.\n
        param name: Describes name of the menu
        type name: str max_length=128
        param description: Describes description of the menu
        type description: str
        param count: Describes count of the menu
        type count: int default=10
        :return: None
        """

        if name:
            self.name = name
        if description:
            self.description = description
        if count:
            self.count = count
        self.save()

    def add_authors(self, authors):
        """
        Add  authors to  menu in the database with the specified parameters.\n
        param authors: list authors
        :return: None
        """

        for employee in authors:
            self.authors.add(employee)
        self.save()

    def remove_authors(self, authors):
        """
        Remove authors to  menu in the database with the specified parameters.\n
        param authors: list authors
        :return: None
        """
        for employee in authors:
            self.authors.remove(employee)
        self.save()

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all books
        """
        all_users = Menu.objects.all()
        return list(all_users)

    @staticmethod
    def get_all_ordered(order_by, filter):
        """
        returns data for json request with QuerySet of filtered and ordered books
        """
        all_books = Menu.objects.filter(**filter).order_by(*order_by)
        return list(all_books)
    
    def all_authors_string(self):
        """
        Returns a list of authors as a string enumeration. 
        """
        autors = [employee.surname_initials() for employee in employee.objects.filter(books__id = self.id)]
        return ", ".join(autors)
