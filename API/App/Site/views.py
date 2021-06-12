from . import assets
from API.Core import app, mail, components
from flask_mail import Message
from werkzeug.exceptions import HTTPException
from flask import render_template as render, \
    request, redirect, send_from_directory, Markup, url_for


@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


# Pages
@app.route('/', methods=['GET', 'POST'])
# @app.route('/faq', methods=['GET', 'POST'])
@app.route('/about_us')
@app.route('/services', methods=['GET', 'POST'])
@app.route('/contact_us', methods=['GET', 'POST'])
def Page():
    from .languages import Russian
    return render('site/page/home.html', **Russian.data)


@app.route('/job/<item>', methods=['GET', 'POST'])
def Job(item):
    from .languages import Russian
    return render('site/page/job_item.html', **Russian.data, Title=item)

@app.route('/None')
@app.route('/info/<path:item>', methods=['GET', 'POST'])
def service(item):
    try:
        from .languages import Russian
        return render('site/page/info.html',
                      **Russian.data,
                      Title=str(item).split('/')[1].replace('_', ' ')
                      )
    except Exception:
        return redirect(url_for(request.path))

@app.route('/send', methods=['POST', 'GET'])
def send():
    if request.method == 'POST':
        if request.form['submit'] == "Contact_US":

            Name = str(request.form['Name'])
            eMail = str(request.form['Email'])
            Subject = str(request.form['Subject'])
            eMessage = str(request.form['Message'])

            data = {
                'Name': Name,
                'eMail': eMail,
                'Subject': Subject,
                'eMessage': eMessage
            }

        elif request.form['submit'] == "Subscribe":
            data = {
                'Name': "Подписчик",
                'Subject': "Подписалась",
                'eMessage': "Хочу Подписаться"
            }

            html_message = Markup(
                "<b>Mail: </b>%s <hr> <b> Message: </b> %s" % (data['eMail'], data['eMessage']))

            with app.app_context():
                msg = Message(
                    subject=data['Subject'],
                    sender=(data['Name'], app.config.get("MAIL_USERNAME")),
                    recipients=['Mr.Tarverdyan@yandex.com'],
                    html='%s' % (html_message)
                )

                mail.send(msg)


            return redirect('/')

    else:
        return redirect('/send/')

    html_message = Markup(
        "<b>Mail: </b>%s <hr> <b> Message: </b> %s" % (data['eMail'], data['eMessage']))

    with app.app_context():
        msg = Message(
            subject=data['Subject'],
            sender=(data['Name'], app.config.get("MAIL_USERNAME")),
            recipients=['Mr.Tarverdyan@yandex.com'],
            html='%s' % (html_message)
        )

        mail.send(msg)

    return redirect('/')


# Errors
Errors = dict(zip(components.is_error()['Code'],
                  components.is_error()['Description']))
@app.errorhandler(Exception)
def handle_error(error):
    if isinstance(error, HTTPException):
        code = error.code
        description = (error.get_description())
        title = "Error %s: %s" % (code, str(error.name))
        return render('error.html',
                      number=code,
                      title=title,
                      description=Errors[code]
                      )


@app.errorhandler(500)
def Error(error):
    number = 500
    title = 'Error %i' %(number)
    description = Errors[number]

    return render('error.html',
                  number=number,
                  title=title,
                  description=description
                  )