# Things are hidden in plain sight...

space = " "
tab = "	"

import binascii

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

i = input("HTML> ")

bits = text_to_bits(i)

invisible = bits.replace("0",space).replace("1",tab)

with open("hips.html","w") as p:
    p.write("<script>"+ "/"+invisible +"""/.source.replace(/ /g, "0").replace(/	/g, "1").replace(/(\d{8})/g, '$1 ').replace(/(^\s+|\s+$)/,'').replace(/\d+./g,str=>String.fromCharCode('0b'+str)).replace(/.{7}/g,function(w){document.write(w)})""" +"</script>")
