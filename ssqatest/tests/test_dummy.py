import pytest


@pytest.mark.usefixtures("init_driver")
class TestDummy:
    def test_dummy_func(self):
        print("I am a dummy test line 1")
        print("I am a dummy test line 2")
        self.driver.get("http://supersqa.com")
        #import pdb; pdb.set_trace()