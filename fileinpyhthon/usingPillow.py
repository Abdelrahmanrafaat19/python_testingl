# from PIL import Image, ImagePalette

# firstImage = Image.open(
#     r"C:\Users\Admin\Desktop\121451037_370734270959886_8419926284063898094_n.jpg"
# )
# cutingImage = firstImage.convert("L")
# # cutingImage.save(r"C:\Users\Admin\Pictures\Screenshots\Screenshot (124).png")

# cutingImage.show()


def sayHello(*name):
    for name in name:
        print(name)


sayHello("Abdelrahman", 255, "SHOAB")
