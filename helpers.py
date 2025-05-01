from datetime import datetime, timedelta

def tomorrow_date():
    current_date = datetime.now()
    tomorrow_date = current_date + timedelta(days=1)
    date = tomorrow_date.strftime('%d-%m-%Y')
    return date
