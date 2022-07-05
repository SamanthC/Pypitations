import requests
from datetime import datetime
from requests.adapters import HTTPAdapter, Retry
import time

time.sleep(2)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

tests_list = [
    {
        "index" : 89,
        "status_code" : 200
    },
    {
        "index" : 187987,
        "status_code" : 500
    },
    {
        "index" : "NOK",
        "status_code" : 422
    }
]

for i in range(len(tests_list)):
    session = requests.Session()
    session.auth = ("alice", "wonderland")
    retries = Retry(total=5)
    session.mount("http://", HTTPAdapter(max_retries=retries))
    r = session.get(
        url = "http://api:8000/LR/test?index={}".format(tests_list[i]["index"])
    )

    output_template = """
    ===========================
          ECG_index test
    ===========================

    date = {date}
    username = alice
    password = wonderland
    index = {index}

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
        index = tests_list[i]["index"],
        expected = tests_list[i]["status_code"],
        status_code = r.status_code,
        test_status = test_status
    )

    print(output)

    with open("./mon_volume/api_test.log", "a") as file:
        file.write(output)
