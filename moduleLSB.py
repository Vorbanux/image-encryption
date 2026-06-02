from PIL import Image
import shutil
import os

def image_encript(image_path: str, text: str) -> bool:
    #get image
    if list(os.path.splitext(image_path))[1].lower() in [".png", ".jpeg"]:
        try:
            #copy image
            copy_path = list(os.path.splitext(image_path))[0] + "_copy" + list(os.path.splitext(image_path))[1]
            shutil.copy2(image_path, copy_path)
            imgOpen = Image.open(copy_path)
        except ValueError as error:
            print(f"Error: {error}")
            return False
    else:
        print("Your path is invalid or file extension is not .png or .jpeg")
        return False
    #encripting text in the image
    if imgOpen.size[0] * imgOpen.size[1] < len(text):
        print("Your text is too big")
        return False
    for px_h in range(imgOpen.size[1]):
        for px_w in range(imgOpen.size[0]):
            chr1 = px_h * imgOpen.size[0] + px_w
            if chr1 < len(text):
                char_id = bin(ord(text[chr1]))[2:].zfill(16)
            else:
                char_id = "0000000000000000"
            pixel = imgOpen.getpixel((px_w, px_h))
            new_r = (pixel[0] & 0b11111000) | int(char_id[0:3], 2)
            new_g = (pixel[1] & 0b11111000) | int(char_id[3:6], 2)
            new_b = (pixel[2] & 0b11111100) | int(char_id[6:8], 2)
            imgOpen.putpixel((px_w, px_h), (new_r, new_g, new_b))

            if char_id == "0000000000000000":
                return True
    imgOpen.save(copy_path)
    return True

def image_decript(image_path: str) -> str:
    #get image
    if list(os.path.splitext(image_path))[1].lower() in [".png", ".jpg"]:
        try:
            img = Image.open(image_path)
        except ValueError as error:
            print(f"Error: {error}")
            return False
    else:
        print("Your path is invalid or file extension is not .png or .jpg")
        return False
    #decripting text in the image
    text = ""
    for px_h in range(img.size[1]):
        for px_w in range(img.size[0]):
            pixel = img.getpixel((px_w, px_h))
            bincode = f"{pixel[0]:16b}"[-3] + f"{pixel[0]:16b}"[-2] + f"{pixel[0]:16b}"[-1] + f"{pixel[1]:16b}"[-3] + f"{pixel[1]:16b}"[-2] + f"{pixel[1]:16b}"[-1] + f"{pixel[2]:16b}"[-2] + f"{pixel[2]:16b}"[-1]
            if bincode == "0000000000000000":
                Return True
            text = f"{text}{chr(int(bincode, 2))}"
    return text

if __name__ == "__main__":
    exit()
