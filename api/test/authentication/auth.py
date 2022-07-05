import requests
from datetime import datetime
from datetime import datetime
from requests.adapters import HTTPAdapter, Retry
import time

time.sleep(2)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

tests_list = [
    {
        "username" : "alice",
        "password" : "wonderland",
        "status_code" : 200
    },
    {
        "username" : "samanth",
        "password" : "datascientest",
        "status_code" : 401
    }
]

for i in range(len(tests_list)):
    session = requests.Session()
    session.auth = (tests_list[i]["username"], tests_list[i]["password"])
    retries = Retry(total=5)
    session.mount("http://", HTTPAdapter(max_retries=retries))
    r = session.get(
        url = "http://api:8000/LR/perf"
    )

    output_template = """
    ===========================
        Authentication test
    ===========================

    date = {date}
    username = {username}
    password = {password}

    expected_result = {expected}
    actual_result = {status_code}

    ==> {test_status}
    """

    if r.status_code == tests_list[i]["status_code"]:
        test_status = "SUCCESS"
    else:
        test_status = "FAILURE"

    output = output_template.format(
        date = now,
        username = tests_list[i]["username"],
        password = tests_list[i]["password"],
        expected = tests_list[i]["status_code"],
        status_code = r.status_code,
        test_status = test_status
    )

    with open("./mon_volume/api_test.log", "a") as file:
        file.write(output)
