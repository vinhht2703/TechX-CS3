lstTest1 = [
    {
        "id": 1,
        "value": [
            {
                "id": 2,
                "value": [{"id": 3, "value": [{"id": 4, "value": []}]}],
            },
        ],
    },
    {"id": 5, "value": []},
]

lstTest2 = [
    {
        "id": 1,
        "value": [
            {
                "id": 2,
                "value": [{"id": 3, "value": [{"id": 4, "value": []}]}],
            },
            {"id": 6, "value": []},
        ],
    },
    {"id": 5, "value": []},
]

# lstResult = [
#     {"id": 1},
#     {"id": 2},
#     {"id": 3},
#     {"id": 4},
#     {"id": 5},
# ]

# def getIds(data, res=[]):
#     for item in data:
#         res.append({"id": item["id"]})
#         if len(item["value"]) > 0:
#             getIds(item["value"], res)

#     return res


# print(getIds(lstDemo))


def getList(data):
    result = []
    for item in data:
        result.append({"id": item["id"]})
        result.extend(getList(item["value"]))

    return result


print(getList(lstTest1))
