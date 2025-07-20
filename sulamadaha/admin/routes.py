from flask import Flask, render_template, redirect, url_for, Blueprint, flash
from sulamadaha.admin.forms import loginadmin_F
from sulamadaha.models import TPengguna, TPenjual, TAdmin, TPaketWisata, TBooking, TPembayaran
from sulamadaha import db



radmin = Blueprint('radmin', __name__)


@radmin.route('/')
def home():
    return render_template("home.html")

@radmin.route('/about')
def about():
    return render_template("about.html")

@radmin.route('/login_admin',methods=['GET', 'POST'])
def login_admin():
    form = loginadmin_F()
    return render_template("admin/login_a.html",form=form)

