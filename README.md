# PCI driver for python

## Environment
- Linux
- python 3
- require : [portio module](http://portio.inrim.it/)


## Usage

    >>> import pypci
    
    # look-up pci board
    >>> board = pypci.lspci(vendor=0x1147, device=3214)
    
    >>> board[0].vendor_id
    4423
    
    >>> board[0].bar
    [BaseAddressRegister(type='mem', addr=2421170176, size=64),
     BaseAddressRegister(type='mem', addr=2421166080, size=64),
     BaseAddressRegister(type='mem', addr=2421174272, size=32)]
    
    >>> bar2 = board[0].bar[2]
    
    # read data
    >>> pypci.read(bar2, 0x0c, 4)
    b'\x00\x00\x00\x0c'
    
    # write data
    >>> pypci.write(b[0].bar[2], 0x04, b'\x01')
    
    >>> data = struct.pack('<I', 1234567)
    >>> pypci.write(b[0].bar[2], 0x00, data)
    

