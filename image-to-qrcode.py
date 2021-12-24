from PIL import Image

inf = Image.open("A.png")
keyf = Image.open("B.png")

inf_rgb = inf.convert("RGB")
keyf_rgb = keyf.convert("RGB")

newimg = Image.new("RGB", (inf.size[0], inf.size[1]))

for x in range(0, inf.size[0]):
    for y in range(0, inf.size[1]):
        in_r, in_g, in_b = inf_rgb.getpixel((x, y))
        key_r, key_g, key_b = keyf_rgb.getpixel((x, y))
        
        in_pixel = (in_r<<16) + (in_g<<8) + in_b;
        key_pixel = (key_r<<16) + (key_g<<8) + key_b;
        
        print(in_pixel)
        print(key_pixel)
        
        new_pixel = bytes(a ^ b for (a, b) in zip(in_pixel.to_bytes(8, byteorder="little"), key_pixel.to_bytes(8, byteorder="little")))
        newimg.putpixel((x, y), int.from_bytes(new_pixel, byteorder = "little"))
newimg.show()
