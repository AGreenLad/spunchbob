from flask import Flask, request, send_file, after_this_request
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from os import remove


app = Flask(__name__)


@app.route('/')
def index():
    print('someone clicked the link lul')
    # woah ip pulling
    ip_address = request.environ['HTTP_X_FORWARDED_FOR']
    img = Image.open('spunchbob.jpeg').convert('RGB')
    x = img.width//2
    y = img.height//1.1

    font = ImageFont.truetype('impact.ttf', 30)
    
    
    blurred = Image.new('RGBA', img.size)
    draw = ImageDraw.Draw(blurred)
    draw.text(xy=(x,y), text=ip_address, fill='black', font=font, anchor='mm')
    blurred = blurred.filter(ImageFilter.BoxBlur(7))
    
    img.paste(blurred,blurred)
    
    draw = ImageDraw.Draw(img)
    draw.text(xy=(x,y), text=ip_address, font=font, anchor='mm')
    img.save('spunchbob_final.jpeg')
    @after_this_request
    def remove_file(response):
      #seeeeee replit it doesnt log your ip pls dont ban me
        try:
            remove('spunchbob_final.jpeg')
        except Exception as error:
            print('wtf it didnt work also heres the error: ' + error)
        return response
    return send_file('spunchbob_final.jpeg', mimetype='image/jpeg')
    


app.run(host='0.0.0.0', port=81)
