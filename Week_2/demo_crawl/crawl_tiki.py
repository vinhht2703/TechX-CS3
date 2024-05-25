# pip install request
# pip list
import requests
import json

# https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&version=home-persionalized&trackity_id=8d4b9386-c82b-5aeb-0fbb-da25a03e217b&category=2549&page=1&urlKey=do-choi-me-be

url = "https://tiki.vn/api/personalish/v1/blocks/listings"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

params = {
    "limit": 10,
    "include": "advertisement",
    "aggregations": 2,
    "version": "home-persionalized",
    "trackity_id": "8d4b9386-c82b-5aeb-0fbb-da25a03e217b",
    "category": 2549,
    "page": 1,
    "urlKey": "do-choi-me-be",
}

lstProduct = []

# for page in range(1, 5):
#     params["page"] = page
#     response = requests.get(url, headers=headers, params=params)

#     if response.status_code == 200:
#         print("Request product ...")
#         for item in response.json().get("data"):
#             lstProduct.append(
#                 {
#                     "id": item["id"],
#                     "sku": item["sku"],
#                     "name": item["name"],
#                     "price": item["price"],
#                     "image": item["thumbnail_url"],
#                 }
#             )

# ------------------ WRITE ------------------
# with open("data_product.json", "w", encoding="utf-8") as file:
#     json.dump(lstProduct, file, ensure_ascii=False)

# ------------------ READ ------------------
with open("data_product.json", "r") as file:
    lstProduct = json.load(file)

print(lstProduct)
