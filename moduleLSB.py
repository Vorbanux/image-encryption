from PIL import Image
import shutil
import os

def image_encript(image_path: str, text: str) -> bool:
    #get image
    image_path = os.path.normpath(image_path)
    if list(os.path.splitext(image_path))[1].lower() in [".png", "jpg", ".jpeg"]:
        try:
            #copy image
            if list(os.path.splitext(image_path))[1].lower() == ".jpeg":
                copy_path = os.path.splitext(image_path)[0] + "_copy.png"
            else:
                copy_path = os.path.splitext(image_path)[0] + "_copy" + list(os.path.splitext(image_path))[1]
            shutil.copy2(image_path, copy_path)
            imgOpen = Image.open(copy_path)
        except Exception as error:
            print(f"Error: {error}")
            return False
    else:
        print("Your path is invalid or file extension is not .png or .jpeg")
        return False
    #encripting text in the image
    text_bytes = text.encode("utf-8")
    if imgOpen.size[0] * imgOpen.size[1] < len(text_bytes):
        print("Your text is too big")
        return False
    for px_h in range(imgOpen.size[1]):
        for px_w in range(imgOpen.size[0]):
            chr1 = px_h * imgOpen.size[0] + px_w
            if chr1 < len(text_bytes):
                char_id = bin(text_bytes[chr1])[2:].zfill(8)
            elif chr1 == len(text_bytes) or chr1 == len(text_bytes) + 1:
                char_id = "00000000"
            else:
                break
            pixel = imgOpen.getpixel((px_w, px_h))
            new_r = (pixel[0] & 0b11111000) | int(char_id[0:3], 2)
            new_g = (pixel[1] & 0b11111000) | int(char_id[3:6], 2)
            new_b = (pixel[2] & 0b11111100) | int(char_id[6:8], 2)
            if imgOpen.mode == "RGBA":
                imgOpen.putpixel((px_w, px_h), (new_r, new_g, new_b, pixel[3]))
            else:
                imgOpen.putpixel((px_w, px_h), (new_r, new_g, new_b))
        else:
            continue
        break
    imgOpen.save(copy_path)
    return True

def image_decript(image_path: str) -> str:
    #get image
    if os.path.splitext(image_path)[1].lower() in [".png", ".jpg", "jpeg"]:
        try:
            img = Image.open(image_path)
        except Exception as error:
            print(f"Error: {error}")
            return False
    else:
        print("Your path is invalid or file extension is not .png, .jpg or .jpeg")
        return False
    #decripting text in the image
    extracted_bytes = bytearray()
    prev_bincode = ""
    for px_h in range(img.size[1]):
        for px_w in range(img.size[0]):
            pixel = img.getpixel((px_w, px_h))
            r_bits = f"{(pixel[0] & 0b111):03b}"
            g_bits = f"{(pixel[1] & 0b111):03b}"
            b_bits = f"{(pixel[2] & 0b11):02b}"
            bincode = r_bits + g_bits + b_bits
            if bincode == "00000000" and prev_bincode == "00000000":
                if extracted_bytes:
                    extracted_bytes.pop() 
                break
            extracted_bytes.append(int(bincode, 2))
            prev_bincode = bincode
        else:
            continue
        break
    try:
        text = extracted_bytes.decode('utf-8')
    except Exception as error:
        print("Decryption failed. Data might be corrupted")
        return False
    return text

if __name__ == "__main__":
    exit()
