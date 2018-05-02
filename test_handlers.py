import unittest
import handlers

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_get_by_email_exist(self):
        self.assertEqual(handlers.get_by_email("abhishek@xyz.com"), {'first_name': "abhishek", 'last_name': "kumar", 'email': 'abhishek@xyz.com', 'phone_number': 8987515575})

    def test_get_by_email_not_exist(self):
        self.assertEqual(handlers.get_by_email("abhishek@pqr.com"), False)

    def test_get_by_first_name_exist(self):
        self.assertEqual(handlers.get_by_first_name("abhishek", 2, 0), [{'phone_number': 8987515575, 'first_name': 'abhishek', 'last_name': 'kumar', 'email': 'abhishek@xyz.com'}, {'phone_number': 89875155756, 'first_name': 'abhishek', 'last_name': 'kumar', 'email': 'abhishek@abc.com'}, {'next_page_uri': '/get/name/abhishek?offset=2'}])
 
    def test_get_by_first_name_exist_with_invlid_offset(self):
        self.assertEqual(handlers.get_by_first_name("abhishek", 10, 11), False)

    def test_get_by_first_name_not_exist(self):
        self.assertEqual(handlers.get_by_first_name("abhishek123", 1, 1), False)

    def test_add_user_in_db(self):
        self.assertEqual(handlers.add_user_in_db("abhishek","kumar", "abhishek@pqr.com", 89876767676), True)

    def test_delete_user_in_db_exist(self):
        self.assertEqual(handlers.delete_user_in_db("abhishek@xyz.com"), True)

    def test_delete_user_in_db_not_exist(self):
        self.assertEqual(handlers.delete_user_in_db("abhishek@pqr.com"), False)

if __name__ == '__main__':
    unittest.main()