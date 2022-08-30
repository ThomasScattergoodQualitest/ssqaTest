import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_non_existing_user(self):
        print("*********")
        print("TEST LOGIN NON EXISTING")
        print("*********")
        my_account = MyAccountSignedOut(self.driver)
        # go to my account
        my_account.go_to_my_account()
        # type username
        my_account.input_login_username('asdasdeqd')
        # type_password
        my_account.input_login_password('a13123h1jebjh')
        # click login
        my_account.click_login_button()

        # verify error message
        expected_err = 'Error: The username asdasdeqd is not registered on this site. ' \
                       'If you are unsure of your username, try your email address instead.'
        my_account.wait_until_error_is_displayed(expected_err)
