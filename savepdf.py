import os



def savetopdf(path,url):
    cwd = os.path.dirname(__file__)+"/phantomjs/bin/"
    cmd = "%sphantomjs url_to_pdf.js \"%s\" \"%s\"" % (cwd, path,url)
    print(cmd)
    os.system(cmd)


