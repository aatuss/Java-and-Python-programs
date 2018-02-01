from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request


# curl -i http://localhost:5000/artistit   nayttaa kaikki artistit
# curl -i http://localhost:5000/artistit/artistin_nimi   hakee artistia nimella
# curl -i -H "Content-Type: application/json" -X POST -d '{"nimi":"artistin_nimi"}' http://localhost:5000/artistit  lisaa uuden
# curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/artistit/nimi  poistaa artistin
# curl -i -H "Content-Type: application/json" -X PUT -d '{"nimi":"uusi_nimi"}' http://localhost:5000/artistit/nimi

# curl -i http://localhost:5000/albumit   nayttaa kaikki albumit
# curl -i http://localhost:5000/albumit/albumin_nimi   hakee albumia albumin nimella
# curl -i http://localhost:5000/albumit_artisti/nimi  hakee albumia artistin nimella
# curl -i -H "Content-Type: application/json" -X POST -d '{"nimi":"albunimi", "artisti":"artisti_nimi,"julkaisuvuosi":"100"}' http://localhost:5000/albumit
# curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/albumit/albumin_nimi poistaa albumin
# curl -i -H "Content-Type: application/json" -X PUT -d '{"nimi":"uusi_nimi"}' http://localhost:5000/albumit/valittuTietue

# Jos parametrissa esiintyy valilyonti, niin se tarvitsee %20 sanojen valiin
# Esimerkiksi: curl -i http://localhost:5000/artistit/Lynyrd%20Skynyrd
# Tai: curl -i http://localhost:5000/albumit/Street%20Survivors haettaessa albumin nimella albumia


app = Flask(__name__)

artistit = [
    {
        'nimi': u'Rammstein',
    },
    {
        'nimi': u'Lynyrd Skynyrd',
    },
    {
        'nimi': u'Queen',
    }
]

albumit = [
    {
        'nimi': u'Reise, Reise',
        'artisti': u'Rammstein',
        'julkaisuvuosi': u'2004',
    },
    {
        'nimi': u'Street Survivors',
        'artisti': u'Lynyrd Skynyrd',
        'julkaisuvuosi': u'1997',
    },
    {
        'nimi': u'Jazz',
        'artisti': u'Queen',
        'julkaisuvuosi': u'1978',
    }
]


#virheiden hallintaa varten. Tulostuu "Not found", jos loytyy virhe
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# FUNKTIOT ARTISTIEN KASITTELYA VARTEN


# hakee kaikki artistit
@app.route('/artistit', methods=['GET'])
def get_artistit():
    return jsonify({'artistit': artistit})

# hakee yksittaisen artistin
@app.route('/artistit/<string:artist_nimi>', methods=['GET'])
def get_artisti(artist_nimi):
    artist = [artist for artist in artistit if artist['nimi'] == artist_nimi]
    if len(artist) == 0:
        abort(404)
    return jsonify({'artisti': artist[0]})


# lisaa uuden artistin
@app.route('/artistit', methods=['POST'])
def create_artisti():
    if not request.json or not 'nimi' in request.json:
        abort(400)
    artist = {
        'nimi': request.json['nimi'],
    }
    artistit.append(artist)
    return jsonify({'artisti': artist}), 201

# paivittaa artistin tietoja
@app.route('/artistit/<string:artist_nimi>', methods=['PUT'])
def update_artisti(artist_nimi):
    artist = [artist for artist in artistit if artist['nimi'] == artist_nimi]
    if len(artist) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'nimi' in request.json and type(request.json['nimi']) != unicode:
        abort(400)
    if 'nimi' in request.json and type(request.json['nimi']) is not unicode:
        abort(400)
    artist[0]['nimi'] = request.json.get('nimi', artist[0]['nimi'])

    return jsonify({'artist': artist[0]})

# poistaa artistin nimella kutsuttaessa
@app.route('/artistit/<string:artist_nimi>', methods=['DELETE'])
def delete_artisti(artist_nimi):
    for artist in artistit:
        if artist['nimi'] == artist_nimi:
            artistit.remove(artist)
            return jsonify({'result': True})
    abort(404)



# FUNKTIOT ALBUMIEN KASITTELYA VARTEN

# hakee kaikki albumit
@app.route('/albumit', methods=['GET'])
def get_albumit():
    return jsonify({'albumit': albumit})

# hakee yksittaista albumia albumin nimella
@app.route('/albumit/<string:album_nimi>', methods=['GET'])
def get_albumi(album_nimi):
    album = [album for album in albumit if album['nimi'] == album_nimi]
    if len(album) == 0:
        abort(404)
    return jsonify({'albumi': album[0]})

#hakee albumia artistin nimella
@app.route('/albumit_artisti/<string:artist_nimi>', methods=['GET'])
def get_albumi_artistin_nimella(artist_nimi):
    album = [album for album in albumit if album['artisti'] == artist_nimi]
    if len(album) == 0:
        abort(404)
    return jsonify({'albumi': album[0]})

# lisaa uuden albumin
@app.route('/albumit', methods=['POST'])
def create_albumi():
    if not request.json or not 'nimi' in request.json:
        abort(400)
    album = {
        'nimi': request.json['nimi'],
        'artisti': request.json['artisti'],
        'julkaisuvuosi': request.json['julkaisuvuosi'],
    }
    albumit.append(album)
    return jsonify({'albumi': album}), 201

# paivittaa albumin tietoja
@app.route('/albumit/<string:albumi_nimi>', methods=['PUT'])
def update_albumi(albumi_nimi):
    album = [album for album in albumit if album['nimi'] == albumi_nimi]
    if len(album) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'nimi' in request.json and type(request.json['nimi']) != unicode:
        abort(400)
    if 'nimi' in request.json and type(request.json['nimi']) is not unicode:
        abort(400)
    album[0]['nimi'] = request.json.get('nimi', album[0]['nimi'])
    album[0]['artisti'] = request.json.get('artisti', album[0]['artisti'])
    album[0]['julkaisuvuosi'] = request.json.get('julkaisuvuosi', album[0]['julkaisuvuosi'])
    return jsonify({'albumi': album[0]})

# poistaa albumin nimella kutsuttaessa
@app.route('/albumit/<string:albumi_nimi>', methods=['DELETE'])
def delete_albumi(albumi_nimi):
    for albumi in albumit:
        if albumi['nimi'] == albumi_nimi:
            albumit.remove(albumi)
            return jsonify({'result': True})
    abort(404)

if __name__ == '__main__':
    app.run(port=5000)
