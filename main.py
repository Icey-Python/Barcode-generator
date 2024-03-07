import requests
def create_barcode(code:str):
  """
  {
  code:str
  }
  """
  url:str =f"https://www.webarcode.com/barcode/image.php?code={code}&type=C128B&xres=1&height=50&width=258&font=3&output=png&style=197"
  print(requests.get(url))
  with open("images/barcode.png", "wb") as file:
    file.write(requests.get(url).content)
    
create_barcode("SCT212-0165/2023")