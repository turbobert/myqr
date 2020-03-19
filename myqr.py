#!/usr/bin/env python3


import qrcode
import sys


#modes: [1] == gotomeeting ID
#       [1] == youtube ID


if sys.argv[1] == "gotomeeting" or sys.argv[1] == "gm":
    url = "https://global.gotomeeting.com/join/%s" % sys.argv[2]
    print("url=%s" % url)
    img = qrcode.make(url)
    img.save("gotomeeting.png")
    sys.exit(0)

if sys.argv[1] == "zoom" or sys.argv[1] == "z":
    url = "https://zoom.us/j/%s" % sys.argv[2]
    print("url=%s" % url)
    img = qrcode.make(url)
    img.save("zoom.png")
    img.save("zoom-%s.png" % sys.argv[2])
    sys.exit(0)

if sys.argv[1] == "mail":
    address = sys.argv[2]
    subject = sys.argv[3]
    body = sys.argv[4]
    if body == "-":
        import sys
        body = sys.stdin.read()
    import urllib.parse
    data = { "subject": subject, "body": body }
    img = qrcode.make("mailto:%s?%s" % (address, urllib.parse.urlencode(data)))
    img.save("mail.png")
    sys.exit(0)

if sys.argv[1] == "text":
    body = sys.argv[2].replace("\\n", "\n")
    if body == "-":
        import sys
        body = sys.stdin.read()
    img = qrcode.make(body)
    img.save("text.png")
    sys.exit(0)

if sys.argv[1] == "youtube":
    url = "https://www.youtube.com/watch?v=%s" % sys.argv[2]
    print("url=%s" % url)
    img = qrcode.make(url)
    img.save("youtube.png")
    sys.exit(0)

if sys.argv[1] == "bank":
    if len(sys.argv) == 2 or sys.argv[2] == "help":
        print("myqr bank <EMPFÄNGER> <IBAN> <BETRAG> <BETREFF>")
        print("Betrag mit PUNKT nicht mit KOMMA")
        sys.exit(0)
    empf = sys.argv[2]
    iban = sys.argv[3]
    amount = sys.argv[4]
    betreff = sys.argv[5]

    text = """bcd
001
1
SCT

%s
%s
EUR%s

%s

""" % (empf, iban, amount, betreff)
    img = qrcode.make(text)
    img.save("bank.png")
    sys.exit(0)
