class Utils:
    def mail_send(**kwargs):
        mail_to = kwargs.get('mail_to')
        mail_from = kwargs.get('mail_from')
        mail_body = kwargs.get('mail_body')
        mail_subject = kwargs.get('mail_subject')
        print_line = f"mail with subject: {mail_subject} \
            and body {mail_body} will be sent to: {mail_to}"
        print(print_line)
        