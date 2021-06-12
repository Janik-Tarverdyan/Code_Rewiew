# -*- coding: utf-8 -*-
# -*- coding_Stype: PEP8 -*-


# settings.py
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


import os
import binascii
from os.path import join
from dotenv import load_dotenv


class Base(object):
    """Base configuration."""
    SECRET_KEY = binascii.hexlify(os.urandom(24))
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = True
    APPLICATION_NAME = 'API'
    APPLICATION_ROOT = os.path.dirname(os.path.abspath(__name__))
    APPLICATION_STATIC = os.path.join(
        APPLICATION_ROOT, '%s/static' % (APPLICATION_NAME + '/Views'))
    APPLICATION_TEMPLATE = os.path.join(
        APPLICATION_ROOT, '%s/templates' % (APPLICATION_NAME + '/Views'))
    ENV_PATH = join(APPLICATION_ROOT, '.env')
    load_dotenv(ENV_PATH)

    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

    # Mail Server
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'Janik.Tarverdyan@gmail.com'
    MAIL_PASSWORD = 'J5a264klxhr142@JAS_GM'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    # MAIL_SERVER = os.getenv('SERVER')
    # MAIL_PORT = os.getenv('PORT')
    # MAIL_USERNAME = os.getenv('USERNAME')
    # MAIL_PASSWORD = os.getenv('PASSWORD')
    # MAIL_USE_TLS = os.getenv('USE_TLS')
    # MAIL_USE_SSL = os.getenv('USE_SSL')


class Development(Base):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True
    ENV = 'Development'


class Testing(Base):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    ENV = 'Testing'


class Production(Base):
    """Production configuration."""
    DEBUG = False
    DEBUG_TB_ENABLED = False
    ENV = 'Production'
