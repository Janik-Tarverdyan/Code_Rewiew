from glob2 import glob as find
from API.Core import Settings


def is_error():
    Errors = {
            'Client': {
                    "Status_1": 400,
                    'Description_1': "BAD REQUEST",

                    "Status_2": 401,
                    'Description_2': "UNAUTHORIZED",

                    # "Status_3": 402,
                    # 'Description_3': "PAYMENT REQUIRED",

                    "Status_4": 403,
                    'Description_4': "FORBIDDEN",

                    "Status_5": 404,
                    'Description_5': "PAGE NOT FOUND",

                    "Status_6": 405,
                    'Description_6': "METHOD NOT ALLOWED",

                    "Status_7": 406,
                    'Description_7': "NOT ACCEPTABLE",

                    # "Status_8": 407,
                    # 'Description_8': "PROXY AUTHENTICATION REQUIRED",

                    "Status_9": 408,
                    'Description_9': "REQUEST TIMEOUT",

                    "Status_10": 409,
                    'Description_10': "CONFLICT",

                    "Status_11": 410,
                    'Description_11': "GONE",

                    "Status_12": 411,
                    'Description_12': "LENGTH REQUIRED",

                    "Status_13": 412,
                    'Description_13': "PRECONDITION FAILED",

                    "Status_14": 413,
                    'Description_14': "REQUEST ENTITY TOO LARGE",

                    "Status_15": 414,
                    'Description_15': "REQUEST URI TOO LONG",

                    "Status_16": 415,
                    'Description_16': "UNSUPPORTED MEDIA TYPE",

                    "Status_17": 416,
                    'Description_17': "REQUESTED RANGE NOT SATISFIABLE",

                    "Status_18": 417,
                    'Description_18': "EXPECTATION FAILED",

                    "Status_19": 428,
                    'Description_19': "PRECONDITION REQUIRED",

                    "Status_20": 429,
                    'Description_20': "TOO MANY REQUESTS",

                    "Status_21": 431,
                    'Description_21': "REQUEST HEADER FIELDS TOO LARGE",
            },
            'Server': {
                    'Status_1': 500,
                    'Description_1': "INTERNAL SERVER ERROR",

                    'Status_2': 501,
                    'Description_2': "NOT IMPLEMENTED",

                    'Status_3': 502,
                    'Description_3': "BAD GATEWAY",

                    'Status_4': 503,
                    'Description_4': "SERVICE UNAVAILABLE",

                    'Status_5': 504,
                    'Description_5': "GATEWAY TIMEOUT",

                    'Status_6': 505,
                    'Description_6': "HTTP VERSION NOT SUPPORTED",

                    # 'Status_7': 511,
                    # 'Description_7': "NETWORK AUTHENTICATION REQUIRED",
            }
    }

    Client = list(Errors['Client'].values())
    Server = list(Errors['Server'].values())

    Status = {
            'Code': [],
            'Description': []
    }
    for status_code in range(0, len(Client)):
        if str(Client[status_code]).isdigit() is True:
            Status['Code'].append(Client[status_code])
        elif str(Client[status_code]).isdigit() is False:
            Status['Description'].append(Client[status_code])
        else:
            continue

    for description in range(0, len(Server)):
        if str(Server[description]).isdigit() is True:
            Status['Code'].append(Server[description])
        elif str(Server[description]).isdigit() is False:
            Status['Description'].append(Server[description])
        else:
            continue

    return Status


class Find:
    def Notify(Title, Description):
        Title = str(Title)
        Description = str(Description)

        print(
                " \v %s: \n" % (Title) + "\n"
                + "\t+" + (len(Description) + 2) * '-' + "+" + "\n"
                + "\t| " + Description + ' |' + "\n"
                + "\t+" + (len(Description) + 2) * '-' + "+" + "\n"
        )

    def Images(**args):
        try:
            URL = "/site/Master_Mind/Data/Media/%s/Images/%s/%s/" % (
                    args['Language'], args['Path'], args['Name'])
            path = Settings.APPLICATION_STATIC + URL
            images = find('%s/*.png' % (path))

            Images = []
            for image in images:
                Images.append(image.split('Views')[1])
            return Images
        except KeyError:
            Find.Notify(
                    'Error',
                    "The function have 3 required parameters "
                    "image path and name of directory:")
            Find.Notify(
                    'Example',
                    "Images(Path='Portfolio', Name='bestcon', "
                    "Language='Russian')")
            Find.Notify(
                    'Notice',
                    "If path and directory exists will return result")

    def Documents(**args):
        try:
            URL = "/site/Master_Mind/Data/Documentataion/%s/%s/" % (
                    args['Language'], args['Path'])
            path = Settings.APPLICATION_STATIC + URL
            Documents = {
                    'doc': find('%s/*.doc' % (path)),
                    'docx': find('%s/*.docx' % (path)),
                    'xlsx': find('%s/*.xlsx' % (path)),
                    'csv': find('%s/*.csv' % (path)),
                    'pdf': find('%s/*.pdf' % (path)),
            }

            Doc_Formats = []
            Doc_Path = []
            for doc_format in Documents:
                if len(Documents[doc_format]) is not 0:
                    Doc_Formats.append(doc_format)
                    Doc_Path.append(Documents[doc_format])

            Documents = dict(zip(Doc_Formats, Doc_Path))

            from docx import Document
            from docx.opc.constants import RELATIONSHIP_TYPE as Link

            Titles = []
            Texts = []
            for document in Documents['docx']:
                Document = Document(document)
                for paragraph in Document.paragraphs:
                    if paragraph.style.name == 'Heading 1':
                        Titles.append(paragraph.text)
                    elif paragraph.style.name == 'Body Text':
                        if len(paragraph.text) is not 0:
                            Texts.append(paragraph.text)

            # return dict(Info=dict(Title = Titles, Paragraph=Texts))

            return Documents

        except Exception:
            Find.Notify(
                    'Error', "The function have 2 required parameters "
                             "image path and name of directory:")
            Find.Notify(
                    'Example', "Documents(Path='Services', Language='Russian')")
            Find.Notify(
                    'Notice', "If path and directory exists will return result")