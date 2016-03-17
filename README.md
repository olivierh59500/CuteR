# CuteR
Combine QRCode with picture

## Sample

Commands:

```bash
python CuteR.py -c 20 -e H -o sample_output.png -v 10 sample_input.png http://www.chinuno.com
python CuteR.py -C -r 0 100 50 sample_input.png http://www.chinuno.com #colourful mode
python main.py -g True -d 0.05 d.gif http://songkaiape.github.io  #GIF mode
```
### GIF Input

![image](/d.gif)

### Output

![image](/qr.gif)
### Input

![image](https://github.com/chinuno-usami/CuteR/raw/master/sample_input.png)

### Output

![image](https://github.com/chinuno-usami/CuteR/raw/master/sample_output.png)

### Output (colourful mode)

![image](https://github.com/chinuno-usami/CuteR/raw/master/sample_output_colourful.png)

## Usage

### As python module

```python
Import CuteR as cr
output = cr.produce(text,image)
```

arguments:

      :txt: QR text
      :img: Image
      :ver: QR version
      :err_crt: QR error correct
      :bri: Brightness enhance
      :cont: Contrast enhance
      :colourful: If colourful mode
      :rgb: color to replace black
      :returns: Produced image

### As command tool

usage:
```
CuteR.py [-h] [-o OUTPUT] [-v VERSION] [-e {Q,H,M,L}] [-b BRIGHTNESS]
                [-c CONTRAST] [-C] [-r R G B] [-g GIF] [-d DURATION] [-m MODIFY]
                image text

Combine your QR code with custom picture

positional arguments:
  image
  text                  QRcode Text.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Name of output file.
  -v VERSION, --version VERSION
                        QR version.In range of [1-40]
  -e {Q,H,M,L}, --errorcorrect {Q,H,M,L}
                        Error correct
  -b BRIGHTNESS, --brightness BRIGHTNESS
                        Brightness enhance
  -c CONTRAST, --contrast CONTRAST
                        Contrast enhance
  -C, --colourful       colourful mode
  -r R G B, --rgb R G B
                        color to replace black
  -g GIF MODE, --gif 
                        use gif picture 
  -d DURATION, --duration duration of gif
                        set duration 
  

```

## Dependencies
- Python  (gif mode only support python2)
- qrcode
- PIL or Pillow

## License
GPLv3
