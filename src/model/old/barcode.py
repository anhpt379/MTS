#! coding: utf-8
""" Provided Barcodes
barcode module: ['code39', 'ean', 'ean13', 'ean8', 'gs1', 'gtin', 'isbn', 'isbn10', 'isbn13', 'issn', 'jan', 'pzn', 'upc', 'upca']

"""

def get_qr_code_from_google():
    from pygooglechart import QRChart
    
    # Create a AxA QR code chart
    chart = QRChart(126, 126)
    
    # Add the text
    chart.add_data('ID:1234|Info: foobar')
    
    # "Level H" error correction with a 0 pixel margin
    chart.set_ec('H', 0)
    
    # Download
    chart.download('1.png')

def get_qr_code():
    from elaphe import barcode
    image = barcode('qrcode',
                    'ID:1234|Info: foobar',
                    options=dict(version=9, eclevel='H'),
                    margin=10, data_mode='8bits')
    image.save('2.png')  
    
def read_qrcode():
    pass
  
  
def encode(str):
  pass

def decode(img_file):
  pass

if __name__ == '__main__':
    get_qr_code_from_google()
    get_qr_code()