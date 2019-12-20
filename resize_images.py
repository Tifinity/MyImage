from PIL import Image
import os.path
import glob

def convert(src, outdir, nw=600):
    img = Image.open(src)
    w, h = img.size
    print(w,h)

    nh = nw * h / w
    nh = int(nh)
    print(nw,nh)
    try:
        new_img = img.resize((nw, nh), Image.BILINEAR)   
        new_img.save(os.path.join(outdir, os.path.basename(src)))
    except Exception as e:
        print(e)

outdir = r"D:\TH\MyImage\WebSecurity\hw1DES"

for src in glob.glob(outdir + "/*.png"):
    convert(src, outdir)
for src in glob.glob(outdir + "/*.jpg"):
    convert(src, outdir)