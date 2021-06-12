# -*- coding: utf-8 -*-
# -*- coding_Stype: PEP8 -*-


# saved.py
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


if request.method == 'POST':
    language = request.args.get('lg')
    session['language'] = language
else:
    language = 'None'

if 'language' in session:
    if 'en' in session['language']:
        from .data.languages import English
        return render('site/page/home.html', **English.data)

    elif 'ru' in session['language']:
        from .data.languages import Russian
        return render('site/page/home.html', **Russian.data)

    elif 'am' in session['language']:
        from .data.languages import Armenian
        return render('site/page/home.html', **Armenian.data)

else:
    from .data.languages import English
    return render('site/page/home.html', **English.data)
    # return session.get('language', 'None')


# Error
@app.errorhandler(547)
def NO_547(error):
    number = 547
    title = 'Error 547'
    description = "Database Insert Error"
    return render('error.html',
                  number=number,
                  title=title,
                  description=description
                  ), 547
