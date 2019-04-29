import sys
from PIL import Image

def main():
    if (len(sys.argv) > 1):
        i = Image.open(sys.argv[1], "r")
        data = i.getdata()
        pixels = list(data)
        text = ConvertToText(pixels, data.size[0], data.size[1])
    if (len(sys.argv) > 2):
        f = open(sys.argv[2], "w")
        f.write(text)
        f.close()
    else:
        print(text)

def ConvertToText(pixels:list, columns:int, rows:int):
    output = []
    for r in range(rows):
        row = []
        for c in range(columns):
            avg = mean(pixels[r*columns + c][0:3])
            if (avg > (255 * 0.8)):
                row.append(" ")
            elif (avg > (255 * 0.6)):
                row.append("░")
            elif (avg > (255 * 0.4)):
                row.append("▒")
            elif (avg > (255 * 0.2)):
                row.append("▓")
            elif (avg >= 0):
                row.append("█")
        row.append("\n")
        output.append("".join(row))
    return "".join(output)
            
def mean(a:list):
    return sum(a) / len(a)

if __name__ == "__main__":
    main()