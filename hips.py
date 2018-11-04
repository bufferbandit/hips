#/usr/bin/env python3

# H.I.P.S, by BufferBandit.
# Hide your HTML source code by encoding it with tabs and spaces...


import binascii

class HIPS:
    
    def __init__(self,raw_html="<svg/onload=alert(1)>"):
        self.space,self.tab = " ","	"
        self.raw_html = raw_html      

    def text_to_bits(self,text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))

    def get_encoded_bits(self,raw_html):
        bits = self.text_to_bits(self.raw_html)
        invisible_bits = bits.replace("0",self.space).replace("1",self.tab)
        return invisible_bits

    def create_html_file(self):
        invisible_bits = self.get_encoded_bits(self.raw_html ) #document.write
        html_string = "<script>"+ "/"+invisible_bits +"""/.source.replace(/ /g, "0").replace(/	/g, "1").replace(/(\d{8})/g, '$1 ').replace(/(^\s+|\s+$)/,'').replace(/\d+./g,str=>String.fromCharCode('0b'+str)).replace(/.{7}/g,function(w){document.write(w)})""" +"</script>"
        return html_string

    def write_html(self,out_file="hips.html"):
        with open(out_file,"w") as p:
            p.write(self.create_html_file())
            
if __name__ == "__main__":
    hips = HIPS()
    hips.write_html()
           
