# -*- coding: utf-8 -*-
# -*- coding_Stype: PEP8 -*-


# __init__.py
#
# Copyright 2021 Janik Tarverdyan <Janik.Tarverdyan@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later


from . import settings
from flask import Flask
from flask_mail import Mail
from flask_script import Manager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Set Settings
Settings = settings.Production

app = Flask(
    import_name=Settings.APPLICATION_NAME,
    root_path=Settings.APPLICATION_ROOT,
    template_folder=Settings.APPLICATION_TEMPLATE,
    static_folder=Settings.APPLICATION_STATIC,
    instance_relative_config=True
)
app.config.from_object(Settings)


# Add extensions into application
db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=Settings.APPLICATION_ROOT+"/migrations")
manager = Manager(app)
mail = Mail(app)

# init app
db.init_app(app)
migrate.init_app(app, db)
mail.init_app(app)
