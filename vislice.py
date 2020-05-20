import model
import bottle

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')


@bottle.post('/igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.redirect('/igra/{}/'.format(id_igre))


@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, poskus = vislice.igre[id_igre]
    return bottle.template('igre.tpl', id_igre=id_igre, igra=igra, poskus=poskus)


@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/{}/'.format(id_igre))


bottle.run(reloader=True, debug=True)