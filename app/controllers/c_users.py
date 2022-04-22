import json
from flask import Blueprint, redirect, render_template, request, url_for
import requests

admin = Blueprint('admin', __name__, url_prefix='/',
                  template_folder='../templates/admin/')

# base_url = 'https://api.beasiswa-tuim.site'
base_url = 'http://192.168.1.9:5000'


# dashboard
@admin.route('/', methods=['GET', 'POST'])
def adminDashboard():
    url = base_url + '/total-data'
    r = requests.get(url).json()
    data = r.get('data')
    ukt = data[0].get('total_penerima').get('beasiswa_ukt')
    print(ukt)
    user = data[0].get('total_user')
    user_login = data[0].get('total_user_login')

    return render_template('dashboard.html', ukt=ukt, user=user, user_login=user_login)


# kategori Fakultas
@admin.route('/kategori-fakultas', methods=['GET', 'POST'])
def kategoriF():

    return render_template('fakultas.html')


# kategori jurusan
@admin.route('/kategori-jurusan', methods=['GET', 'POST'])
def kategoriJ():
    url = base_url + '/kategori/jurusan'
    req = requests.get(url).json()
    response = req.get('data')

    return render_template('jurusan.html', response=response)


# User all data
@admin.route('/users', methods=['GET', 'POST'])
def userData():
    url = base_url+'/auth/get-all'

    r = requests.get(url).json()
    resp = r.get('data')

    return render_template('user-data.html', response=resp)


# user login data
@admin.get('/users-login')
def userLogin():
    url = base_url+'/auth/user-login'

    r = requests.get(url).json()
    resp = r.get('data')

    return render_template('user-login.html', response=resp)


# user add
@admin.route('/user-add', methods=['GET', 'POST'])
def userAdd():
    stambuk = request.form.get('nim')
    nama = request.form.get('name')
    gender = request.form.get('jk')
    email = request.form.get('mail')
    password = request.form.get('pswd')

    url = base_url + '/auth/register'

    headers = {
        'Content-Type': 'application/json'
    }

    payload = json.dumps({
        'stambuk': stambuk,
        'nama': nama,
        'gender': gender,
        'email': email,
        'password': password
    })

    r = requests.post(url=url, headers=headers, data=payload)

    if r.status_code == 201:
        return redirect(url_for('admin.userData'))
    else:
        return render_template('user-add.html')


# get user by id
@admin.route('/edit-user', methods=['POST', 'GET'])
def userById():
    id = request.args.get('id')
    url = base_url + ('/auth/get-uid')

    r = requests.get(url + f'?id={id}')

    resp = r.json()

    return render_template('user-edit.html', response=resp)


# edit user
@admin.route('/update', methods=['PUT', 'PATCH', 'POST'])
def userEdit():
    stambuk = request.form.get('nim')
    nama = request.form.get('name')
    gender = request.form.get('jk')
    email = request.form.get('mail')
    password = request.form.get('pswd')

    headers = {
        'Content-Type': 'application/json'
    }

    payload = json.dumps({
        'stambuk': stambuk,
        'nama': nama,
        'gender': gender,
        'email': email,
        'password': password
    })

    id = request.args.get('id')
    url = base_url + '/auth/edit-user'
    r = requests.put(url + f'?id={id}', headers=headers, data=payload)

    if r.status_code == 201:
        return redirect(url_for('admin.userData'))
    else:
        return redirect(url_for('admin.userById'))


# delete user
@admin.route('/delete-user', methods=['POST', 'GET', 'DELETE'])
def userDelete():
    id = request.args.get('id')
    url = base_url + ('/auth/delete-user')
    r = requests.delete(url + f'?id={id}')

    if r.status_code == 204:
        return redirect(url_for('admin.userData'))
