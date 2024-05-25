# Trie structure
# root = {
#     "c":{
#         "a":{
#             "r":{
#                 "endWord":True
#             },
#             "t":{
#                 "endWord":True
#             },
#             "endWord":False
#         },
#         "endWord":False
#     },
#     "d":{
#         "o":{
#             "n":{
#                 "e":{
#                     "endWord":True
#                 },
#                 "endWord":False
#             },
#             "endWord":True
#         },
#         "endWord":False
#     }
# }

products = ["cat", "banana", "obama", "batman", "car", "cow", "alibaba"]
root = {
    "c": {
        "a": {"t": {"endWord": True}, "r": {"endWord": True}, "endWord": False},
        "o": {"w": {"endWord": True}, "endWord": False},
        "endWord": False,
    },
    "b": {
        "a": {
            "n": {
                "a": {
                    "n": {"a": {"endWord": True}, "endWord": False},
                    "endWord": False,
                },
                "endWord": True,
            },
            "t": {
                "m": {
                    "a": {
                        "n": {
                            "endWord": True,
                        },
                        "endWord": False,
                    },
                    "endWord": False,
                },
                "endWord": True,
            },
            "endWord": False,
        },
        "endWord": False,
    },
    "o": {
        "b": {
            "a": {"m": {"a": {"endWord": True}, "endWord": False}, "endWord": False},
            "endWord": False,
        },
        "endWord": False,
    },
    "a": {
        "l": {
            "i": {
                "b": {
                    "a": {
                        "b": {"a": {"endWord": True}, "endWord": False},
                        "endWord": False,
                    },
                    "endWord": False,
                },
                "endWord": False,
            },
            "endWord": False,
        },
        "endWord": False,
    },
}
