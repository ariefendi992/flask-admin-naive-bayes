import json
from flask import Blueprint, request, render_template, redirect, url_for
import requests

ukt = Blueprint('ukt', __name__, template_folder='../templates/beasiswa-ukt',
                url_prefix='/beasiswa-ukt')

# base_url = 'https://api.beasiswa-tuim.site'
base_url = 'http://192.168.1.8:5000'


@ukt.route('/', methods=['GET', 'POST'])
def indexUkt():
    url = base_url+'/beasiswa-ukt'
    x = request.args.get('page')
    req = requests.get(url + f'?page={x}')

    if req.status_code == 200:
        response = req.json()
        return render_template('get-ukt.html', response=response)
    else:
        return req.json().get('msg')


@ukt.route('/test-data', methods=['GET', 'POST'])
def testUkt():
    url = base_url+'/beasiswa-ukt'
    x = request.args.get('page')
    req = requests.get(url + f'?page={x}')

    if req.status_code == 200:
        response = req.json()
        return render_template('testing-ukt.html', response=response)
    else:
        return req.json().get('msg')


@ukt.route('/tambah-ukt', methods=['GET', 'POST'])
def tambahDataUkt():

    url_user = base_url+'/auth/get-all'
    r_user = requests.get(url_user).json()
    resp_user = r_user.get('data')

    url_ukt = base_url+'/beasiswa-ukt/cek-ukt'
    r_ukt = requests.get(url_ukt).json()
    resp_ukt = r_ukt['data']

    url_prodi = base_url+'/kampus/jurusan'
    r_prodi = requests.get(url_prodi).json()
    resp_prodi = r_prodi.get('data')

    url_sms = base_url+'/kampus/semester'
    r_sms = requests.get(url_sms).json()
    resp_sms = r_sms.get('data')

    id_user = request.form.get('id_user')
    nik = request.form.get('nik')
    prodi = request.form.get('prodi')
    sms = request.form.get('semester')
    status_mhs = request.form.get('status_mhs')
    kip = request.form.get('kip')
    penghasilan = request.form.get('penghasilan_orang_tua')
    tanggungan = request.form.get('tanggungan')
    pkh = request.form.get('pkh')
    keputusan = request.form.get('keputusan')

    url_ukt = base_url+'/beasiswa-ukt/tambah-ukt-admin'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        'id_user': id_user,
        'nik': nik,
        'prodi': prodi,
        'semester': sms,
        'status_mhs': status_mhs,
        'kip': kip,
        'penghasilan_orang_tua': penghasilan,
        'tanggungan': tanggungan,
        'pkh': pkh,
        'keputusan': keputusan
    })

    print('json =', payload)
    r = requests.request('POST', url_ukt, headers=headers, data=payload)

    if r.status_code == 201:
        return redirect(url_for('ukt.indexUkt'))
    else:
        return render_template('tambah-ukt.html', resp_user=resp_user, resp_prodi=resp_prodi, resp_sms=resp_sms, resp_ukt=resp_ukt)
    # return render_template('tambah-ukt.html', resp_user=resp_user, resp_prodi=resp_prodi, resp_sms=resp_sms)
