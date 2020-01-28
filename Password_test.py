import unittest,pyperclip # Importing the unittest module
from Password import Credential,UsersData # Importing the contact class

class TestCredential(unittest.TestCase):
 def setUp(self):
        '''
        Set up method to run before each test case
        '''

        # Create credential object
        self.new_user = Credential("phannie","gmail","atienophanice1")

def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''

        Credential.user_list = []

def test_init(self):
        '''
        Test case to test if the object is initialised properly
        '''
        self.assertEqual( self.new_user.user.password, "phannie")
        self.assertEqual( self.new_user.user_name, "atienophanice" )
        self.assertEqual( self.new_user.user_account, "gmail" )

def test_save_credential(self):
        '''
        Test case to test if the user object is saved into the user list
        '''

        # Save the new credential
        self.new_user.save_credential()

        self.assertEqual( len(Credential.credential_list), 1 )


def test_generate_password(self):
        '''
        Test case to test if a user can log into their credentials
        '''

        generated_password = self.new_credential.generate_password()

        self.assertEqual( len(generated_password), 8 )


def test_display_credential(self):
        '''
        Test case to test if a user can see a list of all the credentials saved
        '''

        # Save the new credential
        self.new_credential.save_credential()

        test_credential = Credential("Phannie","gmail","atienophanice1")

        test_credential.save_credential()

        test_credential = Credential("phannie","gmail","atienophanice1")

        test_credential.save_credential()

        self.assertEqual(len(Credential.display_credential("phannie"),2))

def test_credential_exist(self):

        '''
        Test to check if we can return a boolean if we can't find the credential
        '''

        # Save the new credential
        self.new_credential.save_credential()

        test_credential = Credential("phannie","atienophanice","gmail")

        test_credential.save_credential()

        # use contact exist method
        credential_exists = Credential.credential_exist("Gmail")

        self.assertTcrue(credential_exists)


class TestUsersData(unittest.TestCase):
    def setUp(self):
        '''
        Setting up the structure before each test
        '''
        self.new_data = UsersData(1,1,"facebook.com","phannie")

    def tearDown(self):
        '''
        Cleans up the test after test is complete
        '''
        UsersData.data_list = []

    def test_init(self):
        '''
        Test case to evaluate if the case has been initialized properly
        '''
        self.assertEqual(self.new_data.identity,1)
        self.assertEqual(self.new_data.data_id,1)
        self.assertEqual(self.new_data.website,"facebook.com")
        self.assertEqual(self.new_data.web_key,"phannie")

    def test_add_password(self):
        '''
        Testing if the new website and password can be saved
        '''
        self.new_data.add_password()
        self.assertEqual(len(UsersData.data_list),1)

    def test_display_data(self):
        '''
        Testing if the data can be displayed.
        '''
        self.new_data.add_password()
        test_data = UsersData(1,1,"facebook.com","phannie")
        test_data.add_password()

        data_found = UsersData.display_data(1,1)
        self.assertEqual(data_found.website,test_data.website)

    def test_data_exists(self):
        '''
        Testing to check if the function for checking data works well
        '''
        self.new_data.add_password()
        test_data = UsersData(1,1,"facebook.com","phannie")
        test_data.add_password()

        data_exists = UsersData.existing_data(1)
        self.assertTrue(data_exists)

    def test_copy_password(self):
        '''
        Testing if the copy password function works
        '''
        self.new_data.add_password()
        UsersData.copy_password(1,1)
        self.assertEqual(self.new_data.web_key,pyperclip.paste())


if __name__ == "__main__":
    unittest.main()