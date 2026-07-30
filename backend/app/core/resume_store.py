latest_resume = None


def save_resume(data):
    global latest_resume
    latest_resume = data


def get_resume():
    return latest_resume