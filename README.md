# CuteR
Combine QRCode with picture

Sample command
```bash
python CuteR.py sample_input.png http://www.chinuno.com
python CuteR.py -C -r 0 100 50  sample_input.png http://www.chinuno.com #with color mode
```
### Sample input

![image](https://github.com/chinuno-usami/CuteR/raw/master/sample_input.png)

### Sample output

![image](https://github.com/chinuno-usami/CuteR/raw/master/sample_output.png)

### Sample output with color mode

![image](https://github.com/chinuno-usami/CuteR/raw/master/sample_output_color.png)

## Usage

### Import as module

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
      :color: If color mode
      :rgb: color to replace black
      :returns: Produced image

### As a command tool

usage: 
```
CuteR.py [-h] [-o OUTPUT] [-v VERSION] [-e {Q,H,M,L}] [-b BRIGHTNESS]
                [-c CONTRAST] [-C] [-r R G B]
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
  -C, --color           color mode
  -r R G B, --rgb R G B
                        color to replace black
```
## Dependencies
- Python
- qrcode
- PIL or Pillow

## License
GPLv3
