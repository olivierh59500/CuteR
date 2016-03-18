#!/usr/bin/env python2
from image2gif import writeGif,readGif
from CuteR import produce
from PIL import Image
import qrcode
import os

if __name__ == "__main__":
    
    import argparse
    parser = argparse.ArgumentParser(description="Combine your QR code with custom picture")
    parser.add_argument("image")
    parser.add_argument("text", help="QRcode Text.")
    parser.add_argument("-o", "--output", help="Name of output file.")
    parser.add_argument("-v", "--version", type=int, help="QR version.In range of [1-40]")
    parser.add_argument("-e", "--errorcorrect", choices={"L","M","Q","H"}, help="Error correct")
    parser.add_argument("-b", "--brightness", type=float, help="Brightness enhance")
    parser.add_argument("-c", "--contrast", type=float, help="Contrast enhance")
    parser.add_argument("-C", "--colourful", action="store_true",help="colourful mode")
    parser.add_argument("-r", "--rgb", nargs=3, metavar=('R','G','B'),type = int, help="color to replace black")
    parser.add_argument("-g","--gif",type=bool,help="if the image is gif")
    parser.add_argument("-m","--modify",type=bool,help="resize the image in the middle")
    parser.add_argument("-d","--duration",type=float,help="duration of gif")
    args = parser.parse_args()

    img = args.image
    txt = args.text
    duration=args.duration if args.duration else 0.1
    output = args.output if args.output else 'qr.png'
    ec = qrcode.constants.ERROR_CORRECT_H
    if args.errorcorrect:
        ec_raw = args.errorcorrect
        if ec_raw == 'L':
            ec = qrcode.constants.ERROR_CORRECT_L
        if ec_raw == 'M':
            ec = qrcode.constants.ERROR_CORRECT_M
        if ec_raw == 'Q':
            ec = qrcode.constants.ERROR_CORRECT_Q
    ver = 5
    if args.version:
        if args.version >= 1 and args.version <= 40:
            ver = args.version
    cont = args.contrast if args.contrast else 1.0
    bri = args.brightness if args.brightness else 1.0
    colr = True if args.colourful else False
    if colr :
        if args.rgb:
          rgb = tuple(args.rgb)
        else:
            rgb = (0,0,0)
    else:
        rgb = (0,0,0)
    
    if not args.gif:
        img=Image.open(img)
        if args.modify:
            width,height=images.size
            box=((width-height)/2,0,(width+height)/2,height)
            img=img.crop(box)            
        produce(txt,img,ver,ec,bri, cont ,colourful = colr,rgb=rgb).save(output)
    else:
        output='qr.gif'
        images=readGif(img,False)
        if args.modify:
            width,height=images[0].size
            box=((width-height)/2,0,(width+height)/2,height)
            for im in images:
                im=im.crop(box)
        qr_img=[]
        for im in images:
            temp=produce(txt,im,3,ec,bri, cont ,colourful = True,rgb=(100,150,0))
            qr_img.append(temp)
        writeGif(output,qr_img, duration=duration, subRectangles=False)



