import rembg


input_file = open("lion.jpg", "rb")
output_file = open("output.png", "wb")

input = input_file.read()
output = rembg.remove(input)
output_file.write(output)

input_file.close()
output_file.close()
