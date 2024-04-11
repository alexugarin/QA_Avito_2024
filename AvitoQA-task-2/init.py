import json


def init():
    data_tests = [[-1, 0, 1, 999],
                  [1000, 1001, 1100, 999999],
                  [1000000, 1100000, 999999999],
                  [1000000000, 1100000000, 999999999999],
                  [1000000000000, 1100000000000, 999999999999999, 9999999999999999]
                  ]
    data_json_template = {
        "result": {
            "blocks": {
                "personalImpact": {
                    "data": {
                        "co2": 0,
                        "energy": 0,
                        "materials": 0,
                        "pineYears": 0,
                        "water": 0
                    }
                }
            },
            "isAuthorized": False
        },
        "status": "ok"
    }
    for i, mocked_data in enumerate(data_tests, start=1):
        for j, test in enumerate(mocked_data, start=1):
            data_json_template["result"]["blocks"]["personalImpact"]["data"]["co2"] = test
            data_json_template["result"]["blocks"]["personalImpact"]["data"]["energy"] = test
            data_json_template["result"]["blocks"]["personalImpact"]["data"]["water"] = test
            with open('mock/test-{}.{}.json'.format(i, j), 'w') as file:
                json.dump(data_json_template, file, indent=4)


if __name__ == '__main__':
    init()
