from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import db, User, ScanResult
from scanner_engine import perform_scan
from risk_engine import classify_risk


app = Flask(__name__)

# -------------------------
# Configuration
# -------------------------
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# -------------------------
# Login Manager Setup
# -------------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# -------------------------
# Create Database Tables
# -------------------------
with app.app_context():
    db.create_all()


# -------------------------
# Routes
# -------------------------

@app.route('/')
def home():
    return redirect(url_for('login'))


# -------------------------
# Login
# -------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Credentials"

    return render_template("login.html")


# -------------------------
# Register
# -------------------------
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = generate_password_hash(request.form['password'])

    # Check if user exists
    if User.query.filter_by(username=username).first():
        return "User already exists"

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login'))


# -------------------------
# Dashboard
# -------------------------
@app.route('/dashboard')
@login_required
def dashboard():
    results = ScanResult.query.order_by(ScanResult.timestamp.desc()).all()

    return render_template(
        "dashboard.html",
        username=current_user.username,
        results=results
    )


# -------------------------
# Scan Route
# -------------------------
@app.route('/scan', methods=['POST'])
@login_required
def scan():
    target = request.form['target']

    try:
        scan_data = perform_scan(target)

        for data in scan_data:
            risk = classify_risk(data['port'])

            result = ScanResult(
                target=target,
                ip=data['ip'],
                port=data['port'],
                service=data['service'],
                risk=risk
            )

            db.session.add(result)

        db.session.commit()

    except Exception as e:
        return f"Scan Error: {str(e)}"

    return redirect(url_for('dashboard'))


# -------------------------
# Logout
# -------------------------
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
