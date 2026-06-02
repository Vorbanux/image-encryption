from PIL import Image
import shutil
import os

def image_encript(image_path: str, text: str) -> bool:
    #get image
    if list(os.path.splitext(image_path))[1].lower() in [".png", ".jpg"]:
        try:
            #copy image
            copy_path = image_path.split("\\").pop(-1).split(".")[0] + "_copy" + list(os.path.splitext(image_path))[1]
            shutil.copy2(image_path, copy_path)
            imgOpen = Image.open(copy_path)
        except ValueError as error:
            raise ValueError(f"Error: {error}")
    else:
        raise ValueError("Your path is invalid or file extension is not .png or .jpeg")
    #encripting text in the image
    if imgOpen.size[0] * imgOpen.size[1] < len(text):
        raise ValueError("Your text is too big")
    for px_h in range(imgOpen.size[1]):
        for px_w in range(imgOpen.size[0]):
            chr1 = px_h * imgOpen.size[0] + px_w
            if chr1 < len(text):
                char_id = bin(ord(text[chr1]))[2:].zfill(8)
            else:
                char_id = "00000000"
            pixel = imgOpen.getpixel((px_w, px_h))
            new_r = int(f"{pixel[0]:08b}"[:-3] + char_id[0] + char_id[1] + char_id[2], 2)
            new_g = int(f"{pixel[1]:08b}"[:-3] + char_id[3] + char_id[4] + char_id[5], 2)
            new_b = int("0" + f"{pixel[2]:08b}"[:-3] + char_id[6] + char_id[7], 2)
            imgOpen.putpixel((px_w, px_h), (new_r, new_g, new_b))
            if char_id == "00000000":
                break
    imgOpen.save(copy_path)
    return True

def image_decript(image_path: str) -> str:
    #get image
    if list(os.path.splitext(image_path))[1].lower() in [".png", ".jpg"]:
        try:
            img = Image.open(image_path)
        except ValueError as error:
            raise ValueError(f"Error: {error}")
    else:
        raise ValueError("Your path is invalid or file extension is not .png or .jpg")
    #decripting text in the image
    text = ""
    for px_h in range(img.size[1]):
        for px_w in range(img.size[0]):
            pixel = img.getpixel((px_w, px_h))
            bincode = f"{pixel[0]:08b}"[-3] + f"{pixel[0]:08b}"[-2] + f"{pixel[0]:08b}"[-1] + f"{pixel[1]:08b}"[-3] + f"{pixel[1]:08b}"[-2] + f"{pixel[1]:08b}"[-1] + f"{pixel[2]:08b}"[-2] + f"{pixel[2]:08b}"[-1]
            if bincode == "00000000":
                break
            text = f"{text}{chr(int(bincode, 2))}"
    return text

if __name__ == "__main__":
    exit()