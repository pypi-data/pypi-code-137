# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['appdaemon_testing_fork', 'appdaemon_testing_fork.pytest']

package_data = \
{'': ['*']}

entry_points = \
{'pytest11': ['appdaemon_testing_fork = appdaemon_testing_fork.pytest']}

setup_kwargs = {
    'name': 'appdaemon-testing-fork',
    'version': '0.2.0',
    'description': '',
    'long_description': '# Fork\nThis is a fork of https://github.com/nickw444/appdaemon-testing. Currently just trying to release a straight copy.\n\n\n# appdaemon-testing\nErgonomic and pythonic unit testing for AppDaemon apps. Utilities to allow you to test your AppDaemon home automation apps using all the _pythonic_ testing patterns you are already familiar with.\n\n## Install\n\n```sh\npip install appdaemon-testing\n``` \n\n## Full Documentation\n\nAn enhanced, source-linked version of the documentation below as well as complete [API documentation](https://nickwhyte.com/appdaemon-testing/#header-submodules) is available [here](https://nickwhyte.com/appdaemon-testing/)\n\n## Writing your first test\n\nThis demo assumes you will use [`pytest`](https://docs.pytest.org/en/latest/) as your test runner. Install the `appdaemon-testing` and [`pytest`](https://docs.pytest.org/en/latest/) packages:\n\n```sh\npip install appdaemon-testing pytest\n``` \n\nIn your `appdaemon` configuration directory, introduce a new `tests` directory. This is where we are going to write the tests for your apps.\n\nAdditionally we also need to introduce an `__init__.py` file to `tests` and `apps` directories to make them an importable package. You should have a tree that looks something like this:\n\n```\n├── appdaemon.yaml\n├── apps\n│\xa0\xa0 ├── __init__.py\n│\xa0\xa0 ├── apps.yaml\n│\xa0\xa0 └── living_room_motion.py\n├── dashboards\n├── namespaces\n└── tests\n    ├── __init__.py\n    └── test_living_room_motion.py\n```\n\nWe have an automation, `apps/living_room_motion.py` that we wish to test. It looks like this:\n\n```py\nimport appdaemon.plugins.hass.hassapi as hass\n\n\nclass LivingRoomMotion(hass.Hass):\n    def initialize(self):\n        self.listen_state(self.on_motion_detected, self.args["motion_entity"])\n\n    def on_motion_detected(self, entity, attribute, old, new, kwargs):\n        if old == "off" and new == "on":\n            for light in self.args["light_entities"]:\n                self.turn_on(light)\n```\n\nCreate a new file, `tests/test_living_room_motion.py`. This is where we will write the tests for our automation.\n\nFirst we will declare an _`appdaemon_testing.pytest.automation_fixture`_:\n\n```py\n@automation_fixture(\n    LivingRoomMotion,\n    args={\n        "motion_entity": "binary_sensor.motion_detected",\n        "light_entities": ["light.1", "light.2", "light.3"],\n    },\n)\ndef living_room_motion() -> LivingRoomMotion:\n    pass\n```\n\n\nWith this fixture, it\'s now possible to write some tests. We will first write a test to check the state listener callbacks are registered:\n\n```py\ndef test_callbacks_are_registered(hass_driver, living_room_motion: LivingRoomMotion):\n    listen_state = hass_driver.get_mock("listen_state")\n    listen_state.assert_called_once_with(\n        living_room_motion.on_motion_detected, "binary_sensor.motion_detected")\n```\n\nWe use the `appdaemon_testing.pytest.hass_driver` fixture to obtain mock implementations of methods that exist on the AppDaemon Hass API. We can query these mocks and make assertions on their values. In this test we make an assertion that `listen_state` is called once with the specified parameters.\n\nWe will next write a test to make an assertion that the lights are turned on when motion is detected:\n\n```py\ndef test_lights_are_turned_on_when_motion_detected(\n    hass_driver, living_room_motion: LivingRoomMotion\n):\n    with hass_driver.setup():\n        hass_driver.set_state("binary_sensor.motion_detected", "off")\n\n    hass_driver.set_state("binary_sensor.motion_detected", "on")\n\n    turn_on = hass_driver.get_mock("turn_on")\n    assert turn_on.call_count == 3\n    turn_on.assert_has_calls(\n        [mock.call("light.1"), mock.call("light.2"), mock.call("light.3")]\n    )\n```\n\nThis test uses the `HassDriver.setup()` context manager to set the initial state for testing. When execution is within `HassDriver.setup()` all state updates will not be triggered.\n\nWith the initial state configured, we can now proceed to triggering the state change (`HassDriver.set_state`). After the state change has occured, we can then begin to make assertions about calls made to the underlying API. In this test we wish to make assertions that `turn_on` is called. We obtain the `turn_on` mock implementation and make assertions about its calls and call count.  \n\nYou can see this full example and example directory structure within the [`example`](https://github.com/nickw444/appdaemon-testing/tree/master/example) directory in this repo.\n\n\n## [`pytest`](https://docs.pytest.org/en/latest/) plugin\n\nThe `appdaemon_testing.pytest` package provides a handy `appdaemon_testing.pytest.hass_driver` fixture to allow you easy access to the global `HassDriver` instance. This fixture takes care of ensuring AppDaemon base class methods are patched.\n\nAdditionally, it provides a decorator, `appdaemon_testing.pytest.automation_fixture` which can be used to declare automation fixtures. It can be used like so:\n\n```py\nfrom appdaemon_testing.pytest import automation_fixture\nfrom apps.living_room_motion import LivingRoomMotion\n\n\n@automation_fixture(\n    LivingRoomMotion,\n    args={\n        "motion_entity": "binary_sensor.motion_detected",\n        "light_entities": ["light.1", "light.2", "light.3"],\n    },\n)\ndef living_room_motion() -> LivingRoomMotion:\n    pass\n```\n',
    'author': 'Brandon Hoeksema',
    'author_email': 'brandon.hoeksema@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dataisbaye/appdaemon-testing',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '==3.9.0',
}


setup(**setup_kwargs)
