import qrcode

imagem = qrcode.make('https://github.com/DiegoDeJesuss')
imagem.save('qrcode-github.png')

