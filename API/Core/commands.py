# -*- coding: utf-8 -*-
# -*- coding_Stype: PEP8 -*-


# commands.py
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


from flask_migrate import MigrateCommand
from Core import manager
import os


manager.add_command('db', MigrateCommand)


@manager.command
def runserver():
    command = "gunicorn --reload API.Core.wsgi:app"
    # command = "export FLASK_APP=API/Core/wsgi.py; flask run -h 0.0.0.0"

    return os.system(command)


@manager.command
def local_server():
    command = "gunicorn --reload -w 3 -b 0.0.0.0:8000 API.Core.wsgi:app"

    return os.system(command)


# @manager.command
# def shell():
    # command = "ipython"

    # return os.system(command)
