class Jobs(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    jobstart = db.Column(db.Date())
    jobend = db.Column(db.Date())
    jobdescription = db.Column(db.String(500))

    def __init__(self, title, jobstart, jobend, jobdescription):
        self.title = title
        self.jobstart = jobstart
        self.jobend = jobend
        self.jobdescription = jobdescription

    def __repr__(self):
        return self

