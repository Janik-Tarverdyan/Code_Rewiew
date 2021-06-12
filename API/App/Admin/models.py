# -*- coding: utf-8 -*-
# -*- coding_Stype: PEP8 -*-

# models.py
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


from Core import db


class User(db.Model):
    __tablename__ = 'Admin_Users'

    id = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(128))
    Last_Name = db.Column(db.String(50))
    UserName = db.Column(db.String(50))
    eMail = db.Column(db.String(32))
    Password = db.Column(db.String(64))
    Permission = db.Column(db.String(12))
