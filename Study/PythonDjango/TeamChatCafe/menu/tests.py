import datetime
from unittest import mock

import pytz
from django.test import TestCase

from authentication.models import CustomUser
from employee.models import employee
from Menu.models import Menu
from order.models import Order

TEST_DATE = datetime.datetime(2017, 4, 10, 12, 00, tzinfo=pytz.utc)
TEST_DATE_END = TEST_DATE + datetime.timedelta(days=15)


class TestBookModel(TestCase):
    """Class for CustomUser Model test"""

    def setUp(self):
        """ Create a user object to be used by the tests """
        time_mock = datetime.datetime(2017, 4, 10, 12, 00, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now') as mock_time:
            mock_time.return_value = time_mock
            self.user = CustomUser(id=111, email='email@mail.com', password='1234', first_name='fname',
                                   middle_name='mname',
                                   last_name='lname')
            self.user.save()
            self.user_free = CustomUser(id=222, email='2email@mail.com', password='1234', first_name='2fname',
                                        middle_name='2mname',
                                        last_name='2lname')
            self.user_free.save()

            self.author1 = employee(id=101, name="author1", surname="s1", patronymic="p1")
            self.author1.save()

            self.author2 = employee(id=102, name="author2", surname="s2", patronymic="p2")
            self.author2.save()

            self.book1 = Menu(id=101, name="book1", description="description1", count=1)
            self.book1.save()
            self.book1.authors.add(self.author1)
            self.book1.save()

            self.book2 = Menu(id=102, name="book2", description="description2")
            self.book2.save()
            self.book2.authors.add(self.author2)
            self.book2.save()

            self.book3 = Menu(id=103, name="book3", description="description3")
            self.book3.save()
            self.book3.authors.add(self.author1)
            self.book3.authors.add(self.author2)
            self.book3.save()

            self.order1 = Order(id=101, user=self.user, menu=self.book1, plated_end_at=TEST_DATE)
            self.order1.save()
            self.order2 = Order(id=102, user=self.user, menu=self.book2, plated_end_at=TEST_DATE)
            self.order2.save()
            self.order3 = Order(id=103, user=self.user, menu=self.book3, end_at=TEST_DATE_END, plated_end_at=TEST_DATE)
            self.order3.save()

    def test__str__(self):
        """Test of the CustomUser.__str__() method"""
        book_returned = str(Menu.objects.get(id=101))
        book_to_expect = "'id': 101, 'name': 'book1', 'description': 'description1', 'count': 1, 'authors': [101]"

        self.assertEqual(book_returned, book_to_expect)

    def test__repr__(self):
        """Test of the CustomUser.__repr__() method"""
        book_returned = repr(Menu.objects.get(id=102))
        book_to_expect = "Menu(id=102)"

        self.assertEqual(book_returned, book_to_expect)

    def test_get_by_id_positive(self):
        """Positive test of the CustomUser.get_by_id() method"""
        menu = Menu.get_by_id(101)
        self.assertEqual(menu.id, 101)
        self.assertEqual(menu.name, 'book1')
        self.assertEqual(menu.description, "description1")
        self.assertEqual(menu.count, 1)
        self.assertListEqual(list(menu.authors.all()), [self.author1])

    def test_get_by_id_negative(self):
        """Negative test of the CustomUser.get_by_id() method"""
        menu = Menu.get_by_id(999)
        self.assertIsNone(menu)

    def test_delete_by_id_positive(self):
        """ Test of the CustomUser.delete_by_id() method """
        self.assertTrue(Menu.delete_by_id(103))
        self.assertRaises(Menu.DoesNotExist, Menu.objects.get, pk=103)
        self.assertRaises(Order.DoesNotExist, Order.objects.get, pk=103)
        self.assertEqual(self.author1, employee.objects.get(id=101))
        self.assertEqual(self.author2, employee.objects.get(id=102))

    def test_delete_by_id_negative(self):
        """ Test of the CustomUser.delete_by_id() method """
        self.assertFalse(Menu.delete_by_id(999))

    def test_create_positive_name_description(self):
        """ Positive Test of the CustomUser.create method """

        menu = Menu.create(name="testBook", description="testDescription")
        self.assertIsInstance(menu, Menu)
        self.assertEqual(menu.name, "testBook")
        self.assertEqual(menu.description, "testDescription")
        self.assertEqual(menu.count, 10)
        self.assertListEqual(list(menu.authors.all()), [])

    def test_create_positive_name_description_empty(self):
        """ Positive Test of the CustomUser.create method """

        menu = Menu.create(name="testBook", description="")
        self.assertIsInstance(menu, Menu)
        self.assertEqual(menu.name, "testBook")
        self.assertEqual(menu.description, "")
        self.assertEqual(menu.count, 10)
        self.assertListEqual(list(menu.authors.all()), [])

    def test_create_positive_name_description_count(self):
        """ Positive Test of the CustomUser.create method """

        menu = Menu.create(name="testBook", description="testDescription", count=5)
        self.assertIsInstance(menu, Menu)
        self.assertEqual(menu.name, "testBook")
        self.assertEqual(menu.description, "testDescription")
        self.assertEqual(menu.count, 5)
        self.assertListEqual(list(menu.authors.all()), [])

    def test_create_positive_name_description_count_a(self):
        """ Positive Test of the CustomUser.create method """

        menu = Menu.create(name="testBook", description="testDescription", count=5,
                           authors=[self.author1, self.author2])
        self.assertIsInstance(menu, Menu)
        self.assertEqual(menu.name, "testBook")
        self.assertEqual(menu.description, "testDescription")
        self.assertEqual(menu.count, 5)
        self.assertListEqual(list(menu.authors.all()), [self.author1, self.author2])

    def test_create_negative_len_name(self):
        """ Positive Test of the CustomUser.create method TEST_DATE_END"""
        menu = Menu.create(name="1" * 128, description="12")
        self.assertIsInstance(menu, Menu)
        menu = Menu.create(name="1" * 129, description="12")
        self.assertIsNone(menu)

    def test_get_all(self):
        """ Positive Test of the CustomUser.create method TEST_DATE_END"""
        books = Menu.get_all()
        books.sort(key=lambda menu: menu.id)
        self.assertListEqual(books, [self.book1, self.book2, self.book3])

    def test_add_authors(self):
        menu = Menu.objects.get(id=103)
        menu.add_authors([self.author2])

        menu = Menu.objects.get(id=103)
        self.assertListEqual(list(menu.authors.all()), [self.author1, self.author2])

    def test_add_authors_duplicate(self):
        menu = Menu.objects.get(id=103)
        menu.add_authors([self.author1, self.author2])

        menu = Menu.objects.get(id=103)
        self.assertListEqual(list(menu.authors.all()), [self.author1, self.author2])

    def test_remove_authors(self):
        menu = Menu.objects.get(id=103)
        menu.remove_authors([self.author1, self.author2])

        menu = Menu.objects.get(id=103)
        self.assertListEqual(list(menu.authors.all()), [])

    def test_update(self):
        menu = Menu.objects.get(id=101)
        menu.update(name="testName", description="testDescription", count=5)
        menu = Menu.objects.get(id=101)
        self.assertIsInstance(menu, Menu)
        self.assertEqual(menu.name, "testName")
        self.assertEqual(menu.description, "testDescription")
        self.assertEqual(menu.count, 5)
        self.assertListEqual(list(menu.authors.all()), [self.author1])

    def test_update_name(self):
        menu = Menu.objects.get(id=101)
        menu.update(name="testName")
        menu = Menu.objects.get(id=101)
        self.assertIsInstance(menu, Menu)
        self.assertEqual(menu.name, "testName")
        self.assertEqual(menu.description, "description1")
        self.assertEqual(menu.count, 1)
        self.assertListEqual(list(menu.authors.all()), [self.author1])
